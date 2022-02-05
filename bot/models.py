from django.db import models

# Create your models here.
class User(models.Model):
    ProfileName = models.CharField(max_length=100)
    WaId = models.IntegerField()
    
    def __str__(self):
        return self.ProfileName
    
class Message(models.Model):
    user = models.ForeignKey(User, related_name='message',on_delete=models.CASCADE)
    SmsStatus = models.CharField(max_length=100)
    Body = models.CharField(max_length=100)

    def __str__(self):
        return self.Body
