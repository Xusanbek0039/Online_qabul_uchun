from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
    path('full-stack_python/',FullPython.as_view(), name = 'python_course'),
    path('django/',DjangoView.as_view(), name = 'django'),
    path('flask/',FlaskView.as_view(),name='flask'),

    ]