from django.http import HttpResponse, JsonResponse

from decimal import Decimal
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.decorators import action
from django.db.models import Q


from students.models import Student


from django.apps import apps

from operation.serializers import GroupSerializer,InstructorSerializer,StudentSerializer,PaymentSerializer,PackageSerializer,InvoiceSerializer,AttendanceSerializer,AttendanceUISerializer, Instructor_ConfirmationSerializer,Student_ConfirmationSerializer,IAMaterialSerializer

from students.serializers import StudentPaymentSerializer, StudentWithGroupsSerializer,InstructorSerializer0,StudentSerializer0,EvaluationSerializer,MaterialSerializer

from instructors.serializers import InstructorWithGroupsSerializer,InstructorAttendancePaySheetSerializer

from instructors.models import Instructor

from students.serializers import *

from operation.adminserializers import AdminStudentSerializer,AdminStudentPlainSerializer,AdminAttendanceSerializer,AdminInstructorConfirmationSerializer,AdminStudentConfirmationSerializer

from operation.adminmakerserializers import AdminMakerStudent,AdminMakerInstructor0,AdminMakerPayment,AdminMakerPaymentPlain,AdminMakerPackage,AdminMakerAttendance,AdminMakerInstructorConfirmation,AdminMakerStudentConfirmation


import json



from django.contrib.auth import get_user_model
User = get_user_model()

from groups.models0 import Attendance,Payment


from django.utils import timezone
from zoneinfo import ZoneInfo
from datetime import datetime, time
import calendar




import random


django_serializers={
#################ADMINDASHBOARDSERIALIZERS#################
    'Admin-Student-Serializer':AdminStudentSerializer,
    'Admin-Student-Plain-Serializer':AdminStudentPlainSerializer,
    'Admin-Attendance-Serializer':AdminAttendanceSerializer,
    'Admin-Instructor-Confirmation-Serializer':AdminInstructorConfirmationSerializer,
    'Admin-Student-Confirmation-Serializer':AdminStudentConfirmationSerializer,





    

#################USERSERIALIZERS#################
    'User':UserSerializer,

#################STUDENTSERIALIZERS#################
    'Student-With-Groups':StudentWithGroupsSerializer,
    'Studentpaymentserializer':StudentPaymentSerializer,
    'Evaluation':EvaluationSerializer,
    'Review_Topics': IAMaterialSerializer,
    'Learned_Material':IAMaterialSerializer,
    'Review_Material':IAMaterialSerializer,
    'Core_Material':IAMaterialSerializer,

#################INSTRUCTORSERIALIZERS#################
    'Instructor-With-Groups':InstructorWithGroupsSerializer,
    'Instructor-Attendance-Pay-Sheet-Serializer':InstructorAttendancePaySheetSerializer,


#################DATABASE SERIALIZERS#################

    'Group':GroupSerializer,
    'Iamaterial':IAMaterialSerializer,
    'Instructor':InstructorSerializer,
    'Student':StudentSerializer,
    'Payment':PaymentSerializer,
    'Invoice':InvoiceSerializer,
    'Package':PackageSerializer,
    'Attendance':AttendanceSerializer,


    'Attendance-UI-Serializer':AttendanceUISerializer,

    'Instructor_Confirmation':Instructor_ConfirmationSerializer,
    'Instructor_Confirmation_Set':Instructor_ConfirmationSerializer,

    'Student_Confirmation':Student_ConfirmationSerializer,



################# ADMIN MAKER SERIALIZERS #################

    'Admin-Maker-Student':AdminMakerStudent,
    'Admin-Maker-Instructor':AdminMakerInstructor0,
    'Admin-Maker-Payment':AdminMakerPayment,
    'Admin-Maker-Payment-Plain':AdminMakerPaymentPlain,
    'Admin-Maker-Package':AdminMakerPackage,
    'Admin-Maker-Attendance':AdminMakerAttendance,
    'Admin-Maker-Instructor-Confirmation':AdminMakerInstructorConfirmation,
    'Admin-Maker-Student-Confirmation':AdminMakerStudentConfirmation,
}




def json_payments(student):
    payments=Payment.objects.filter(package__student=student).order_by('-datetime').distinct('datetime')


    # payments=list(set(payments))


    serializer=get_serializer('Admin-Maker-Payment')
    payments=serializer(payments,many=True).data

    return payments



