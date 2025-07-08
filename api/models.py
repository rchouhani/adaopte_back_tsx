from django.db import models

# Create your models here.
class Pets_Statuses(models.Model):
    status_title = models.CharField(max_length=48)

    def __str__(self):
        return self.status_title
    

class Admins(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username


class Availabilities(models.Model):
    frequency = models.CharField(max_length=255)

    def __str__(self):
        return self.frequency
    

class Users(models.Model):
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=1024)
    phone = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250)
    motivation = models.CharField(max_length=1024)
    volunteer = models.BooleanField(default=False)
    adoptant = models.BooleanField(default=False)
    availability_id = models.ForeignKey(Availabilities, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.firstname, self.lastname, self.city, self.email
    

class Donations(models.Model):
    amount_euros = models.IntegerField()
    user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount_euros
    

class Pets(models.Model):
    pet_name = models.CharField(max_length=250)
    status_id = models.ForeignKey(Pets_Statuses, on_delete=models.DO_NOTHING)
    birthyear = models.DateField(auto_now=False, auto_now_add=False)
    breed =  models.CharField(max_length=250)
    pet_type =  models.CharField(max_length=250)
    city =  models.CharField(max_length=250)
    zipcode =  models.CharField(max_length=250)
    pet_description = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pet_name
    

class Petting_Dates(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    pet_id = models.ForeignKey(Pets, on_delete=models.DO_NOTHING)
    appointment = models.DateTimeField(auto_now=False, auto_now_add=False)
    duration_minutes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.appointment
    

class Adoptions(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    pet_id = models.ForeignKey(Pets, on_delete=models.DO_NOTHING)
    adoptions_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.adoptions_date