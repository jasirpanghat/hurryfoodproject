from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
# import requests
from django.http import HttpResponse
from datetime import datetime,timedelta,date
from django.utils import timezone
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
import random




# def login(request):
#     return render(request,"login.html")
# ___________admin_______
def landing(request):
    return render(request,'index.html')
def index(request):
    return render(request,"home.html")



def login_(request):
    if request.method=='POST':
        try:

            username=request.POST['admin']
            password=request.POST['ps']
            print(username)
            print(password)
            data=login.objects.get(username=username,password=password)
            

            if data.role=='ADMIN':
                return redirect(admin_home)
            elif data.role=='RESTAURANT':

                print('hhhhh')
                request.session['lid']=data.login_id
                print('jjjj')
                r=restaurants.objects.get(LOGIN_id=data.login_id)
                request.session['rest']=r.r_id

            
                return render(request,"restuarant_templates/dashbord.html")
            
            elif data.role=='CUSTOMER':
                request.session['cid']=data.login_id
                c=customer.objects.get(LOGIN=data.login_id)
                request.session['cust']=c.c_id
                
                return render(request,"customer_templates/dashbord.html")
        except:       

            return render(request,'login_index.html')
            


    else:
        return render(request,'login_index.html')


def admin_home(request):
    
    return render(request,'admin_templates/dashbord.html')

def restuarent_register(request):
    
    if request.method=='POST':

        data=restaurants()
        data.r_name=request.POST['rest_name']
        data.r_location=request.POST['rest_location']
        data.license_number=request.POST['rest_licnum']
            
            
        data.r_mobile=request.POST['rest_mob']
        data.r_mail=request.POST['rest_mail']
              
        a=request.POST['rest_mail']
        b=request.POST['rest_mob']


            
              
            






        if len(request.FILES) != 0:
            data.license_photo=request.FILES['file1']
            data.r_photo=request.FILES['file2']

            log_data=login()
            log_data.username=request.POST['rest_mail']
            log_data.password=request.POST['rest_mob']
            log_data.status=False
            log_data.role='RESTAURANT'



            log_data.save()


            data.LOGIN_id=login.objects.last()

    
            data.save()
            return redirect(landing)
        
    
    return render(request,"restuarant_templates/restaurant_register.html")

def view_restaurant(request):
    res=restaurants.objects.all()

    return render(request,"admin_templates/view_restaurant.html",{'res':res})
def block(request,id):
    rest=login.objects.get(login_id=id)
    rest.status=False
    rest.save()
    
    



    return  redirect(view_restaurant)


def view_block(request):
    res=restaurants.objects.all()
    return render(request,"admin_templates/view_unblock.html",{'res':res})

def unblock(request,id):
    rest=login.objects.get(login_id=id)
    rest.status=True
    rest.save()
    
    return  redirect(view_restaurant)

def edit_restaurant(request,id):
    
    
    res=restaurants.objects.get(LOGIN_id=id)
    log=login.objects.get(login_id=id)
    if request.method=='POST':
        res.r_name=request.POST['rest_name']
        res.r_location=request.POST['rest_location']
        res.license_number=request.POST['rest_licnum']
            
            
        res.r_mobile=request.POST['rest_mob']
        res.r_mail=request.POST['rest_mail']
        res.license_photo=request.FILES['file1']
        res.r_photo=request.FILES['file2']
        log.username=request.POST['rest_mail']
        log.password=request.POST['rest_mob']
        log.save()

        res.save()

                
                
        
                

                

        return redirect(view_restaurant)
              
        


    return render(request,'admin_templates/restaurent_edit.html',{'res':res})





# ______________restuarent_________

def restuarant_(request):
    return render(request,"restuarant_templates/dashbord.html")
