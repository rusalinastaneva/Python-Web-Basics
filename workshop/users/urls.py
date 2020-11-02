from django.urls import path

from users.views import login, register, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    # path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
]