class AdminMaker(viewsets.GenericViewSet):
    queryset=None
    serializer_class=None
    permission_classes=(permissions.IsAuthenticated,)

    @action(detail=False,methods=['post'])
    def get_students(self,request,*args,**kwargs):
        active_students=Student.objects.filter(user__is_active=True).order_by('user__first_name')
        # inactive_students=Student.objects.filter(user__is_active=False).order_by('user__first_name')


        serializer=get_serializer('Admin-Maker-Student')
        active_students=serializer(active_students,many=True).data
        # inactive_students=serializer(inactive_students,many=True).data
        

        data={
            'active':active_students,
            'inactive':None,
        }

        return JsonResponse(data,safe=False)
    

    @action(detail=False,methods=['post'])
    def get_instructors(self,request,*args,**kwargs):
        instructors=Instructor.objects.filter(user__is_active=True).order_by('user__first_name')

        serializer=get_serializer('Admin-Maker-Instructor')

        instructors=serializer(instructors,many=True).data

        return JsonResponse(instructors,safe=False)

        



    @action(detail=False,methods=['post'])
    def all_into_one(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')


        student=Student.objects.get(pk=student_id)




        attendances=Attendance.objects.filter(student_confirmation__student__in=[student])
        for attendance in attendances:
            student_packages=attendance.package_set.filter(student=student)
            attendance.package_set.remove(*student_packages)

        new_payment=Payment.objects.create()
        new_package=new_payment.package.create(student=student)

        new_package.attendance.add(*attendances)



        payments=Payment.objects.filter(package__student=student)
        for payment in payments:
            if payment.package.filter(pk=new_package.pk).exists():
                pass
            else:
                for package in payment.package.all():
                    package.delete()
                payment.delete()



        payments=json_payments(student)


        return JsonResponse(payments,safe=False)
    


    @action(detail=False,methods=['post'])
    def fix_in_packages(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)


        mexico_tz=ZoneInfo('America/Mexico_City')



        payments=Payment.objects.filter(package__student=student)

        for payment in payments:
            for package in payment.package.all():
                package.attendance.clear()
                package.taken_hours=0
                package.save()

 

        attendances=Attendance.objects.filter(student_confirmation__student__in=[student])

        class obj:
            pass


        i=0
        for attendance in attendances:
            payment=payments[i]
            package=payment.package.last()

            if package.taken_hours<package.package_hours:
                package.attendance.add(attendance)
                package.taken_hours+=attendance.duration
                package.save()
            else:
                i+=1
                if i>=len(payments):

                    attendance_datetime=attendance.datetime
                    payment=Payment.objects.create(
                        datetime=datetime(attendance_datetime.year,attendance_datetime.month,attendance_datetime.day,0,0).astimezone(mexico_tz),
                        amount=student.package_cost,
                        method=student.payment_method,
                        paid=True
                    )

                    package=payment.package.create(
                        student=student,
                        package_hours=student.package_hours
                    
                    )
                    package.attendance.add(attendance)
                    package.taken_hours+=attendance.duration
                    package.save()

                    payments.append(payment)
        payments=json_payments(student)


        return JsonResponse(payments,safe=False)
    


                
            
        





    @action(detail=False,methods=['post'])
    def make_all_monthly(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)


        mexico_tz=ZoneInfo('America/Mexico_City')



        payments=Payment.objects.filter(package__student=student).order_by('datetime')

        for payment in payments:
            for package in payment.package.all():
                package.attendance.clear()

 

        attendances=Attendance.objects.filter(student_confirmation__student__in=[student])

        class obj:
            pass

        maker=obj()
        maker.attendances=attendances
        maker.months={}

        i=0
        for attendance in maker.attendances:
            attendance_datetime=attendance.datetime.astimezone(mexico_tz)
            month=attendance_datetime.month
            year=attendance_datetime.year
            category=f'{year}-{month}'
            if category in maker.months:
                pass
            else:
                if i<len(payments):
                    payment=payments[i]
                else:
                    payment=Payment.objects.create(
                        datetime=datetime(year,month,1,0,0).astimezone(mexico_tz),
                        amount=student.package_cost,
                        method=student.payment_method,    
                        paid=True

                    )

                    payment.package.create(
                        student=student,
                        package_hours=student.package_hours
                        
                    )


                for package in payment.package.all():
                    package.datetime=payment.datetime
                    package.save()

                maker.months[category]=obj()
                maker.months[category].payment=payment
                maker.months[category].attendances=[]


                i+=1
            if attendance not in maker.months[category].attendances:
                maker.months[category].attendances.append(attendance)

 
        for month in maker.months.values():
            month.payment.package.last().attendance.add(*month.attendances)
            month.payment.package.last().taken_hours=month.payment.package.last().package_hours

            month.payment.package.last().save()



        payments=json_payments(student)
        return JsonResponse(payments,safe=False)






    @action(detail=False,methods=['post'])
    def make_monthly(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')
        query_datetime=data.get('query_datetime')

        student=Student.objects.get(pk=student_id)



        mexico_tz=ZoneInfo('America/Mexico_City')
        query_datetime=datetime.fromisoformat(query_datetime).astimezone(mexico_tz)

        query_datetime=datetime(query_datetime.year,query_datetime.month,query_datetime.day,0,0,tzinfo=mexico_tz)

        payments=Payment.objects.filter(package__student=student,datetime__gte=query_datetime).order_by('datetime')

        for payment in payments:
            for package in payment.package.all():
                package.attendance.clear()

 

        attendances=Attendance.objects.filter(student_confirmation__student__in=[student],datetime__gte=query_datetime)

        class obj:
            pass

        maker=obj()
        maker.attendances=attendances
        maker.months={}

        i=0
        for attendance in maker.attendances:
            month=attendance.datetime.month
            year=attendance.datetime.year
            category=f'{year}-{month}'
            if category in maker.months:
                pass
            else:
                if i<len(payments):
                    payment=payments[i]
                else:
                    payment=Payment.objects.create(
                        datetime=datetime(year,month,1,0,0,tzinfo=mexico_tz),
                        amount=student.package_cost,
                        method=student.payment_method,    
                        paid=True
                    )

                    payment.package.create(
                        student=student,
                        package_hours=student.package_hours
                        
                    )


                for package in payment.package.all():
                    package.datetime=payment.datetime
                    package.save()

                maker.months[category]=obj()
                maker.months[category].payment=payment
                maker.months[category].attendances=[]


                i+=1
            if attendance not in maker.months[category].attendances:
                maker.months[category].attendances.append(attendance)

 
        for month in maker.months.values():
            month.payment.package.last().attendance.add(*month.attendances)
            month.payment.package.last().taken_hours=month.payment.package.last().package_hours
            month.payment.package.last().save()



        payments=json_payments(student)
        return JsonResponse(payments,safe=False)



    @action(detail=False,methods=['post'])
    def default_datetimes(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')
        payment_id=data.get('payment_id')

        student=Student.objects.get(pk=student_id)
        mexico_tz=ZoneInfo('America/Mexico_City')

        payment=Payment.objects.get(pk=payment_id)
        payment.datetime=datetime(payment.datetime.year,payment.datetime.month,1,0,0,tzinfo=mexico_tz)
        payment.save()
        for package in payment.package.all():
            package.datetime=payment.datetime

            if package.attendance.exists():
                package.datetime=package.attendance.last().datetime
                payment.datetime=package.attendance.last().datetime
            payment.save()
            package.save()
        payments=json_payments(student)
        return JsonResponse(payments,safe=False)



    @action(detail=False,methods=['post'])
    def delete_duplicate_datetimes(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')
        payment_id=data.get('payment_id')

        student=Student.objects.get(pk=student_id)
        payment=Payment.objects.get(pk=payment_id)

        mexico_tz=ZoneInfo('America/Mexico_City')


        class dates_obj:
            pass
            
        for package in payment.package.all():
            dates=dates_obj()
            dates.all=[]

            for attendance in package.attendance.all():
                attendance_datetime=attendance.datetime.astimezone(mexico_tz)
                category_string=f'{attendance_datetime.year} {attendance_datetime.month} {attendance_datetime.day}'
                if category_string in dates.all:
                    attendance.delete()
                else:
                    dates.all.append(category_string)


        payments=json_payments(student)
        return JsonResponse(payments,safe=False)

        






    @action(detail=False,methods=['post'])
    def get_payments(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)

        payments=json_payments(student)


        return JsonResponse(payments,safe=False)

    @action(detail=False,methods=['post'])
    def update_payment(self,request,*args,**kwargs):
        data=request.data
        json_payment=data.get('payment')

        payment=Payment.objects.get(pk=json_payment.get('id'))


        serializer=get_serializer('Admin-Maker-Payment')
        payment_serializer=serializer(instance=payment,data=json_payment,partial=True)
        if payment_serializer.is_valid():
            print('#'*40,'DIS IS VALIIIIIID','#'*40)
            payment=payment_serializer.save()
        payment=serializer(payment).data
        

        return JsonResponse(payment,safe=False)

    @action(detail=False,methods=['post'])
    def update_package(self,request,*args,**kwargs):
        data=request.data
        json_package=data.get('package')

        package=Package.objects.get(pk=json_package.get('id'))


        serializer=get_serializer('Admin-Maker-Package')
        package_serializer=serializer(instance=package,data=json_package,partial=True)
        if package_serializer.is_valid():
            print('#'*40,'DIS IS VALIIIIIID','#'*40)
            package=package_serializer.save()
        package=serializer(package).data
        
        return JsonResponse(package,safe=False)


    @action(detail=False,methods=['post'])
    def update_attendance(self,request,*args,**kwargs):
        data=request.data
        json_attendance=data.get('attendance')

        attendance=Attendance.objects.get(pk=json_attendance.get('id'))


        serializer=get_serializer('Admin-Maker-Attendance')
        attendance_serializer=serializer(instance=attendance,data=json_attendance,partial=True)
        if attendance_serializer.is_valid():
            print('#'*40,'DIS IS VALIIIIIID','#'*40)
            attendance=attendance_serializer.save()
        attendance=serializer(attendance).data
        
        return JsonResponse(attendance,safe=False)

    @action(detail=False,methods=['post'])
    def update_instructor_confirmation(sefl,request,*args,**kwargs):
        data=request.data
        json_confirmation=data.get('confirmation')

        confirmation=Instructor_Confirmation.objects.get(pk=json_confirmation.get('id'))


        serializer=get_serializer('Admin-Maker-Instructor-Confirmation')
        confirmation_serializer=serializer(instance=confirmation,data=json_confirmation,partial=True)
        if confirmation_serializer.is_valid():
            print('#'*40,'DIS IS VALIIIIIID','#'*40)
            confirmation=confirmation_serializer.save()
        confirmation=serializer(confirmation).data
        
        return JsonResponse(confirmation,safe=False)


    @action(detail=False,methods=['post'])
    def update_student_confirmation(sefl,request,*args,**kwargs):
        data=request.data
        json_confirmation=data.get('confirmation')

        confirmation=Student_Confirmation.objects.get(pk=json_confirmation.get('id'))


        serializer=get_serializer('Admin-Maker-Student-Confirmation')
        confirmation_serializer=serializer(instance=confirmation,data=json_confirmation,partial=True)
        if confirmation_serializer.is_valid():
            print('#'*40,'DIS IS VALIIIIIID','#'*40)
            confirmation=confirmation_serializer.save()
        confirmation=serializer(confirmation).data
        
        return JsonResponse(confirmation,safe=False)

    @action(detail=False,methods=['post'])
    def create_payment(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')    

        student=Student.objects.get(pk=student_id)
        package=student.package_set.create(student=student,package_hours=student.package_hours)
        package.payment_set.create(method=student.payment_method,amount=student.package_cost)

        payments=json_payments(student)


        return JsonResponse(payments,safe=False)

    @action(detail=False,methods=['post'])
    def delete_payment(self,request,*args,**kwargs):
        data=request.data
        payment_id=data.get('payment_id')
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)
        
        payment=Payment.objects.get(pk=payment_id)
        for package in payment.package.all():
            for attendance in package.attendance.all():
                for student_confirmation in attendance.student_confirmation.all():
                    student_confirmation.delete()
                for instructor_confirmation in attendance.instructor_confirmation.all():
                    instructor_confirmation.delete()
                attendance.delete()
            package.delete()
        payment.delete()

        payments=json_payments(student)


        return JsonResponse(payments,safe=False)
    


    @action(detail=False,methods=['post'])
    def create_package(self,request,*args,**kwargs):
        data=request.data
        payment_id=data.get('payment_id')
        student_id=data.get('student_id')    

        student=Student.objects.get(pk=student_id)

        payment=Payment.objects.get(pk=payment_id)

        payment.package.create(student=student,package_hours=student.package_hours)

        payments=json_payments(student)


        return JsonResponse(payments,safe=False)
    
    @action(detail=False,methods=['post'])
    def delete_package(self,request,*args,**kwargs):
        data=request.data
        package_id=data.get('package_id')
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)
        
        package=Package.objects.get(pk=package_id)
        for attendance in package.attendance.all():
            for student_confirmation in attendance.student_confirmation.all():
                student_confirmation.delete()
            for instructor_confirmation in attendance.instructor_confirmation.all():
                instructor_confirmation.delete()
            attendance.delete()
        package.delete()

        payments=json_payments(student)


        return JsonResponse(payments,safe=False)


    @action(detail=False,methods=['post'])
    def create_attendance(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')
        package_id=data.get('package_id')

        student=Student.objects.get(pk=student_id)
        group=student.group_set.last()

        package=Package.objects.get(pk=package_id)

        package.attendance.create(group=group)

        payments=json_payments(student)

        return JsonResponse(payments,safe=False)
    

    @action(detail=False,methods=['post'])
    def delete_attendance(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')
        attendance_id=data.get('attendance_id')

        student=Student.objects.get(pk=student_id)
        attendance=Attendance.objects.get(pk=attendance_id)

        for student_confirmation in attendance.student_confirmation.all():
            student_confirmation.delete()
        for instructor_confirmation in attendance.instructor_confirmation.all():
            instructor_confirmation.delete()
        attendance.delete()

        payments=json_payments(student)

        return JsonResponse(payments,safe=False)
    


    @action(detail=False,methods=['post'])
    def create_instructor_confirmation(self,request,*args,**kwargs):
        data=request.data
        attendance_id=data.get('attendance_id')
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)
        group=student.group_set.last()
        
        attendance=Attendance.objects.get(pk=attendance_id)

        for instructor in group.instructor.all():
            attendance.instructor_confirmation.create(instructor=instructor)

        payments=json_payments(student)

        return JsonResponse(payments,safe=False)

    @action(detail=False,methods=['post'])
    def delete_instructor_confirmation(self,request,*args,**kwargs):
        data=request.data
        confirmation_id=data.get('confirmation_id')
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)

        confirmation=Instructor_Confirmation.objects.get(pk=confirmation_id)
        confirmation.delete()

        payments=json_payments(student)

        return JsonResponse(payments,safe=False)
    

    @action(detail=False,methods=['post'])
    def create_student_confirmation(self,request,*args,**kwargs):
        data=request.data
        attendance_id=data.get('attendance_id')
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)
        group=student.group_set.last()
        
        attendance=Attendance.objects.get(pk=attendance_id)

        for student0 in group.student.all():
            attendance.student_confirmation.create(student=student0)

        payments=json_payments(student)

        return JsonResponse(payments,safe=False)

    @action(detail=False,methods=['post'])
    def delete_student_confirmation(self,request,*args,**kwargs):
        data=request.data
        confirmation_id=data.get('confirmation_id')
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)

        confirmation=Student_Confirmation.objects.get(pk=confirmation_id)
        confirmation.delete()

        payments=json_payments(student)

        return JsonResponse(payments,safe=False)

    @action(detail=False,methods=['post'])
    def update_attendance_package(self,request,*args,**kwargs):
        data=request.data
        student_id=data.get('student_id')
        attendance_id=data.get('attendance_id')
        package_id=data.get('package_id')

        student=Student.objects.get(pk=student_id)


        attendance=Attendance.objects.get(pk=attendance_id)

        current_student_packages=None

        if attendance.package_set.filter(student=student):
            current_student_packages=attendance.package_set.filter(student=student)
        
        if current_student_packages:
            attendance.package_set.remove(*current_student_packages)

        package=Package.objects.get(pk=package_id)

        attendance.package_set.add(package)

        payments=json_payments(student)

        return JsonResponse(payments,safe=False)







class DashboardViewset(viewsets.GenericViewSet):
    queryset=None
    serializer_class=None
    permission_classes=(permissions.IsAuthenticated,)

    @action(detail=False,methods=['post'])
    def filtered_bad_attendances(self,request,*args,**kwargs):
        data=request.data
        initial_datetime=data.get('initial_datetime')
        final_datetime=data.get('final_datetime')

        mexico_tz=ZoneInfo('America/Mexico_City')
        initial_datetime=datetime.fromisoformat(initial_datetime).astimezone(mexico_tz)
        final_datetime=datetime.fromisoformat(final_datetime).astimezone(mexico_tz)


        year=timezone.now().year
        month=timezone.now().month
        month_attendances=Attendance.objects.filter(Q(datetime__gte=initial_datetime),Q(datetime__lte=final_datetime))
        bad_attendances=[]
        for attendance in month_attendances:
            # if not attendance.package_set.exists():
            #     continue
            confirmation_missing=False
            confirmation_mismatch=False
            if not attendance.instructor_confirmation.exists():
                confirmation_missing=True
                

            if not attendance.student_confirmation.exists():
                confirmation_missing=True


            if not confirmation_missing:
                instructor_confirmation=attendance.instructor_confirmation.last().confirmation
                student_confirmations=[]

                if attendance.group!=None:
                    for student in attendance.group.student.all():
                        if attendance.student_confirmation.filter(student=student).exists():
                            student_confirmation=attendance.student_confirmation.filter(student=student).last().confirmation
                            student_confirmations.append(student_confirmation)

                    for student_confirmation in student_confirmations:
                        if student_confirmation != instructor_confirmation:
                            confirmation_mismatch=True


            if confirmation_missing or confirmation_mismatch:
                bad_attendances.append(attendance)
        
        serializer=get_serializer('Admin-Attendance-Serializer')
        bad_attendances=serializer(bad_attendances,many=True).data

        return JsonResponse(bad_attendances,safe=False)








    @action(detail=False,methods=['post'])
    def create_instructor_confirmation(self,request,*args,**kwargs):
        data=request.data
        attendance_id=data.get('attendance_id')

        instructor_id=data.get('instructor_id')
        instructor=Instructor.objects.get(pk=instructor_id)

        student_id=data.get('student_id')
        student=Student.objects.get(pk=student_id)
        group=student.group_set.last()



        attendance=Attendance.objects.get(pk=attendance_id)
        for instructor in group.instructor.all():
            if not attendance.instructor_confirmation.filter(instructor).exists():
                attendance.instructor_confirmation.create(instructor=instructor)
        attendance.save()

        serializer=get_serializer('Admin-Student-Serializer')

        student=serializer(student).data



        return JsonResponse(student,safe=False)

    @action(detail=False,methods=['post'])
    def create_student_confirmation(self,request,*args,**kwargs):
        data=request.data
        attendance_id=data.get('attendance_id')

        student_id=data.get('student_id')
        student=Student.objects.get(pk=student_id)


        group=student.group_set.last()

        attendance=Attendance.objects.get(pk=attendance_id)
        for student in group.student.all():
            if not attendance.student_confirmation.filter(student=student).exists():
                attendance.student_confirmation.create(student=student)
        attendance.save()

        serializer=get_serializer('Admin-Student-Serializer')

        student=serializer(student).data



        return JsonResponse(student,safe=False)




    @action(detail=False,methods=['post'])
    def move_attendance(self,request,*args,**kwargs):
        data=request.data
        package_id=data.get('package_id')
        attendance_id=data.get('attendance_id')
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)

        attendance=Attendance.objects.get(pk=attendance_id)

        student_packages=attendance.package_set.filter(student=student)
        attendance.package_set.remove(*student_packages)
        attendance.save()

        package=Package.objects.get(pk=package_id)
        attendance.package_set.set([package])
        attendance.save()

        serializer=get_serializer('Admin-Student-Serializer')
        student=serializer(student).data

        return JsonResponse(student,safe=False)


    @action(detail=False,methods=['post'])
    def update_attendance(self,request,*args,**kwargs):
        data=request.data
        json_attendance=data.get('attendance')
        attendance=Attendance.objects.get(pk=json_attendance.get('id'))

        mexico_tz=ZoneInfo('America/Mexico_City')

        attendance_date=datetime.fromisoformat(json_attendance.get('datetime')).astimezone(mexico_tz)


        attendance.datetime=attendance_date
        attendance.duration=Decimal(json_attendance.get('duration'))

        attendance.save()

        serializer=get_serializer('Admin-Attendance-Serializer')
        attendance=serializer(attendance).data

        
        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)

        serializer=get_serializer('Admin-Student-Serializer')

        student=serializer(student).data



        return JsonResponse(student,safe=False)
    
    @action(detail=False,methods=['post'])
    def update_confirmation(self,request,*args,**kwargs):
        data=request.data
        json_confirmation=data.get('confirmation')
        endpoint=json_confirmation.get('endpoint')

        if endpoint=='Instructor_Confirmation':
            confirmation=Instructor_Confirmation.objects.get(pk=json_confirmation.get('id'))

            serializer=get_serializer('Admin-Instructor-Confirmation-Serializer')
        else:
            confirmation=Student_Confirmation.objects.get(pk=json_confirmation.get('id'))
            serializer=get_serializer('Admin-Student-Confirmation-Serializer')


        confirmation.confirmation=json_confirmation.get('confirmation')
        confirmation.save()

        student_id=data.get('student_id')

        student=Student.objects.get(pk=student_id)

        serializer=get_serializer('Admin-Student-Serializer')

        student=serializer(student).data

        return JsonResponse(student,safe=False)


        
    



    @action(detail=False,methods=['post'])
    def bad_attendances(self,request,*args,**kwargs):
        mexico_tz=ZoneInfo('America/Mexico_City')

        year=timezone.now().astimezone(mexico_tz).year
        month=timezone.now().astimezone(mexico_tz).month
        month_attendances=Attendance.objects.filter(Q(datetime__month=month),Q(datetime__year=year))

        bad_attendances=get_bad_attendances(month_attendances)


        return JsonResponse(bad_attendances,safe=False)



    @action(detail=False,methods=['post'])
    def get_objects(self,request,*args,**kwargs):
        data=request.data
        objects=data.get('objects')


        students=User.objects.filter(is_active=True,role='Student')
        students=students.count()

        instructors=User.objects.filter(role='Instructor',is_active=True)
        instructors=instructors.count()

        groups=Group.objects.filter(is_active=True)

        groups=groups.count()

        mexico_tz=ZoneInfo('America/Mexico_City')

        year=timezone.now().astimezone(mexico_tz).year
        month=timezone.now().astimezone(mexico_tz).month
        month_attendances=Attendance.objects.filter(Q(datetime__month=month),Q(datetime__year=year))


        bad_attendances=get_bad_attendances(month_attendances)

        bad_attendances=len(bad_attendances)



        c={
            'students':students,
            'instructors':instructors,
            'groups':groups,
            'bad_attendances':bad_attendances,
            }


        return JsonResponse(c,safe=False)
    

    @action(detail=False,methods=['post'])
    def collection(self,request,*args,**kwargs):




        active_students=Student.objects.filter(user__is_active=True)
        final_active_students=[]
        for student in active_students:
            packages=student.package_set.all()
            for package in packages:
                payments=package.payment_set.filter(paid=False).exists()
                if payments:
                    final_active_students.append(student)

        serializer=get_serializer('Admin-Student-Plain-Serializer')

        active_students=list(set(final_active_students))
        active_students=serializer(active_students,many=True)
        active_students=active_students.data

        return JsonResponse(active_students,safe=False)
        

    @action(detail=False, methods=['post'])
    def individual_collection(self,request,*args,**kwargs):
        data=request.data
        studentid=data.get('studentid')
        student=Student.objects.get(pk=studentid)

        serializer=get_serializer('Admin-Student-Serializer')
        student=serializer(student).data
        return JsonResponse(student,safe=False)


    @action(detail=False, methods=['post'])
    def search_users(self,request,*args,**kwargs):
        data=request.data
        searchpattern=data.get('searchpattern')

        if searchpattern=='':
            return JsonResponse({'':''})
        student_query=Q(role='Student')

        query=Q(username__icontains=searchpattern)|Q(first_name__icontains=searchpattern)|Q(last_name__icontains=searchpattern)

        users=User.objects.filter(student_query & query)

        # users=User.objects.all()

        serializer=get_serializer('User')

        users=serializer(users,many=True)
        users=users.data

        return JsonResponse(users,safe=False)

    @action(detail=False, methods=['post'])
    def get_student_payments(self,request,*args,**kwargs):
        data=request.data
        studentid=data.get('studentid')
        student=Student.objects.get(pk=studentid)

        serializer=get_serializer('Admin-Student-Serializer')
        student=serializer(student).data
        return JsonResponse(student,safe=False)





























