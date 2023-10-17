from django.db import models
from datetime import datetime,date

class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=60,unique=True)
    password=models.CharField(max_length=60)
    status=models.BooleanField(default=False)
    
    role=models.CharField(max_length=20)



class restaurants(models.Model):
    r_id=models.AutoField(primary_key=True)
    r_name=models.CharField(max_length=60)
    r_location=models.CharField(max_length=60)
    license_number=models.CharField(max_length=60)
    license_photo=models.ImageField(upload_to='license/',null=True)
    r_photo=models.ImageField(upload_to='restaurent_photo/',null=True)
    r_mobile=models.CharField(max_length=12,unique=True)
    r_mail=models.EmailField(max_length=30)
    LOGIN_id=models.ForeignKey(login,on_delete=models.CASCADE)

class dishes(models.Model):
    d_id=models.AutoField(primary_key=True)
    d_name=models.CharField(max_length=60)
    d_photo=models.ImageField(upload_to='dish/',null=True)
    d_price=models.FloatField()
    restaurant=models.ForeignKey(restaurants,on_delete=models.CASCADE)
    d_discription=models.CharField(max_length=200,default='none')

class table(models.Model):
    t_id=models.AutoField(primary_key=True)
    number_table=models.IntegerField()
    
    t_capacity=models.IntegerField()
    status=models.CharField(max_length=20,default='available')
    RESTAURANT=models.ForeignKey(restaurants,on_delete=models.CASCADE,default=None)
    total=models.IntegerField()
    
    



class offer(models.Model):
    dish=models.CharField(max_length=60)
    of_code=models.CharField(max_length=50)
    offer=models.CharField(max_length=50)
    discount_percentage=models.FloatField(default=None)
    from_date=models.DateField(max_length=20,null=True)
    to_date=models.DateField(max_length=20,null=True)
    DISH=models.ForeignKey(dishes,on_delete=models.CASCADE)
    RESTAURANT=models.ForeignKey(restaurants,on_delete=models.CASCADE,default=None)
    active=models.BooleanField(default=False)

class customer(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=60)
    c_phone=models.CharField(max_length=12)
    c_mail=models.EmailField(max_length=50)
    c_password=models.CharField(max_length=60)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class cart(models.Model):
    ct_id=models.AutoField(primary_key=True)
    ct_dish=models.ForeignKey(dishes,on_delete=models.CASCADE)
    ct_restaurant=models.ForeignKey(restaurants,on_delete=models.CASCADE)
    ct_customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    status=status=models.CharField(max_length=60,default='pending')

class dining(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    phone=models.CharField(max_length=12)
    mail=models.EmailField(max_length=50)
    time=models.TimeField(auto_now=False,auto_now_add=False)
    date=models.DateTimeField()
    NOP=models.IntegerField()
    s_request=models.CharField(max_length=500)
    RESTAURANT=models.ForeignKey(restaurants,on_delete=models.CASCADE,default=None)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,default=None)
    


class events(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    phone=models.CharField(max_length=12)
    mail=models.EmailField(max_length=50)
    
    date=models.DateTimeField()
    NOP=models.IntegerField()
    event_type=models.CharField(max_length=60)
    s_request=models.CharField(max_length=500)
    RESTAURANT=models.ForeignKey(restaurants,on_delete=models.CASCADE,default=None)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,default=None)

class complaint(models.Model):
    complaints=models.CharField(max_length=2000)
    restaurant=models.CharField(max_length=60)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,default=None)

class feedback(models.Model):
    feedback=models.CharField(max_length=2000)
    RESTAURANT=models.ForeignKey(restaurants,on_delete=models.CASCADE,default=None)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,default=None)

class payment(models.Model):
    id=models.AutoField(primary_key=True)
    amount=models.CharField(max_length=20)
    status=models.CharField(max_length=30)
    RESTAURANT=models.ForeignKey(restaurants,on_delete=models.CASCADE,default=None)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,default=None)
    type=models.CharField(max_length=30)
    date=models.DateField()


class address(models.Model):
    id=models.AutoField(primary_key=True)
    district=models.CharField(max_length=20,default='Ernakulam')
    city=models.CharField(max_length=60,default='')
    street=models.CharField(max_length=200,default='')
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,default=None)



   
    
class order(models.Model):
    id=models.AutoField(primary_key=True)
    status=models.CharField(max_length=30)
    RESTAURANT=models.ForeignKey(restaurants,on_delete=models.CASCADE,default=None)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,default=None)
    payment=models.ForeignKey(payment,on_delete=models.CASCADE,default=None)
    address=models.ForeignKey(address,on_delete=models.CASCADE,default=None)
    order_number=models.CharField(max_length=30)
    date=models.DateField(default=datetime.now())
    
class baseorder(models.Model):
    id=models.AutoField(primary_key=True)
    dish=models.CharField(max_length=70,default='')
    discription=models.CharField(max_length=60,default='')
    quantity=models.CharField(max_length=60,default='')
    date=models.DateField()
    status=models.CharField(max_length=60,default='pending')
    RESTAURANT=models.ForeignKey(restaurants,on_delete=models.CASCADE,default=None)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,default=None) 
    order=models.ForeignKey(order,on_delete=models.CASCADE,default=None) 
    amount=models.FloatField()  
    

    











    
    



    
    



    

    












