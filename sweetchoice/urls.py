from django.urls import path,include
from . import views

urlpatterns = [
				path("",views.index,name = "index"),
				path("send_message",views.test,name="test")
]