class MaterialsViewset(viewsets.GenericViewSet):
    queryset=None
    serializer_class=None
    permission_classes = (permissions.IsAuthenticated,)


    @action(detail=False,methods=['post'])
    def get_material(self,request,*args,**kwargs):
        data=request.data
        materialid=data.get('materialid')
        material=IAMaterial.objects.get(pk=materialid)
        serializer=get_serializer('IAMaterial')
        material=serializer(material).data



        return JsonResponse(material,safe=False)
    
    @action(detail=False,methods=['post'])
    def get_materials(self,request,*args,**kwargs):
        materials=IAMaterial.objects.all()
        serializer=get_serializer('iamaterial')
        materials=serializer(materials,many=True).data
        return JsonResponse(materials,safe=False)        





class InstructorsViewset(
                # mixins.ListModelMixin,
                # mixins.RetrieveModelMixin,
                # mixins.CreateModelMixin,
                # mixins.UpdateModelMixin,
                # mixins.DestroyModelMixin,
                viewsets.GenericViewSet
                ):
    queryset=None
    serializer_class=None
    permission_classes = (permissions.IsAuthenticated,)


    @action(detail=False,methods=['post'])
    def hoursheet(self,request,*args, **kwargs):
        data=request.data
        userid=data.get('userid')



        instructor=Instructor.objects.get(user__pk=userid)
        mexico_tz=ZoneInfo('America/Mexico_City')

        year=timezone.now().astimezone(mexico_tz).year
        month=timezone.now().astimezone(mexico_tz).month
        today=timezone.now().astimezone(mexico_tz).day
        if today<15:
            month=month-1
            initial_day=16
            final_day=calendar.monthrange(year, month)[1]
        else:
            initial_day=1
            final_day=15



        initial_datetime=datetime(year,month,initial_day,00,00,00).astimezone(mexico_tz)
        final_datetime=datetime(year,month,final_day,23,59,59).astimezone(mexico_tz)

        attendances=Attendance.objects.filter(Q(instructor_confirmation__instructor=instructor),Q(datetime__gte=initial_datetime),Q(datetime__lte=final_datetime)).order_by('-datetime')
        attendances=list(set(attendances))
        for attendance in attendances:
            attendance.pay=instructor.hourly_rate
            if not attendance.group:
                attendance.group=attendance.student_confirmation.last().student.group_set.last()
            attendance.save()

        for attendance in attendances:
            if attendance.instructor_confirmation.last().confirmation in ['confirmed','confirm','Confirmed','no-show','NS','cancelled-late','CL','Cancelled Late']:
                pass
            else:
                attendance.pay=0
                attendance.duration=0
            attendance.save()

        serializer=get_serializer('Instructor-Attendance-Pay-Sheet-Serializer')
        attendances=serializer(attendances,many=True).data


        return JsonResponse(attendances,safe=False)


    @action(detail=False,methods=['post'])
    def get_instructor(self,request,*args, **kwargs):
        data=request.data
        userid=data.get('userid')
        instructor=Instructor.objects.get(user__pk=userid)

        serializer=get_serializer('Instructor-With-Groups')
        instructor=serializer(instructor).data

        return JsonResponse(instructor,safe=False)       

    @action(detail=False,methods=['post'])
    def get_calendar(self,request,*args, **kwargs):
        data=request.data
        user_id=data.get('user_id')
        instructor=Instructor.objects.get(user__pk=user_id)

        calendar={
            'calendar':instructor.calendar,
        }

        return JsonResponse(calendar,safe=False)       





    @action(detail=False,methods=['post'])
    def get_attendance(self,request,*args,**kwargs):
        data=request.data
        groupid=data.get('groupid')
        group=Group.objects.get(pk=groupid)

        attendance=get_todays_group_attendance(group)
        if not attendance:
            return JsonResponse({'none':None})


        serializer=get_serializer('Attendance-UI-Serializer')
        attendance=serializer(attendance).data

        return JsonResponse(attendance,safe=False)


    @action(detail=False,methods=['post'])
    def class_status(self,request,*args,**kwargs):
        data=request.data
        groupid=data.get('groupid')
        userid=data.get('userid')
        status=data.get('status')

        group=Group.objects.get(pk=groupid)


        instructor=Instructor.objects.get(user__pk=userid)
        
        attendance=get_todays_group_attendance(group)

        if not attendance:
            attendance=Attendance.objects.create(group=group)

        attendance.instructor_confirmation.create(instructor=instructor,confirmation=status)



        mexico_tz=ZoneInfo('America/Mexico_City')

        today=timezone.now().astimezone(mexico_tz).date()


        attendance.pay=instructor.hourly_rate
        attendance.duration=group.duration        

        attendance.link=f'https://interactspeakingcenter.com/meet/{group.pk}-{today}'
        if group.link!='':
            attendance.link=group.link
        if instructor.link!='':
            attendance.link=instructor.link
        attendance.save()

        return JsonResponse({'ok':'ok'})

    @action(detail=False,methods=['post'])
    def addmaterial(self,request,*args,**kwargs):
        data=request.data
        selectedmaterialids=data.get('selectedmaterialids')
        attendanceid=data.get('attendanceid')

        attendance=Attendance.objects.get(pk=attendanceid)
        selectedmaterial=IAMaterial.objects.filter(pk__in=selectedmaterialids)
        attendance.iamaterial.clear()
        attendance.iamaterial.add(*selectedmaterial)

        serializer=get_serializer('Attendance-UI-Serializer')
        attendance=serializer(attendance).data

        return JsonResponse(attendance,safe=False)
    
    @action(detail=False,methods=['post'])
    def update_attendance(self,request,*args,**kwargs):
        data=request.data
        attendance_id=data.get('attendance_id')
        attendance_duration=data.get('attendance_duration')
        attendance_material=data.get('attendance_material')
        instructor_id=data.get('instructor_id')

        instructor=Instructor.objects.get(user__id=instructor_id)

        attendance=Attendance.objects.get(pk=attendance_id)
       
        attendance.duration=Decimal(attendance_duration)

        attendance.pay=instructor.hourly_rate*attendance.duration

        group=attendance.group
        if group.pay!=0:
            attendance.pay=group.pay*attendance.duration
        
        # attendance.iamaterial.set(IAMaterial.objects.filter(pk__in=[materialid for materialid in attendance_material.values()]))
        
        
        attendance.save()


        serializer=get_serializer('Attendance-UI-Serializer')
        attendance=serializer(attendance).data

        return JsonResponse(attendance,safe=False)

    @action(detail=False,methods=['post'])
    def update_tutorial(self,request,*args,**kwargs):
        data=request.data
        instructorid=data.get('instructorid')

        instructor=Instructor.objects.get(pk=instructorid)
        instructor.user.tutorial=True

        instructor.user.save()
        return JsonResponse({'ok':'ok'})










