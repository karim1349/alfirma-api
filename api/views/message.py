from rest_framework import viewsets, mixins
from api.models import Message
from api.serializers import MessageSerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

class MessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save()
        message = serializer.instance
        subject = 'New message from {}'.format(message.name)
        html_message = render_to_string('message.html', {'message': message})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = settings.EMAIL_HOST_USER
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
