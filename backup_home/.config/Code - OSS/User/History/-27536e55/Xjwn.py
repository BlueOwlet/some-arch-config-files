from django.db import models
from groups.models import Group
from materials.models import IAMaterial
from students.models import Student,Student_Confirmation
from instructors.models import Instructor,Instructor_Confirmation
from django.utils import timezone


class Attendance(models.Model):
    instructor_confirmation=models.ManyToManyField(Instructor_Confirmation,blank=True)
    student_confirmation=models.ManyToManyField(Student_Confirmation,blank=True)
    datetime=models.DateTimeField(blank=True,null=True,default=timezone.now)
    group=models.ForeignKey(Group, blank=True,null=True, on_delete=models.SET_NULL)
    pay=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0,null=True)
    iamaterial=models.ManyToManyField(IAMaterial, blank=True,null=True)
    duration=models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=2,default=0)
    link=models.CharField(blank=True,max_length=1000)
    admin_check=models.CharField(blank=True,max_length=100)
    endpoint=models.CharField(max_length=100,default='Attendance')
    ui=models.CharField(max_length=1000,default='attendance')


    def save(self,*args,**kwargs):
        if self.id:
            students=[]
            final_student_confirmations=[]
            try:
                student_confirmations=self.student_confirmation.all()
                if student_confirmations:
                    for student_confirmation in student_confirmations:
                        students.append(student_confirmation.student)
                    students=set(students)
                    final_student_confirmations=[f'{student_confirmations.filter(student=student).last().ui}. ' for student in students]
            except Exception as e:
                print(e)

            instructor_confirmation=''
            try:
                instructor_confirmation=self.instructor_confirmation.last().ui
            except Exception as e:
                print(e)

            self.ui=f'{self.datetime} | {instructor_confirmation} | {final_student_confirmations}'
        super(Attendance,self).save(*args,**kwargs)

    class Meta:
        ordering=['-datetime']


class Package(models.Model):
    student=models.ForeignKey(Student,null=True,blank=True,on_delete=models.SET_NULL)
    attendance=models.ManyToManyField(Attendance,blank=True)
    datetime=models.DateTimeField(blank=True,null=True,default=timezone.now)

    package_hours=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=8)
    taken_hours=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0)
    endpoint=models.CharField(max_length=100,default='Package')


    past_id=models.CharField(max_length=100,blank=True,null=True)


    ui=models.CharField(max_length=1000,default='package')


    def save(self,*args,**kwargs):
        if self.pk:
            if self.attendance.all().exists():
                total_taken_hours=0
                for attendance in self.attendance.all():
                    confirm_check=False
                    if attendance.student_confirmation.filter(student=self.student).exists():
                        if attendance.student_confirmation.filter(student=self.student).last().confirmation in ['confirm','confirmed','Confirmed','cancelled-late','CL','no-show','NS','WaitingforConfirmation']:
                            # if confirm_check:
                                # pass
                            # else:
                            total_taken_hours+=attendance.duration
                            confirm_check=True
                self.taken_hours=total_taken_hours
            
            if self.student:
                self.ui=f'{self.student.ui} | {self.taken_hours}/{self.package_hours}'
            
            else:
                self.ui=f'{self.taken_hours}/{self.package_hours}'


        super(Package,self).save(*args,**kwargs)
    
    class Meta:
        ordering=['-datetime']



    



class Invoice(models.Model):
    date=models.DateField(default=timezone.now)
    amount=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=2400)
    method=models.CharField(max_length=100)
    paid=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,default=False)
    reference=models.CharField(max_length=100)
    endpoint=models.CharField(max_length=100,default='Invoice')
    ui=models.CharField(max_length=1000,default='invoice')


    def save(self,*args,**kwargs):
        self.ui=f'{self.reference} | {self.method} | {self.paid}'
        super(Invoice,self).save(*args,**kwargs)


class Payment(models.Model):

    package=models.ManyToManyField(Package,blank=True)

    invoice=models.ManyToManyField(Invoice,blank=True)
    datetime=models.DateTimeField(default=timezone.now)
    amount=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=2400)
    method=models.CharField(max_length=100,blank=True,default='clip')
    paid=models.BooleanField(blank=True,null=True,default=False)
    reference=models.CharField(max_length=1000,default='',blank=True,null=True)
    status=models.CharField(max_length=1000,default='',blank=True,null=True)
    comments=models.TextField(max_length=1000,default='',blank=True,null=True)

    endpoint=models.CharField(max_length=100,default='Payment')

    past_id=models.CharField(max_length=100,blank=True,null=True)


    ui=models.CharField(max_length=1000,default='payment')


    def save(self,*args,**kwargs):
        self.ui=f'{self.status} {self.method} | {self.amount} | {self.paid}'

        super(Payment,self).save(*args,**kwargs)


    class Meta:
        ordering=['-datetime']