class StudentsViewset(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet
                ):
    queryset=None
    serializer_class=None
    permission_classes = (permissions.IsAuthenticated,)


    @action(detail=False,methods=['post'])
    def get_student(self,request,*args, **kwargs):
        data=request.data
        userid=data.get('userid')
        user=User.objects.get(pk=userid)

        student=Student.objects.get(user__pk=userid)

        serializer=get_serializer('Student-With-Groups')
        student=serializer(student).data

        return JsonResponse(student,safe=False)   

    @action(detail=False,methods=['post'])
    def get_materials(self,request,*args,**kwargs):
        materials=IAMaterial.objects.all()
        serializer=get_serializer('IAMaterial')
        materials=serializer(materials,many=True).data
        return JsonResponse(materials,safe=False)

    @action(detail=False,methods=['post'])
    def get_group_attendance(self,request,*args,**kwargs):
        data=request.data
        groupid=data.get('groupid')
        group=Group.objects.get(pk=groupid)
        attendance=get_todays_group_attendance(group)

        if attendance:
            serializer=get_serializer('Attendance-UI-Serializer')
        else:
            return JsonResponse({'none':attendance},safe=False)

        
        

        attendance=serializer(attendance).data
        return JsonResponse(attendance,safe=False)
    

    @action(detail=False,methods=['post'])
    def class_status(self,request,*args,**kwargs):
        data=request.data
        groupid=data.get('groupid')
        userid=data.get('userid')
        status=data.get('status')

        
        group=Group.objects.get(pk=groupid)
        student=Student.objects.get(user__pk=userid)

        if not Payment.objects.filter(package__student=student).exists():
            new_payment=Payment.objects.create(
                method=student.payment_method,
                amount=student.package_cost
            )
            new_payment.package.create(student=student,package_hours=student.package_hours)



        payments=Payment.objects.filter(package__student=student)
        payment=payments.first()

        package=payment.package.first()
        if package.taken_hours>=package.package_hours:
            payment=Payment.objects.create(
                method=student.payment_method,
                amount=student.package_cost
            )
            package=payment.package.create(student=student,package_hours=student.package_hours)

        attendance=get_todays_group_attendance(group)

        if not attendance:
            attendance=Attendance.objects.create(group=group)

        

        attendance.student_confirmation.create(student=student,confirmation=status)

        package.attendance.add(attendance)


        package.save()

        serializer=get_serializer('Attendance-UI-Serializer')
        attendance=serializer(attendance).data

        
        return JsonResponse(attendance,safe=False)

    @action(detail=False,methods=['post'])
    def get_payments(self,request,*args,**kwargs):
        data=request.data
        userid=data.get('userid')
        student=Student.objects.get(user__pk=userid)

        students=[student]


        payments=Payment.objects.filter(package__student__in=students).order_by('-datetime')
        payments=set(payments)
        payments=Payment.objects.filter(pk__in=[payment.pk for payment in payments]).order_by('-datetime')
        serializer=get_serializer('Studentpaymentserializer')
        payments=serializer(payments,many=True).data



        # payments=sorted(payments,key=lambda payment:payment.get('id'),reverse=True)




        return JsonResponse(payments,safe=False)
    
    @action(detail=False,methods=['post'])
    def update_clip_payment_status(self,request,*args,**kwargs):
        data=request.data
        paymentid=data.get('paymentid')
        reference=data.get('reference')
        status=data.get('status')
        paid=False
        if status in ['CHECKOUT_CREATED','CHECKOUT_PENDING']:
            paid=False
        if status in ['CHECKOUT_CANCELLED','CHECKOUT_EXPIRED']:
            paid=False
            reference=''
            status=''
        if status in ['CHECKOUT_COMPLETED']:
            paid=True


        payment=Payment.objects.get(pk=paymentid)
        payment.reference=reference
        payment.status=status
        payment.paid=paid
        payment.save()
        return JsonResponse({'ok':'ok'})
    
    
    @action(detail=False,methods=['post'])
    def update_paypal_payment_status(self,request,*args,**kwargs):
        data=request.data
        paymentid=data.get('paymentid')
        status=data.get('status')

        payment=Payment.objects.get(pk=paymentid)
        payment.status=status
        payment.save()

        return JsonResponse({'ok':'ok'})


    @action(detail=False,methods=['post'])
    def get_paypal_link(self,request,*args,**kwargs):
        data=request.data
        method=data.get('method')

        link='https://www.paypal.com/paypalme/sammerdammer/'

        if 'owl' in method:
            link='https://www.paypal.com/paypalme/diegoortiz1/'
        if 'sloth' in method:
            link='https://www.paypal.com/paypalme/sammerdammer/'
        if 'lion' in method:
            link='https://www.paypal.com/paypalme/fernandoortiz/'
        return JsonResponse({'link':link})
    
    @action(detail=False,methods=['post'])
    def update_tutorial(self,request,*args,**kwargs):
        data=request.data
        studentid=data.get('studentid')

        student=Student.objects.get(pk=studentid)
        student.user.tutorial=True

        student.user.save()
        return JsonResponse({'ok':'ok'})
        



