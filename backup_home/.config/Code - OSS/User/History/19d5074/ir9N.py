from rest_framework import serializers




from students.models import Student,Student_Confirmation
from instructors.models import Instructor,Instructor_Confirmation
from groups.models0 import Payment,Package,Attendance
from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


from zoneinfo import ZoneInfo






class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        mexico_tz=ZoneInfo('America/Mexico_City')
        value=value.astimezone(mexico_tz)
        formatted_datetime = value.strftime('%Y-%m-%dT%H:%M')

        return formatted_datetime







class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


        


class AdminMakerInstructor0(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields='__all__'



class AdminMakerInstructorConfirmation(serializers.ModelSerializer):
    instructor=AdminMakerInstructor0(read_only=True)
    datetime=CustomDateTimeField()

    class Meta:
        model=Instructor_Confirmation
        fields='__all__'


        


class AdminMakerStudent0(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class AdminMakerStudentConfirmation(serializers.ModelSerializer):
    student=AdminMakerStudent0(read_only=True)
    datetime=CustomDateTimeField()

    class Meta:
        model=Student_Confirmation
        fields='__all__'



class AdminMakerGroup(serializers.ModelSerializer):
    instructor=AdminMakerInstructor0(many=True,read_only=True)
    student=AdminMakerStudent0(many=True,read_only=True)
    class Meta:
        model=Group
        fields='__all__'

class AdminMakerAttendance(serializers.ModelSerializer):
    # instructor_confirmation=AdminMakerInstructorConfirmation(many=True,read_only=True)
    # student_confirmation=AdminMakerStudentConfirmation(many=True,read_only=True)
    # group=AdminMakerGroup()
    datetime=CustomDateTimeField()
    class Meta:
        model=Attendance
        fields='__all__'
        depth=4


class AdminMakerPackage(serializers.ModelSerializer):
    attendance=AdminMakerAttendance(many=True,read_only=True)
    datetime=CustomDateTimeField()

    class Meta:
        model=Package
        fields='__all__'
        # depth = 1


class AdminMakerPayment(serializers.ModelSerializer):
    package=AdminMakerPackage(many=True,read_only=True)
    datetime=CustomDateTimeField()

    class Meta:
        model=Payment
        fields='__all__'
        # depth = 1


class AdminMakerPaymentPlain(serializers.ModelSerializer):
    datetime=CustomDateTimeField()

    class Meta:
        model=Payment
        fields='__all__'
        depth=1







class AdminMakerStudent(serializers.ModelSerializer):
    last_payments=serializers.SerializerMethodField()
    groups=serializers.SerializerMethodField()
    user=UserSerializer()
    class Meta:
        model=Student
        fields='__all__'


    def get_groups(self,student):
        groups=Group.objects.filter(student=student)
        serializer=AdminMakerGroup(groups,many=True).data
        return serializer

    def get_last_payments(self,student):
        payments = Payment.objects.filter(package__student=student)
        payments=payments[:3]
        serializer = AdminMakerPaymentPlain(payments, many=True).data
        return serializer





