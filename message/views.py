from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator
from message.models import Message
from message.serializers import MessageSerializer


DEFAULT_MESSAGE_PER_PAGE = 100


@api_view(['GET'])
def message_list(request):
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', DEFAULT_MESSAGE_PER_PAGE)

    message_list = Message.objects.order_by('-created').all()
    paginator = Paginator(message_list, per_page)

    messages = paginator.get_page(page)
    serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data)
