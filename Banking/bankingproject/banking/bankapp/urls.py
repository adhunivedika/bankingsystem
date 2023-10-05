from. import views
from django.urls import path
app_name='bankapp'
urlpatterns = [

    path('',views.demo,name='demo'),
    path('status',views.status,name='status'),
    path('form_view',views.form_view,name='form_view'),
]