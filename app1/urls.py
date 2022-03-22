from django.urls import path
from app1 import views


urlpatterns = [
    path('',views.form),
    path('login/',views.login),
    path('signup/',views.signup),
    path('info/',views.info),
    path('contact/',views.contact),
    path('<int:id>/',views.edit),
    path('delete/<int:id>/',views.delete),
    path('logout/',views.logOut)
]
