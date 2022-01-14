from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.myfunctionabout,name="about"),
    path('contact',views.myfunctioncontact,name="contact"),
    path('login',views.myfunctionlogin,name="login"),
    path('register',views.myfunctionregister,name="register"),
    path('Success',views.myfunctionsuccess,name="success"),
    path('Logout',views.logout,name="logout"),
    path('edit',views.edit,name="edit"),
    path('editnew',views.editnew,name="editnew"),
    path('delete',views.delete,name="delete")
   
]