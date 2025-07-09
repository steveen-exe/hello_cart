from django.db import models
#product-items

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    Delete_status = ((LIVE, 'Live'), (DELETE, 'Delete'))

    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/products')
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=Delete_status, default=LIVE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) ->  str:
        return self.title
    
