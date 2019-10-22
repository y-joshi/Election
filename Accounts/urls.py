from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name = 'login'),
    path('register',views.register,name = 'register'),
    path('home',views.home,name = 'home'),
    path('Result',views.Result,name = 'Result'),
    path('OTPverify',views.OTPverify,name = 'OTPverify'),
    path('FaceRecognition',views.FaceRecognition,name = 'FaceRecognition')
]