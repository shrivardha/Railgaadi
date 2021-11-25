from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Add_Train(models.Model):
    trainname = models.CharField(max_length=30,null=True)
    train_no = models.IntegerField(null=True)
    from_city = models.CharField(max_length=30,null=True)
    to_city = models.CharField(max_length=30,null=True)
    departuretime=models.TimeField(null=True)
    arrivaltime=models.TimeField(null=True)
    traveltime=models.TimeField(null=True)
    distance=models.IntegerField(null=True)
    img=models.FileField(default= 'default.jpg', upload_to ='train.pics')
    #no_of_seats=models.IntegerField()
    def __str__(self):
        return self.trainname+" "+str(self.train_no)

class Add_route(models.Model):
    train = models.ForeignKey(Add_Train,on_delete=models.CASCADE,null=True)
    route = models.CharField(max_length=100,null=True)
    distance=models.IntegerField(null=True)
    fare=models.IntegerField(null=True)
    def __str__(self):
        return self.route+" "+str(self.train.train_no)

class Passenger(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    train = models.ForeignKey(Add_Train,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=30,null=True)
    route=models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=30,null=True)
    date1 = models.DateField(null=True)
    fare = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username+" : "+self.name

class Book_ticket(models.Model):
    passenger=models.ForeignKey(Passenger,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    route=models.CharField(max_length=100,null=True)
    date2=models.DateField(null=True)
    fare=models.IntegerField(null=True)
    def __str__(self):
        return self.user.username+" : "+self.route

class Asehi(models.Model):
    fare = models.IntegerField(null=True)
    train_name = models.CharField(max_length=30,null=True)
    date3 = models.DateField(null=True)