class DatabaseViewset(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet
                ):
    queryset=None
    serializer_class=None
    permission_classes = (permissions.IsAuthenticated,)


    
    @action(detail=False, methods=['post'])
    def get_objects(self,request,*args,**kwargs):
        data=request.data
        model=data.get('model')

        model=get_model(model)

        serializer=get_serializer(model.__name__)

        models=serializer(model.objects.all(),many=True).data

        return JsonResponse(models,safe=False)
    
    @action(detail=False,methods=['post'])
    def get_object(self,request,*args,**kwargs):
        data=request.data
        object=data.get('object')
        modelstring=object.get('endpoint')
        model=get_model(modelstring)
        real_model=model.objects.get(pk=object.get('id'))
        serializer=get_serializer(modelstring)

        real_model=serializer(real_model).data

        return JsonResponse(real_model)

    @action(detail=False, methods=['post'])
    def get_filtered_objects(self,request,*args,**kwargs):
        data=request.data
        model=data.get('model').title()
        parent=data.get('parent')
        parent_model=get_model(parent.get('endpoint'))
        real_parent=parent_model.objects.get(pk=parent.get('id'))

        child_manager=get_related_manager(real_parent,model)
        try:
            real_children=child_manager.all()
            serializer=get_serializer(model)
            serialized_children=serializer(real_children,many=True)
            serialized_children=serialized_children.data
        except Exception as e:
            serializer=get_serializer(model)
            serialized_children=serializer(child_manager).data
            serialized_children=[serialized_children]

        return JsonResponse(serialized_children,safe=False)


    @action(detail=False,methods=['post'])
    def patch(self,request,*args,**kwargs):
        data=request.data
        object=data.get('object')
        attributestring=data.get('attribute')
        attributevalue=data.get('value')
        model=get_model(object.get('endpoint'))
        realmodel=get_real_model(model,object.get('id'))

        if attributestring=='password':
            realmodel.set_password(attributevalue)
        else:
            setattr(realmodel,attributestring,attributevalue)
        realmodel.save()
        return JsonResponse({'patching':[attributestring,attributevalue]},safe=False)
    
    
    @action(detail=False,methods=['post'])
    def addfromlist(self,request,*args,**kwargs):
        data=request.data
        children=data.get('selected')
        childrenmodelstring=data.get('selectedmodelstring')
        parent=data.get('parent')
        parentmodelstring=data.get('parentmodelstring')

        parentmodel=get_model(parentmodelstring)
        real_parent=parentmodel.objects.get(pk=parent.get('id'))

        child_manager=get_related_manager(real_parent,childrenmodelstring)


        childmodel=get_model(childrenmodelstring)

        
        real_children=[]
        for child in children.values():
            real_child=childmodel.objects.get(pk=child.get('id'))
            real_children.append(real_child)
        


        if not child_manager:
            setattr(real_parent,childrenmodelstring,real_children[0])
            real_parent.save()
            models=get_related_manager(real_parent,childrenmodelstring)
            serializer=get_serializer(childrenmodelstring)
            models=serializer(models).data
            models=[models]

        else:
            child_manager.add(*real_children)
            models=child_manager.all()

            serializer=get_serializer(childrenmodelstring)
            models=serializer(models,many=True).data
        # return JsonResponse({'trouble in paradis':'trouble in paradis'})

        return JsonResponse(models,safe=False)



    @action(detail=False,methods=['post'])
    def addnew(self,request,*args,**kwargs):

        data=request.data
        modelstring=data.get('model').title()
        parent=data.get('parentmodel')





        if modelstring in ['Student','Instructor']:

            model=get_model('User')
            new_user=model.objects.create(first_name='new user',email=f'{random.randint(1,100000)}@interactspeakingcenter.com',role=modelstring)

            # getting student or instructor from new user 
            role_related_manager=get_related_manager(new_user,modelstring)
            # getting last since its a related manager though models are foreignfields so for there to be a student or intstructor there mus be a user and that user can be attached to many students though it's usually just the one. Maybe in the future I can add supervisor accounts for children
            role=role_related_manager.last()

            # getting the specific related manager. related managers are specific the model so all() doesn't print all the elements in db it just prints our the model's all()

            model=get_model(role.endpoint)
            final_manager=model.objects
            modeltoserialize=modelstring
        else:

            if parent:
                parentmodelstring=parent.get('endpoint')
                model=get_model(modelstring)
                new_child=model.objects.create()
                parentmodel=get_model(parentmodelstring)
                real_parent_model=parentmodel.objects.get(pk=parent.get('id'))

                child_related_manager=get_related_manager(real_parent_model,modelstring)

                child_related_manager.add(new_child)

                final_manager=child_related_manager
                modeltoserialize=modelstring

            else:
                model=get_model(modelstring)
                model.objects.create()
                serializer=get_serializer(modelstring)
                models=model.objects.all()
                models=serializer(models,many=True).data
                return JsonResponse(models,safe=False)


        models=final_manager.all()

        modelserializer=get_serializer(modeltoserialize)
        models=modelserializer(models,many=True).data

        return JsonResponse(models,safe=False)
    

    @action(detail=False,methods=['post'])
    def remove(self,request,*args,**kwargs):
        data=request.data
        
        children=data.get('selected')
        childmodelstring=data.get('selectedmodelstring')
        parent=data.get('parent')

        
        childmodel=get_model(childmodelstring)
        
        real_children=[]
        for child in children.values():
            child=get_real_model(childmodel,child.get('id'))
            real_children.append(child)


        if parent:
            parentmodelstring=parent.get('endpoint')
            parentmodel=get_model(parentmodelstring)
        else:

            for real_child in real_children:
                real_child.delete()
            model=get_model(childmodelstring)
            models=model.objects.all()
            serializer=get_serializer(childmodelstring)
            models=serializer(models,many=True).data
            return JsonResponse(models,safe=False)
        
        



        real_parent=get_real_model(parentmodel,parent.get('id'))
        child_related_manager=get_related_manager(real_parent,childmodelstring)
        child_related_manager.remove(*real_children)
        modelstoserialize=child_related_manager.all()
        serializer=get_serializer(childmodelstring)
        models=serializer(modelstoserialize,many=True).data

        return JsonResponse(models,safe=False)







    @action(detail=False, methods=['post'])
    def move_objects(self,request,*args,**kwargs):
        
        data=request.data
        parents=data.get('parents')
        children=data.get('children')


        parentmodel=None
        for parent in parents.values():
            parentmodel=get_model(parent.get('endpoint'))
            break

        childmodel=None
        for child in children.values():
            childmodel=get_model(child.get('endpoint'))
            break

        real_parents=[]
        for parent in parents.values():
            real_parents.append(get_real_model(parentmodel,parent.get('id')))

        real_children=[]
        for child in children.values():
            real_children.append(get_real_model(childmodel,child.get('id')))

        for real_child in real_children:
            parent_related_manager=get_related_manager(real_child,parentmodel.__name__)
            parent_related_manager.clear()

        for real_parent in real_parents:            
            related_manager=get_related_manager(real_parent,childmodel.__name__)
            related_manager.add(*real_children)
        
        return JsonResponse({'move_objects':'move_objects'})

    
    
    @action(detail=False, methods=['post'])
    def copy_objects(self,request,*args,**kwargs):
        
        data=request.data
        parents=data.get('parents')
        children=data.get('children')


        parentmodel=None
        for parent in parents.values():
            parentmodel=get_model(parent.get('endpoint'))
            break

        childmodel=None
        for child in children.values():
            childmodel=get_model(child.get('endpoint'))
            break

        
        real_parents=[]
        for parent in parents.values():
            real_parents.append(get_real_model(parentmodel,parent.get('id')))

        real_children=[]
        for child in children.values():
            real_children.append(get_real_model(childmodel,child.get('id')))

        for real_parent in real_parents:
            related_manager=get_related_manager(real_parent,childmodel.__name__)
            related_manager.add(*real_children)
        
        return JsonResponse({'copy_objects':'copy_objects'})

    



