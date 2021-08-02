from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import customer, products
from .serializers import MessageSerializer
from .utils.hooks import send_template
from .utils.outbound import send_img_msg, send_qck_msg, send_txt_msg


@api_view(['POST'])
def getmessage(request):
    try:
        if request.method=='POST':
            mesdata=request.data.get('payload')
            #print(mesdata['payload']['text'])

            ###view more btton cod3e
            try:
                if mesdata['payload']['id']=='more':
                    usr=customer.objects.filter(number=mesdata['source'])
                    
                    if usr:
                        usr=usr[0]
                        product = products.objects.filter(name=usr.product_searched).order_by('id')
                        l=usr.last_product_id
                        print(l)
                        c=product.count()
                        c=c-l
                        if c>5:
                            print('d')
                            productdepricated=product[l:(l+5)]
                            t=l
                            result=''
                            for i in productdepricated:
                            
                                t+=1
                                #result=str(t)+"}"+i.short_desc.upper()+": \n"+"Price:"+str(i.price)+"\n"+"Buy:"+i.page+"\n\n"
                                result=str(t)+".*"+i.short_desc.upper()+"* : \n"+"*Price:* "+str(i.price)+"\n"+"*Buy:* "+i.page
                                usr.last_product_id=t
                                send_img_msg(mesdata['source'],"https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg","https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg",result)
                                #usr.product_searched=mesdata['payload']['text']
                            usr.save()
                          #  print(send_template(mesdata['source'],result))
                        else:
                            productdepricated=product[l:]
                            usr.delete()
                            t=l
                            result=''
                            for i in productdepricated:
                                t+=1
                                result=str(t)+".*"+i.short_desc.upper()+"* : \n"+"*Price:* "+str(i.price)+"\n"+"*Buy:* "+i.page
                                #result=str(t)+"}"+i.short_desc.upper()+": \n"+"Price:"+str(i.price)+"\n"+"Buy:"+i.page+"\n\n"
                                send_img_msg(mesdata['source'],"https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg","https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg",result)
                           # print(send_template(mesdata['source'],result))
                    else:
                        print(send_template(mesdata['source'],"Search something First Idiot"))
                        
                print("sdas")
                return HttpResponse(status=200)            
            except:
                pass

           
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
                        result=str(t)+".*"+i.short_desc.upper()+"* : \n"+"*Price:* "+str(i.price)+"\n"+"*Buy:* "+i.page
                        send_img_msg(mesdata['source'],"https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg","https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg",result)
                else:
                    productdepricated=product[0:5]
                    usr=customer.objects.filter(number=mesdata['source'])
                    if usr :
                        usr=usr[0]
                        result=''
                        productdepricated=product[0:5]
                        for i in productdepricated:
                            t+=1
                            result=str(t)+".*"+i.short_desc.upper()+"* : \n"+"*Price:* "+str(i.price)+"\n"+"*Buy:* "+i.page
                            usr.last_product_id=t
                            usr.product_searched=mesdata['payload']['text']
                            usr.save()
                            send_img_msg(mesdata['source'],"https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg","https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg",result)
                    else:
                        usr=customer(number=mesdata['source'],product_searched=mesdata['payload']['text'])
                        result=''
                        for i in productdepricated:
                            t+=1
                            result=str(t)+".*"+i.short_desc.upper()+"* : \n"+"*Price:* "+str(i.price)+"\n"+"*Buy:* "+i.page
                            usr.last_product_id=t
                            usr.product_searched=mesdata['payload']['text']
                            send_img_msg(mesdata['source'],i.image,i.image,result)

                        usr.save()

               # print(send_template(mesdata['source'],result)) 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        else :
            return HttpResponse(status=200)
    except:
        return HttpResponse(status=205)
