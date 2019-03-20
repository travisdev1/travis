from django.contrib import admin
from happinesspackets.messaging.models import Message, BlacklistedEmail

admin.site.register(Message)
admin.site.register(BlacklistedEmail)