def get_real_model(model,id):
    real_model=model.objects.get(pk=id)
    return real_model

def get_model(model):
    model=model.title()
    if 'Set' in model:
        model=model.split('_')[0]

    django_model=None
    for django_model in apps.get_models():
        if 'auth' not in django_model._meta.app_label and django_model.__name__ == model or f'{django_model.__name__}s'==model:
            break
    return django_model
def get_serializer(model0):
    model=model0.title()
    if any(['set' in model,'Set' in model]):
        if model in django_serializers:
            serializer=django_serializers[model]
            return serializer
        model=model.split('_')[0]
    serializer=None
    serializer=django_serializers.get(model)
    if serializer:
        return serializer
    serializer=django_serializers[model0]
    return serializer


def get_related_manager(object_to_check,modelstring):
    modelstring=modelstring.lower()

    related_manager=None
    if hasattr(object_to_check,modelstring):
        related_manager=getattr(object_to_check,modelstring)
    else:
        related_manager=getattr(object_to_check,f'{modelstring}_set')
    return related_manager

def get_todays_group_attendance(group):
    attendance=None
    mexico_tz=ZoneInfo('America/Mexico_City')
    utc=ZoneInfo('UTC')
    today=timezone.now().astimezone(mexico_tz).date()
    start_of_day = datetime.combine(today, time.min, tzinfo=mexico_tz)
    end_of_day = datetime.combine(today, time.max, tzinfo=mexico_tz)
    attendance = Attendance.objects.filter(group__pk=group.pk,datetime__gt=start_of_day,datetime__lt=end_of_day).order_by('datetime').last()

    return attendance




