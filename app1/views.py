from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import action 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.



class StudentView(ModelViewSet):
    serializer_class=StudentSer
    model=Student_Details
    queryset=Student_Details.objects.all()

    @action(detail=True,methods=['get'])
    def get_details(self,request,*args,**kwrgs):
        id=kwrgs.get('pk')
        details=Student_Details.objects.get(id=id)
        marksheet=Marklist.objects.filter(studentdetails=details)
        ser=MarkSer(marksheet,many=True)
        return Response(data=ser.data)
    
    @action(detail=True,methods=['post'])
    def add_details(self,request,*args,**kwrgs):
        id=kwrgs.get('pk')
        details=Student_Details.objects.get(id=id)
        ser=MarkSer(data=request.data,context={"studentdetails":details})
        if ser.is_valid():
            ser.save()
            return Response({"msg":"ok"})

        else:
            return Response({"msg":"error"})
        


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id,"username":token.user.username,})
