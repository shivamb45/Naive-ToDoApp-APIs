from django.db import models

# Create your models here.

class Tasks(models.Model):
    taskId = models.AutoField(primary_key=True)
    taskName = models.TextField()
    isDone = models.BooleanField(blank=True,default=False)
    doneAt = models.DateTimeField(blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return "#"+str(self.taskId)+": "+str(self.taskName)
