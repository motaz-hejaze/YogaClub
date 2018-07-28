from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home , name='home' ),
    path('about', views.about , name='about'),
    path('classes', views.classes , name='classes'),
    path('instructors', views.instructors , name='instructors'),
    path('contact', views.contact , name='contact'),
    path('blog/', views.blog , name='blog'),
    path('post/<int:id>', views.post , name='post'),

]