def add_dish(request):
    if request.method=='POST':
        d_data=dishes()
        d_data.d_name=request.POST['textfield']
        d_data.d_discription=request.POST['textfield1']
        d_data.d_price=request.POST['textfield2']
        

        if len(request.FILES) != 0:
            d_data.d_photo=request.FILES['file']
            d_data.restaurant=restaurants.objects.get(LOGIN_id=request.session['lid'])
            d_data.save()
    return render(request,"restuarant_templates/add_dishes.html")


def view_dishes(request):

    res=dishes.objects.filter(restaurant=request.session['rest'])
    
    return render(request,'restuarant_templates/view_dishes.html',{'res':res})

def add_offer(request):
    res=dishes.objects.filter(restaurant=request.session['rest'])
    data=offer()
    if request.method=='POST':
        did=request.POST['select']
        data.dish=request.POST['select']
        data.of_code=request.POST["textfield1"]
        data.offer=request.POST["textfield2"]
        data.discount_percentage=request.POST["textfield3"]
        data.from_date=request.POST["textfield4"]
        data.to_date=request.POST["textfield5"]
        data.DISH=dishes.objects.get(d_id=did)
        data.RESTAURANT=restaurants.objects.get(r_id=request.session['rest'])
        data.save()
    return render(request,"restuarant_templates/add_offer.html",{'res':res})

def view_offer(request):

    
    res=offer.objects.filter(RESTAURANT=request.session['rest'])
    return render(request,"restuarant_templates/view_offer.html",{'res':res})
 
    
def add_table(request):
    data=table()
    
    if request.method=='POST':
        res=table.objects.filter(RESTAURANT=request.session['rest'])
        data.number_table=request.POST['textfield']
        data.total=request.POST['textfield2']

        data.t_capacity=request.POST['textfield2']
        data.RESTAURANT=restaurants.objects.get(r_id=request.session['rest'])
        data.save()
        

            
        
            
        
        
       

    return render(request,"restuarant_templates/add_table.html")
def view_table(request):
    res=table.objects.filter(RESTAURANT=request.session['rest'])
    return render(request,"restuarant_templates/view_table.html",{'res':res})
def edit_table(request,id):
    res=table.objects.get(t_id=id)
    if request.method=='POST':
        a=request.POST['textfield']
        b=request.POST['textfield2']
        res.number_table=res.number_table+int(a)
        res.total=res.total+int(b)
        res.t_capacity=res.t_capacity+int(b)
        res.save()
        return redirect(view_table)






    return render(request,"restuarant_templates/edit_table.html",{'res':res})

def delete_table(request,id):
    res=table.objects.get(t_id=id)
    res.delete()
    return redirect(view_table)


        
    

def edit_dish(request,id):
    data=dishes.objects.get(d_id=id)
    if request.method=='POST':
        data.d_name=request.POST['textfield']
        data.d_discription=request.POST['textfield1']
        data.d_price=request.POST['textfield2']
        

        if len(request.FILES) != 0:
            data.d_photo=request.FILES['file']
            data.save()

            return redirect(view_dishes)
    return render(request,'restuarant_templates/edit_dishes.html',{'res':data})
def delete_dish(request,id):
    dish=dishes.objects.get(d_id=id)
    dish.delete()
    return redirect(view_dishes)
def edit_offer(request,id):
    data=offer.objects.get(DISH=id)
    if request.method=='POST':
        
        data.dish=request.POST['name']
        data.of_code=request.POST["textfield1"]
        data.offer=request.POST["textfield2"]
        data.discount_percentage=request.POST["textfield3"]
        data.from_date=request.POST["textfield4"]
        data.to_date=request.POST["textfield5"]
       
        data.save()
        return redirect(view_offer)
    return render (request,'restuarant_templates/edit_offer.html',{'res':data})
def delete_offer(request,id):
    data=offer.objects.get(DISH=id)
    data.delete()
    return redirect(view_offer)

def view_dining_reservation(request):

    data=dining.objects.filter(RESTAURANT=request.session['rest'])

    return render(request,"restuarant_templates/view_dining_reservation.html",{'res':data})