def get_bad_attendances(month_attendances):
    bad_attendances=[]
    for attendance in month_attendances:
        # if not attendance.package_set.exists():
        #     continue
        instructor_confirmation_exists=False
        student_confirmation_exists=False
        confirmation_mismatch=False
        package_missing=False


        if attendance.instructor_confirmation.exists():
            instructor_confirmation_exists=True
            

        if attendance.student_confirmation.exists():
            student_confirmation_exists=True

        instructor_confirmation=None
        if instructor_confirmation_exists:
            instructor_confirmation=attendance.instructor_confirmation.last().confirmation



        student_confirmations=[]
        if student_confirmation_exists:
            if attendance.group!=None:
                for student in attendance.group.student.all():
                    if attendance.student_confirmation.filter(student=student).exists():
                        student_confirmation=attendance.student_confirmation.filter(student=student).last().confirmation
                        student_confirmations.append(student_confirmation)



        for student_confirmation in student_confirmations:
            if student_confirmation != instructor_confirmation:
                confirmation_mismatch=True
                break

        if attendance.group!=None:
            for student in attendance.group.student.all():
                student_package_exists=attendance.package_set.filter(student=student).exists()
                if not student_package_exists:
                    package_missing=True
                    break



        if not instructor_confirmation_exists or not student_confirmation_exists or confirmation_mismatch or package_missing:
            bad_attendances.append(attendance)
    
    serializer=get_serializer('Admin-Maker-Attendance')
    bad_attendances=serializer(bad_attendances,many=True).data

    return bad_attendances









# from django.utils import timezone
# from zoneinfo import ZoneInfo
# from datetime import datetime, time
# from groups.models0 import *
# from groups.models import *

# group=Group.objects.get(pk=27)
# attendance=None
# mexico_tz=ZoneInfo('America/Mexico_City')
# utc=ZoneInfo('UTC')
# today=timezone.now().astimezone(mexico_tz).date()
# start_of_day = datetime.combine(today, time.min, tzinfo=mexico_tz)
# end_of_day = datetime.combine(today, time.max, tzinfo=mexico_tz)
# attendance = Attendance.objects.filter(group__pk=group.pk,datetime__gt=start_of_day,datetime__lt=end_of_day).order_by('datetime').last()

