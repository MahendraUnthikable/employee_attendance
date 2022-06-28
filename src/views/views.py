import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.serializers import registratoinSerializer
from ..models.models import employeeRegistratoin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class register(APIView):
    def post(self, request):
        serializer=registratoinSerializer(data=request.data)
        if serializer.is_valid():
            useremail=request.data['email']
            userphone=request.data['phone']
            logger.debug("This logs a debug message.")
            if employeeRegistratoin.objects.filter(email=useremail).first():
                return Response({"status":"email already exists!!"})
            elif employeeRegistratoin.objects.filter(phone=userphone).first():
                return Response({"status":"phone number already exists!!"})  
            serializer.save()    
            user=employeeRegistratoin.objects.filter(email=useremail).first()
            refresh = RefreshToken.for_user(user)
            request.session['refresh-token'] = str(refresh)
            return Response({"status":"sucess",
                             "data":serializer.data,
                             'Token':str(refresh),
                           }, 
                           status=status.HTTP_200_OK)
        else:
            return Response({"status":"error ", "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)    



class employeeProfile(APIView):
    authentication_classes=[[SessionAuthentication, BasicAuthentication]]
    permission_classes=[IsAuthenticated]

    def get(self,request,id=None):
        if id:
            item = employeeRegistratoin.objects.get(id=id)
            serializer = registratoinSerializer(item)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        
        item=employeeRegistratoin.objects.all()
        serializer=registratoinSerializer(item, many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)

    def patch(self,request, id=None):
        if id:
            item = employeeRegistratoin.objects.get(id=id)
            serializer = registratoinSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
               serializer.save()
               return Response({"status":"sucess","data":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"error ", "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,id=None):
        if id:
            item = employeeRegistratoin.objects.get(id=id)
            serializer = registratoinSerializer(item,data=request.data)            
            if serializer.is_valid():
               serializer.save()
               return Response({"status":"sucess","data":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"error ", "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id=None):            
        if id:
            employeeRegistratoin.objects.filter(id=id).delete()
            return Response({"status":"success","data":"Item Deleted"})


class employeeLogin(APIView):
    def post(self,request):
        serializer = registratoinSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data['email']
            password = request.data['password']
            if not email:
              return 'Missing email', 400
            if not password:
              return 'Missing password', 400  
            usercreds=employeeRegistratoin.objects.filter(Q(email=email),Q(password=password)).first()
            if usercreds is not None:
                return Response({"status":"Login sucessfully","data":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Login Error","msg":"Access denied: wrong username or password."})


class Logout(APIView):
    def post(self, request):
        try:
            del request.session['refresh-token']
            res =  "Logout successfull"  
            return Response(res,status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)




        
            