def view_event_reservation(request):

    data=events.objects.filter(RESTAURANT=request.session['rest'])
    
    return render(request,"restuarant_templates/view_event_reservation.html",{'res':data})




# _________________customer__________


def customer_register(request):
   
    if request.method=='POST':
        try:

                data=customer()
                data.c_name=request.POST['textfield1']
                data.c_phone=request.POST['textfield2']
                data.c_mail=request.POST['textfield3']
                data.c_password=request.POST['textfield5']


                log=login()
                log.username=request.POST['textfield3']
                log.password=request.POST['textfield5']
                log.status=True
                log.role="CUSTOMER"
                
                log.save()

                data.LOGIN=login.objects.last()
                data.save()


                
                name=request.POST['textfield1']     
                a=request.POST['textfield3']
                b=request.POST['textfield5']
                print('hhhh')


                subject = " HURRY FOOD " 
                message = f''' Welcome {name} To Hurry Food
                                You are registered successfully'''
                                            
                recipient = request.POST['textfield3']
                send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=True)

                return redirect(landing)
        except:

            return render(request,"customer_templates/register_index.html")   
    
        
    
    return render(request,"customer_templates/register_index.html")
def cust_home(request):
    return render(request,"customer_templates/dashbord.html")

def view_restuarents(request):

    res=restaurants.objects.all()

    return render(request,"customer_templates/View_restuarant.html",{'res':res})
def view_home(request,id):
    request.session['vid']=id
    request.session['rid']=id

    return render(request,"customer_templates/viewhome.html")

def cview_dish(request):
    drs=dishes.objects.filter(restaurant=request.session['vid'])

    return render(request,"customer_templates/view_dish.html",{'res':drs})


def cview_offers(request):
    orf=offer.objects.filter(RESTAURANT=request.session['vid'])
    print(orf)

    return render(request,"customer_templates/view_custoffer.html",{'res':orf})
def add_cart(request,id):
    
    request.session['off']=id
    di=dishes.objects.get(d_id=id)
    

    
    
    d=cart.objects.filter(ct_customer=request.session['cust'])
    if request.method=='POST':
        addcart=cart()
        addcart.quantity=request.POST["textfield"]
        addcart.ct_dish=dishes.objects.get(d_id=id)
        addcart.ct_customer=customer.objects.get(LOGIN=request.session['cid'])
        addcart.ct_restaurant=restaurants.objects.get(r_id=request.session['vid'])
        data=cart.objects.filter(ct_customer=request.session['cust'],status="pending")
        if data.exists():
            data=cart.objects.filter(ct_customer=request.session['cust'],status="pending")
            for i in data:

            
                if di.restaurant !=i.ct_restaurant :
                        h="Multiple restaurants order not allowed"
                        
                        return render(request,"customer_templates/add_cart.html",{'message':h})
                        
                
                else:
                    if di.d_id == i.ct_dish.d_id:
                        h="This item is already in cart"
                        return render(request,"customer_templates/add_cart.html",{'message':h})
                        
                        
                    else:
                        h='succesfully added into cart'
                        
                        addcart.save()
                        return redirect(view_cart)
                        
                        
            
            
        else:
            h='succesfully added into cart'
            
            addcart.save()

            return redirect(view_cart)
    else:
        return render(request,"customer_templates/add_cart.html")
 
    
def view_cart(request):
    data=cart.objects.filter(ct_customer=request.session['cust'],status='pending')
    datas=order.objects.all()
    
    return render(request,"customer_templates/view_cart.html",{'res':data,'ras':datas})
    
def place_order(request):
    
    data=cart.objects.filter(ct_customer=request.session['cust'])
    off=offer.objects.filter(RESTAURANT=request.session['vid'])

    l=[]
    for i in data:
        for j in off:
            if i.ct_dish.d_id==j.DISH.d_id:
                ca=i.quantity*(j.DISH.d_price*(1-j.discount_percentage/100))
                l.append(ca)
            else:
                ca=i.ct_dish.d_price*i.quantity
                l.append(ca)
            
    
        print(l)
    sum1=sum(l)

    content={
        'res':data,
        'total':l,
        
    }

   
    return render(request,"customer_templates/place_order.html",content,{'sum1':sum1})

        




