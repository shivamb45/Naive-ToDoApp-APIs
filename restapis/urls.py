from django.urls import path
from restapis.views import listTasks, addTask, taskDetail, editTask
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tasks/',listTasks),
    path('addTask/',addTask),
    path('viewTask/<int:id>/',taskDetail),
    path('editTask/<int:id>/',editTask),
]
# 
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json',])
