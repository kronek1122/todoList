from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=50)
    todo_text = models.CharField(max_length = 500)
    condition = models.BooleanField(default=False)
    #piority = models.BooleanField()
    creation_time = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(User,on_delete = models.CASCADE )

    def __str__(self):
        return self.title
    
