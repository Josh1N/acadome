from django.db import models

# Create your models here.

class Room(models.Model):
    # host = models.CharField(max_length=255)
    # topic = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # participants = models.ManyToManyField(Participant)    
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name()