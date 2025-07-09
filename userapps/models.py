from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #first_name, last_name, password1, password2,email,us
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    profile_pix = models.ImageField(upload_to='userpix',default='https://media.istockphoto.com/id/2151669184/vector/vector-flat-illustration-in-grayscale-avatar-user-profile-person-icon-gender-neutral.jpg?s=612x612&w=0&k=20&c=UEa7oHoOL30ynvmJzSCIPrwwopJdfqzBs0q69ezQoM8=')

    def __str__(self):
        return self.fullname