def reservation(request):
    
    capa=table.objects.get(RESTAURANT=request.session['vid'])
    if request.method=='POST':
        po=request.POST["party-type"]
        if po=='restaurant-dining':
            a=request.POST['num-of-people']
            print()
            data=dining()
            data.name=request.POST['name']
            data.mail=request.POST['email']
            data.phone=request.POST['phone']
            data.date=request.POST['date']
            data.time=request.POST['time']
            
            data.NOP=request.POST['num-of-people']
            data.s_request=request.POST['special-requests']
            data.RESTAURANT=restaurants.objects.get(r_id=request.session['vid'])
            data.customer=customer.objects.get(LOGIN=request.session['cid'])
            data.status='Booked'
            a=request.POST['num-of-people']

            cap=table.objects.get(RESTAURANT=request.session['vid'])
            cap.t_capacity=cap.t_capacity-int(a)
            date=request.POST['date']
            time=request.POST['time']
            reservation_time = datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
            cutoff_time = datetime.now() + timedelta(hours=24)

            if reservation_time < cutoff_time:
                print('fgujhbjnjnkj')
                
            # Save reservation to database
                if cap.t_capacity >= int(a):
                    if int(a) >= 4 and int(a) <= 10 :
                        
                        data.save()
                        cap.save()
                        return redirect(view_reservation)
                    else:
                        return HttpResponse("morethan 10 people is not allowed for table dining")
                else:
                    messages='sorry for the trouble! restaurant dining is not available'
                    return render(request,"customer_templates/reservation.html",{'res':messages}) 
                
                
            else:
            # Display error message
                error_message = 'Reservation must be made at least 1 hour in advance.'
                # return render(request, 'customer_templates/reservation.html', {'error_message': error_message})
                return HttpResponse("Reservation must be made at least 1 hour in advance.")

            
            
        else:
            b=request.POST['num-of-people']

            data=events()
            data.name=request.POST['name']
            data.mail=request.POST['email']
            data.phone=request.POST['phone']
            data.date=request.POST['date']
            
            data.NOP=request.POST['num-of-guests']
            data.s_request=request.POST['special-requests']
            data.event_type=request.POST["event-type"]
            data.RESTAURANT=restaurants.objects.get(r_id=request.session['vid'])
            data.customer=customer.objects.get(LOGIN=request.session['cid'])
            b=request.POST['num-of-guests']

            ch=request.POST['date']
            print(ch)
            eva=events.objects.filter(RESTAURANT=request.session['vid'],date=ch)
            if eva:
                return HttpResponse("un available for this date")
            else:
                if int(b) >10 :
                    data.save()
                    return redirect(view_reservation)
                else:
                    return HttpResponse("in events we allow morethan 10 peoples")
           

            


    return render(request,"customer_templates/reservation.html",{'av':capa})
def cartplus(request,id):
    data=cart.objects.get(ct_id=id)
    if request.POST['Submit']=='+':
    
        data.quantity=data.quantity+1
        data.save()
        return redirect(view_cart)

    elif request.POST['Submit']=='-':
        if data.quantity==0:
            data.save()
        else:
        
            data.quantity=data.quantity-1
            data.save()
        return redirect(view_cart)
def cartremove(request,id):
    data=cart.objects.get(ct_id=id)
    data.delete()
    return redirect(view_cart)

def complaints(request):
    data=restaurants.objects.all()
    if request.method=='POST':
        cop=complaint()
        
        cop.complaints=request.POST['textarea']
        cop.restaurant=request.POST['select']
        cop.customer=customer.objects.get(LOGIN=request.session['cid'])
        cop.save()
        return render(request,"customer_templates/dashbord.html")
    else:
    
        return render(request,'customer_templates/complaint_register.html',{'res':data})



