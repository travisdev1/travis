from .models import Message

def packets_sent_processor(request):
    packets_sent = Message.objects.filter(status="sent").count()
    return {'packets_sent': packets_sent}
