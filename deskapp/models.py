from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Passenger(models.Model):
    phnNo_validator = RegexValidator(
        regex=r'^(?:7|0|(?:\+94))[0-9]{9,10}$',
        message='Enter a valid Sri Lankan phone number.'
    )

    teleno_validator = RegexValidator(
        regex=r'0((11)|(2(1|[3-7]))|(3[1-8])|(4(1|5|7))|(5(1|2|4|5|7))|(6(3|[5-7]))|([8-9]1))[0-9]{7}',
        message='Enter a valid Sri Lankan telephone number.'
    )

    email_validator = RegexValidator(
         regex=r'^[\w.\-]+@[\w.\-]+\.[a-zA-Z]{2,}$',
        message= 'Email not valid'
    )
    nic_validator= RegexValidator(
       regex=r'^(([5,6,7,8,9]{1})([0-9]{1})([0,1,2,3,5,6,7,8]{1})([0-9]{6})([v|V|x|X]))|(([1,2]{1})([0,9]{1})([0-9]{2})([0,1,2,3,5,6,7,8]{1})([0-9]{7}))',
       message='nic number not valid'
   )

    registration_number  = models.IntegerField(unique=True, null=False)
    passport_number  = models.TextField(unique=True, null=False)
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    nic =models.CharField(validators=[nic_validator],max_length =12,unique=True, null=False)
    mobile = models.CharField(validators=[phnNo_validator],max_length =12,unique=True, null=False)
    telephone = models.CharField(validators=[teleno_validator],max_length=12,null=False)
    email = models.TextField(validators=[email_validator],unique=True, null=False)
    address= models.TextField(null=False)


    def __str__(self):
        return self.task_title