def view_complaints(request):

    res=complaint.objects.all()

    return render(request,"admin_templates/View_complaints.html",{'res':res})




def view_reservation(request):
    
    res=dining.objects.filter(customer=request.session['cust'])

    eve=events.objects.filter(customer=request.session['cust'])

    return render(request,"customer_templates/view_reservation.html",{'res':res,'ev':eve})
def feedbacks(request):
    if request.method=='POST':
        feed=feedback()
        feed.feedback=request.POST['textarea']
        feed.RESTAURANT=restaurants.objects.get(r_id=request.session['vid'])
        feed.customer=customer.objects.get(LOGIN=request.session['cid'])
        feed.save()
    
    return render(request,"customer_templates/feedback.html")
def view_feedback(request):
    data=feedback.objects.filter(RESTAURANT=request.session['rest'])

    return render (request,'restuarant_templates/view_feedback.html',{'res':data})
     
def cancel_booking(request,id):
    booking = dining.objects.get(id=id)
   
    tab=table.objects.get(RESTAURANT=request.session['vid'])
    tab.t_capacity=tab.t_capacity+booking.NOP
    booking.delete()
    tab.save()
    return redirect(view_reservation)
 
        
        
    
def insertbase(request):
    ad=address.objects.filter(customer=request.session['cust'])
    if ad.exists():
        
        messages="alrady"
    
    else:
    
        if request.method=='POST':
                res=address()
                res.city=request.POST['city']
                res.district=request.POST['select']
                res.street=request.POST['textarea']
                res.customer=customer.objects.get(LOGIN=request.session['cid'])

                res.save()
                
    res=cart.objects.filter(ct_customer=request.session['cust'])

    

            
                
           
    return redirect(addres)

    return render(request,"restuarant_templates/place.html")

def location(request):
    # if request.method == 'POST':
    #     address = request.POST['address']
    #     # Use the Google Maps API to retrieve the location coordinates
    #     response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=AIzaSyDYHbuP58Uw6msURqbIFBoFseRI3iOpMz4')
    #     data = response.json()
    #     location = data['results'][]['geometry']['location']
    if request.method == 'POST':

        location= request.POST['location']
        # api_key = 'AIzaSyDYHbuP58Uw6msURqbIFBoFseRI3iOpMz4'
        # url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}'
        # response = requests.get(url).json()
        # print(location)
        # print(lat = response['results'][0]['geometry']['location']['lat'])
        # lng = response['results'][0]['geometry']['location']['lng']
        # return lat, lng
    return render(request,"customer_templates/address.html")

def your_view_name(request):
    if request.method == 'POST':
        location = request.POST['location']
        lat, lng = requests.get(location)
        context = {'lat': lat, 'lng': lng}
        return render(request, 'customer_templates/address.html', context)
    else:
        
        return render(request,"customer_templates/address.html")
    
def delete_event(request,id):

    data=events.objects.get(id=id)
    data.delete()



    return redirect(view_event_reservation)


        
def payments(request):
    
    data=cart.objects.filter(ct_customer=request.session['cust'],status="pending")
    off=offer.objects.filter(RESTAURANT=request.session['vid'])

    l=[]
    print(data)
    for i in data:
        for j in off:
            if i.ct_dish.d_id==j.DISH.d_id:
                ca=i.quantity*(j.DISH.d_price*(1-j.discount_percentage/100))
                l.append(ca)
                print(ca)
            else:
                ca=i.ct_dish.d_price*i.quantity
                l.append(ca)
                print(ca)

    sum1=sum(l)
    print(sum1)
    return render(request,"customer_templates/payment.html",{'sum1':sum1})


