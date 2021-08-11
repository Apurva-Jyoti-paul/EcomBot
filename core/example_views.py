from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import customer, products
from .serializers import MessageSerializer
from .webhooks import send_products, send_template


@api_view(['POST'])
def hook(request):
    if request.method == 'POST':
        try:
            if request.data.get('type') == 'message':
                payload:dict = request.data.get('payload')
                send_products(payload['source'], keyword = payload['payload']['text'])
            return Response(status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)
    
    else:
        return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)
