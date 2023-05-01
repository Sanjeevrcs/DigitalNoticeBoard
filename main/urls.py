from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('ckeditor/',include('ckeditor_uploader.urls')),
     path('login',loginpage,name='login'),
     path('logout',logoutpage,name='logout'),
     path('template/<page_name>',template,name='template'),
     path('main',main,name='main'),
     path('forms/<str:page_name>',forms,name='forms'),
     path('edit/<page_name>',edit,name='edit'),
     path('deletepage/<page_name>',deletepage,name='deletepage'),
     path('custom_templates/<l_name>',custom_template,name='custom_template'),
     path('elementcreate/<l_name>',elementcreate,name='elementcreate'),
     path('newlayout/<l_name>',newlayout,name='newlayout'),
     path('testing',testing,name='testing'),
     path('Template1',Template1,name='Template1'),
     path('Template2',Template2,name='Template2'),
     path('Template3',Template3,name='Template3'),
     path('Template4',Template4,name='Template4'),
     path('test/<page_name>',test,name='test'),
     path('deletelayout/<str:id>/<str:layout>/<str:page_name>',deletelayout,name='deletelayout')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