def available(request,id):
    booking = dining.objects.get(id=id)
    data=table.objects.get(RESTAURANT=request.session['rest'])
    data.t_capacity=data.t_capacity+booking.NOP
    data.save()
    booking.delete()
    return redirect(view_dining_reservation)
def place(request):
   
    data=cart.objects.filter(ct_customer=request.session['cust'],status="pending")
    off=offer.objects.filter(RESTAURANT=request.session['vid'])
    print(off)

    l=[]
    for i in data:
        for j in off:
            if i.ct_dish.d_id==j.DISH.d_id:
                ca=i.quantity*(j.DISH.d_price*(1-j.discount_percentage/100))
                l.append(ca)
            else:
                ca=i.ct_dish.d_price*i.quantity
                l.append(ca)
            
    
        print(l)
    sum1=sum(l)

    data1=[data,sum1]

    context={'res':data,'total':l,'sum1':sum1}

    return render(request,'restuarant_templates/place.html',context)    

           
          

  
def addres(request):
    res=address.objects.get(customer=request.session['cust'])
    data=cart.objects.filter(ct_customer=request.session['cust'],status="pending")
    off=offer.objects.filter(RESTAURANT=request.session['vid'])
    
    l=[]
    for i in data:
        for j in off:
            if i.ct_dish.d_id==j.DISH.d_id:
                ca=i.quantity*(j.DISH.d_price*(1-j.discount_percentage/100))
                l.append(ca)
            else:

                ca=i.ct_dish.d_price*i.quantity
                l.append(ca)  
    sum1=sum(l)
    print(sum1)

    return render(request,"customer_templates/address.html",{'res':res,'sum1':sum1})
    




def edit_address(request,id):
    res=address.objects.get(id=id)
    if request.method=='POST':
            
        res.city=request.POST['city']
        res.district=request.POST['select']
        res.street=request.POST['textarea']
        res.save()
        return redirect(addres)
    return render(request,"customer_templates/edit_address.html",{'res':res})   
# from twilio.rest import Client

def confirm(request,sum1):

    sum=sum1
    if request.method=='POST':
        data=payment()
        data.amount=sum1
        data.status="successful"
        data.type='Dining'
        data.customer=customer.objects.get(LOGIN=request.session['cid'])
        data.RESTAURANT=restaurants.objects.get(r_id=request.session['vid'])
        data.date=datetime.now()
        data.save()


        num=customer.objects.get(LOGIN=request.session['cid'])
        na=num.c_mail

        print(na)
        n='+919961478196'
        print(n)
        name=num.c_name
        # body=f'the amount{a} successfully'
        # from1='+13203029387'

        # account_sid='AC8992db3b878244e36eda23cbb87438ea'
        # auth_token='8d0e9a3919f952665ca641cdef8fb263'
        # client=Client(account_sid,auth_token)

        # message=client.messages.create(

        #                                 body=body,
        #                                 from_=from1,
        #                                 to='+91'+na

        #             )

    subject = " HURRY FOOD " 
    message = f''' Hi {name} ,Your payment {sum1} done successfully
                You are orderd successfully
                Thank you'''
                                            
    recipient = na
    send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=True)

   
    
    a=str(random.randint(1000,10000))   

    res=cart.objects.filter(ct_customer=request.session['cust'],status="pending")

    ord=order()
    ord.status="CONFIRM"
    ord.RESTAURANT=restaurants.objects.get(r_id=request.session['vid'])
    ord.customer=customer.objects.get(LOGIN=request.session['cid'])
    ord.payment=data
    ord.address=address.objects.get(customer=request.session['cust'])
    ord.order_number=a
    ord.date==datetime.now().strftime("%Y-%m-%d")
    ord.save()
    
    
    off=offer.objects.filter(RESTAURANT=request.session['vid'])
    
   
        


    for i in res:
        data=baseorder()
        data.dish=i.ct_dish.d_name
        data.discription=i.ct_dish.d_discription
        data.quantity=i.quantity
        data.customer=customer.objects.get(LOGIN=request.session['cid'])
        data.RESTAURANT=restaurants.objects.get(r_id=request.session['vid'])
        data.date=datetime.now()
          
        
        data.status='success'
        data.order=ord 
        for j in off:
            if i.ct_dish.d_id==j.DISH.d_id:
                ca=i.quantity*(j.DISH.d_price*(1-j.discount_percentage/100))
                data.amount=ca
            else:

                ca=i.ct_dish.d_price*i.quantity
                data.amount=ca
        
        data.save()
        
        if i.status=='pending':
            i.status= 'confirm'  
            i.save()  
        
    

    return render(request,"customer_templates/viewhome.html")


