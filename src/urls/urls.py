from django.urls import path
from src.views.views import employeeProfile,register, Logout, employeeLogin


urlpatterns =[
    path('v1/employee/registration',register.as_view()),
    path('v1/employee/allprofile', employeeProfile.as_view()),
    path('v1/employee/profile/<int:id>', employeeProfile.as_view()),
    path('v1/employee/login', employeeLogin.as_view()),
    path('v1/employee/logout', Logout.as_view())

]