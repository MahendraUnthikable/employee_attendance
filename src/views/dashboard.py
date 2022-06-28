import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.serializers import registratoinSerializer,ChangePasswordSerializer
from ..models.models import employeeRegistratoin
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.shortcuts import render,redirect


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class EmployeeDashboard(APIView):
    def dashboard(request):
        
        '''
        Summary of all apps - display here with charts etc.
        eg.lEAVE - PENDING|APPROVED|RECENT|REJECTED - TOTAL THIS MONTH or NEXT MONTH
        EMPLOYEE - TOTAL | GENDER 
        CHART - AVERAGE EMPLOYEE AGES
        '''
        dataset = dict()
        user = request.user

        if not request.user.is_authenticated:
            return redirect('accounts:login')

        employees = employeeRegistratoin.objects.all()
        dataset['employees'] = employees

        return render(request,'dashboard/dashboard_index.html',dataset)