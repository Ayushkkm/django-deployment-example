from django.urls import path
from project import views

# TEMPLATE TAGGING , used in relative html page 
app_name = 'project'

urlpatterns = [
    path("relative/",views.relative,name='relative'),
    path("other/",views.other,name='other'),
]