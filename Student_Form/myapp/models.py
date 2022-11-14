from django.db import models
from . validators import gmail_validation
# Create your models here.

standard = (
    ("1", "First"),
    ("2", "Second"),
    ("3", "Third"),
    ("4", "Fourth"),
    ("5", "Fifth"),
    ("6", "Sixth"),
    ("7", "Seventh"),
    ("8", "Eigth"),
    ("9", "Ninth"),
    ("10", "Tenth"),
    ("11", "Eleventh"),
    ("12", "Tweleth"),
)
class Student(models.Model):
    full_Name = models.CharField( max_length=50,blank=False,null=True,)
    email = models.EmailField(max_length=100,blank=False, null=True, validators=[gmail_validation],)
    age = models.IntegerField( max_length=50 ,blank=False,null=True )

    Class = models.CharField(max_length = 20,choices = standard, default = '1')
    description = models.TextField()


