from rest_framework import serializers
from restapis.models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('taskId','taskName','isDone','doneAt','createdAt')
