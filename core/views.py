from django.shortcuts import render,redirect
import json
from .models import message
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer
from rest_framework import status

#@csrf_exempt
@api_view(['POST'])
def getmessage(request):
    if request.method=='POST':
        #data=json.loads(request.body.decode('utf-8'))
        #data = {'message': request.DATA.get('the_post'), 'author': request.user.pk}

        mesdata=request.data.get('payload')
        print(mesdata['payload']['text'])
        databuffer={
            'mesgcont':mesdata['payload']['text'],
            'source' : mesdata['source'],
            'conttype':mesdata['type'],
            'sender':mesdata['sender']['name'],
            'countrycode':mesdata['sender']['country_code'],
            'dialcode': mesdata['sender']['dial_code']
            }
        serializer = MessageSerializer(data=databuffer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #print(mesdata['payload']['text'])
        #return HttpResponse(status=200)
    else :
        return HttpResponse(status=400)
 





# Create your views here.
