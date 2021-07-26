from os import name
from django.shortcuts import render,redirect
import json
from .models import message,products,customer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer
from rest_framework import status
from .utils.hooks import send_template
#@csrf_exempt
@api_view(['POST'])
def getmessage(request):
   # try:
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
            # print(send_template("917365960750","Rafi Chuustiya hai"))
            product = products.objects.filter(name=mesdata['payload']['text']).order_by('id')
            t=0
            if product.count() < 5 :
                result=''
                for i in product:
                    t+=1
                    result=result+str(t)+"}"+i.short_desc.upper()+": \n"+"Price:"+str(i.price)+"\n"+"Buy:"+i.page+"\n\n"
            print(send_template(mesdata['source'],result)) 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_200_OK)
    #print(mesdata['payload']['text'])
    #return HttpResponse(status=200)
    else :
        return HttpResponse(status=200)
   # except:
    #    return HttpResponse(status=205)





# Create your views here.
