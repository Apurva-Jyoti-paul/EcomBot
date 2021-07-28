from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import products
from .serializers import MessageSerializer
from .utils.hooks import send_template


@api_view(['POST'])
def getmessage(request):
    try:
        if request.method=='POST':
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
        else :
            return HttpResponse(status=200)
    except:
        return HttpResponse(status=205)
