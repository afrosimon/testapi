from rest_framework.decorators import api_view
from rest_framework.response import Response
from message.models import Message
from message.serializers import MessageSerializer


@api_view(['GET'])
def message_list(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data)
