from rest_framework import serializers
from .models import Student_Details,Marklist


class StudentSer(serializers.ModelSerializer):
    class Meta:
        model=Student_Details
        fields='__all__'
    

class MarkSer(serializers.ModelSerializer):
    studentdetails=StudentSer(many=False,read_only=True)
    class Meta:
        model=Marklist
        fields=['studentdetails','Semester','Mark']
    
    def create(self, validated_data):
        detail=self.context.get("studentdetails")
        return Marklist.objects.create(studentdetails=detail,**validated_data)
 