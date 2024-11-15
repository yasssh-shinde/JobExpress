from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_register/', views.user_register, name='user_register'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('post_job/', views.post_job, name='post_job'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('all_users/', views.all_users, name='all_users'),
    path('about_contact/', views.about_contact, name='about_contact'),
    path('logout/', logout_view, name='logout_view'),
   #  path('login/', views.login_view, name='login'),
     path('login/', views.user_login, name='login'),

     path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('login/', views.admin_login, name='login'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),

]
