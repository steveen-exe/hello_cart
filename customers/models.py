from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    Delete_status = ((LIVE, 'Live'), (DELETE, 'Delete'))

    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User ,related_name='customer_profile',on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    delete_status = models.IntegerField  (choices= Delete_status ,default = LIVE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) ->  str:
        return self.title
