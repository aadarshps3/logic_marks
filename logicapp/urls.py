
from django.urls import path

from logicapp import views

urlpatterns = [
      path('markview',views.markview,name="markview")
]