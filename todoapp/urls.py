from django.urls import path
from .views import listfunc, detailfunc, createfunc, deletefunc, \
updatefunc, signupfunc, loginfunc, logoutfunc


urlpatterns = [
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('create/', createfunc, name='create'),
    path('delete/<int:pk>', deletefunc, name='delete'),
    path('update/<int:pk>', updatefunc, name='update'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    # path('profile/<int:pk>/', Profile.as_view(), name='profile')
]
