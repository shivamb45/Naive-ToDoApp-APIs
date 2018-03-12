from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from restapis.models import Tasks
from restapis.serializers import TasksSerializer


@api_view(['GET',])
@renderer_classes((JSONRenderer,))
def listTasks(request,format='json'):
    tasks = Tasks.objects.all()
    response = dict()
    response['status'] = 'ok'
    serializedObjs = TasksSerializer(tasks,many=True)
    response['tasks'] = serializedObjs.data
    return Response(response)

@api_view(['POST',])
@renderer_classes((JSONRenderer,))
def addTask(request):

    data = JSONParser().parse(request)
    serializedNewTask = TasksSerializer(data=data)
    if not serializedNewTask.is_valid():
        response = dict()
        response['status'] = 'Invalid Input!'
        return Response(response)
    else:
        serializedNewTask.save()
        response = dict()
        response['status'] = 'ok'
        response['task'] = serializedNewTask.data
        return Response(response)

@api_view(['GET',])
@renderer_classes((JSONRenderer,))
def taskDetail(request,id):

    try:
        task = Tasks.objects.get(taskId=id)
        serializedTask = TasksSerializer(task)
        response = dict()
        response['status'] = 'ok'
        response['task'] = serializedTask.data
        return JsonResponse(response,status=200)

    except Exception as e:
        response = dict()
        response['status'] = 'Invalid taskId ! No matching Task Found!'
        return JsonResponse(response,status=404)

@api_view(['POST',])
@renderer_classes((JSONRenderer,))
def editTask(request,id):

    try:
        task = Tasks.objects.get(taskId=id)
        data = JSONParser().parse(request)
        try:
            if data['taskId'] != id:
                response = dict()
                response['status'] = "CRITICAL! The taskId in JSON object and API URL doesn't match."
                response['error'] = 'Supplied id in URL {} whereas id in JSON object is {}'.format(id,data['taskId'])
                return JsonResponse(response,status = 400)
            else:
                serializedTask = TasksSerializer(task,data=data)
                if serializedTask.is_valid():
                    serializedTask.save()
                    response = dict()
                    response['status'] = 'ok'
                    response['task'] = serializedTask.data
                    return JsonResponse(response)
                else:
                    response = dict()
                    response['status'] = 'Error Ocurred While Parsing JSON'
                    response['error'] = serializedTask.errors
                    return JsonResponse(response,status=400)
        except:
                response = dict()
                response['status'] = "Important! The taskId in JSON object is required for editing"
                response['error'] = 'No taskId found in JSON object supplied.'
                return JsonResponse(response,status = 400)

    except Exception as e:
        response = dict()
        response['status'] = 'Invalid taskId ! No matching Task Found!'
        if not request.POST:
            response['status'] = '!!! No JSON Object Supplied.'
        return JsonResponse(response,status=404)
