from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('display/<int:pk>',views.display,name='display'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('add/',views.add,name='add'),
    path('update/<int:pk>',views.update,name='update'),
]