def view_payments(request):
    a=payment.objects.filter(RESTAURANT=request.session['rest'])

    return render(request,'restuarant_templates/view_payment.html',{'res':a}) 


def view_order(request):
    base=baseorder.objects.filter(RESTAURANT=request.session['rest'],status='success')
    return render(request,'restuarant_templates/view_delivery_order.html',{'res':base})


def ready(request,id):
    print(id)
    base=baseorder.objects.get(id=id)
    base.status='complete'
    base.save()

    return(view_order)

        

def view_transaction(request):
    l=[]
    data=order.objects.filter(RESTAURANT=request.session['rest'],status="CONFIRM")
    res=payment.objects.filter(RESTAURANT=request.session['rest'],status="successful")
    for i in res:
        am=float(i.amount)
        l.append(am)
    sum1=sum(l)
        
   
    return render(request,'restuarant_templates/transactions.html',{'res':data,'l':sum1})

def cust_vieworder(request):
    res=baseorder.objects.filter(customer=request.session['cust'],date=datetime.now())
    return render(request,'customer_templates/delivery food.html',{'res':res})

def password(request):
    if request.method=='POST':

        rs=login.objects.get(login_id=request.session['lid'])
        rs.password=request.POST["textfield3"]
        rs.save()
        return render(request,'login_index.html')
        
    return render(request,'restuarant_templates/password.html')








def logeout_rest(request):

    # del request.session['lid']
    # del request.session['rest']
    

    return redirect(landing)


def logeout_customer(request):

    del request.session['cid']
    del request.session['cust']
    

    return redirect(landing)

def logeout_admin(request):
    return redirect(landing)

def order_cancel(request,id):
    base=baseorder.objects.get(id=id)
    ord=order.objects.get(id=base.order.id)

    ord.amount=float(ord.payment.amount)-base.amount
    ord.save()
    base.delete()
    return redirect(cust_vieworder)

def approved(request,id):
    res=login.objects.get(login_id=id)
    res.status=True
    res.save()
    re=restaurants.objects.get(LOGIN_id=id)
    a=re.r_mail
    b=re.r_mobile
    subject = 'hurry food'
    message = f"username:{a} password:{b}"
                                    
    recipient = a
    send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False) 
    return redirect(admin_home)
def reject(request,id):
    re=restaurants.objects.get(LOGIN_id=id)
    res=login.objects.get(login_id=id)
    re.delete()
    res.delete()
    return redirect(admin_home)

def view_pending(request):
    res=restaurants.objects.all()

    return render(request,"admin_templates/view_pending.html",{'res':res})

def rest_profile(request):
    res=restaurants.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'restuarant_templates/view_profile.html',{'res':res})

def view_deliverd_order(request):
    base=baseorder.objects.filter(RESTAURANT=request.session['rest'],status='complete')
    return render(request,'restuarant_templates/view_deliverd_order.html',{'res':base})

def search_transaction(request):
    if request.method=='POST':

        fromdate=request.POST['textfield']
        todate=request.POST['textfield2']
        
        base=baseorder.objects.filter(RESTAURANT=request.session['rest'],status='complete',)
        
        print(base)
        
   
        return render(request,'restuarant_templates/view_deliverd_order.html',{'res':base})


    

