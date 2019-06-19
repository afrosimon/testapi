from django.contrib import admin
from django.urls import path
from message.views import message_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', message_list)
]
