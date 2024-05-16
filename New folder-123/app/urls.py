
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.application, name='application'),
#     path('success/', views.success, name='success'),
#     path('view-users/', views.view_users, name='view_users'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.application, name='application'),  # URL for submitting new application
    path('success/', views.success, name='success'),  # URL for success page
    path('view_users/', views.view_users, name='view_users'),  # URL for viewing all users
    path('edit_user/<int:id>/', views.edit_user, name='edit_user'),  # URL for editing a user
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),  # URL for deleting a user
]

# path('edit_user/<int:id>/', views.edit_user, name='edit_user')