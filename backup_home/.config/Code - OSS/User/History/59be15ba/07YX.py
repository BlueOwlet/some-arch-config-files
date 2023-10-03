from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.decorators import action
from django.db.models import Q

from decimal import Decimal

from django.apps import apps

import json

from django.contrib.auth import get_user_model
User = get_user_model()


from django.utils import timezone
from zoneinfo import ZoneInfo
from datetime import datetime, time
import calendar

import random


django_serializers={
#################USERSERIALIZERS#################
    'User':UserSerializer,

    # 'Admin-Maker-Student':AdminMakerStudent,
}





# class DatabaseViewset(
#                 # mixins.ListModelMixin,
#                 # mixins.RetrieveModelMixin,
#                 # mixins.CreateModelMixin,
#                 # mixins.UpdateModelMixin,
#                 # mixins.DestroyModelMixin,
#                 viewsets.GenericViewSet
#                 ):
#     queryset=None
#     serializer_class=None
#     permission_classes = (permissions.IsAuthenticated,)


    
#     @action(detail=False, methods=['post'])
#     def get_objects(self,request,*args,**kwargs):
#         data=request.data
#         model=data.get('model')

#         model=get_model(model)

#         serializer=get_serializer(model.__name__)

#         models=serializer(model.objects.all(),many=True).data

#         return JsonResponse(models,safe=False)
    
#     @action(detail=False,methods=['post'])
#     def get_object(self,request,*args,**kwargs):
#         data=request.data
#         object=data.get('object')
#         modelstring=object.get('endpoint')
#         model=get_model(modelstring)
#         real_model=model.objects.get(pk=object.get('id'))
#         serializer=get_serializer(modelstring)

#         real_model=serializer(real_model).data

#         return JsonResponse(real_model)

#     @action(detail=False, methods=['post'])
#     def get_filtered_objects(self,request,*args,**kwargs):
#         data=request.data
#         model=data.get('model').title()
#         parent=data.get('parent')
#         parent_model=get_model(parent.get('endpoint'))
#         real_parent=parent_model.objects.get(pk=parent.get('id'))

#         child_manager=get_related_manager(real_parent,model)
#         try:
#             real_children=child_manager.all()
#             serializer=get_serializer(model)
#             serialized_children=serializer(real_children,many=True)
#             serialized_children=serialized_children.data
#         except Exception as e:
#             serializer=get_serializer(model)
#             serialized_children=serializer(child_manager).data
#             serialized_children=[serialized_children]

#         return JsonResponse(serialized_children,safe=False)


#     @action(detail=False,methods=['post'])
#     def patch(self,request,*args,**kwargs):
#         data=request.data
#         object=data.get('object')
#         attributestring=data.get('attribute')
#         attributevalue=data.get('value')
#         model=get_model(object.get('endpoint'))
#         realmodel=get_real_model(model,object.get('id'))

#         if attributestring=='password':
#             realmodel.set_password(attributevalue)
#         else:
#             setattr(realmodel,attributestring,attributevalue)
#         realmodel.save()
#         return JsonResponse({'patching':[attributestring,attributevalue]},safe=False)
    
    
#     @action(detail=False,methods=['post'])
#     def addfromlist(self,request,*args,**kwargs):
#         data=request.data
#         children=data.get('selected')
#         childrenmodelstring=data.get('selectedmodelstring')
#         parent=data.get('parent')
#         parentmodelstring=data.get('parentmodelstring')

#         parentmodel=get_model(parentmodelstring)
#         real_parent=parentmodel.objects.get(pk=parent.get('id'))

#         child_manager=get_related_manager(real_parent,childrenmodelstring)


#         childmodel=get_model(childrenmodelstring)

        
#         real_children=[]
#         for child in children.values():
#             real_child=childmodel.objects.get(pk=child.get('id'))
#             real_children.append(real_child)
        


#         if not child_manager:
#             setattr(real_parent,childrenmodelstring,real_children[0])
#             real_parent.save()
#             models=get_related_manager(real_parent,childrenmodelstring)
#             serializer=get_serializer(childrenmodelstring)
#             models=serializer(models).data
#             models=[models]

#         else:
#             child_manager.add(*real_children)
#             models=child_manager.all()

#             serializer=get_serializer(childrenmodelstring)
#             models=serializer(models,many=True).data
#         # return JsonResponse({'trouble in paradis':'trouble in paradis'})

#         return JsonResponse(models,safe=False)



#     @action(detail=False,methods=['post'])
#     def addnew(self,request,*args,**kwargs):

#         data=request.data
#         modelstring=data.get('model').title()
#         parent=data.get('parentmodel')





#         if modelstring in ['Student','Instructor']:

#             model=get_model('User')
#             new_user=model.objects.create(first_name='new user',email=f'{random.randint(1,100000)}@interactspeakingcenter.com',role=modelstring)

#             # getting student or instructor from new user 
#             role_related_manager=get_related_manager(new_user,modelstring)
#             # getting last since its a related manager though models are foreignfields so for there to be a student or intstructor there mus be a user and that user can be attached to many students though it's usually just the one. Maybe in the future I can add supervisor accounts for children
#             role=role_related_manager.last()

#             # getting the specific related manager. related managers are specific the model so all() doesn't print all the elements in db it just prints our the model's all()

#             model=get_model(role.endpoint)
#             final_manager=model.objects
#             modeltoserialize=modelstring
#         else:

#             if parent:
#                 parentmodelstring=parent.get('endpoint')
#                 model=get_model(modelstring)
#                 new_child=model.objects.create()
#                 parentmodel=get_model(parentmodelstring)
#                 real_parent_model=parentmodel.objects.get(pk=parent.get('id'))

#                 child_related_manager=get_related_manager(real_parent_model,modelstring)

#                 child_related_manager.add(new_child)

#                 final_manager=child_related_manager
#                 modeltoserialize=modelstring

#             else:
#                 model=get_model(modelstring)
#                 model.objects.create()
#                 serializer=get_serializer(modelstring)
#                 models=model.objects.all()
#                 models=serializer(models,many=True).data
#                 return JsonResponse(models,safe=False)


#         models=final_manager.all()

#         modelserializer=get_serializer(modeltoserialize)
#         models=modelserializer(models,many=True).data

#         return JsonResponse(models,safe=False)
    

#     @action(detail=False,methods=['post'])
#     def remove(self,request,*args,**kwargs):
#         data=request.data
        
#         children=data.get('selected')
#         childmodelstring=data.get('selectedmodelstring')
#         parent=data.get('parent')

        
#         childmodel=get_model(childmodelstring)
        
#         real_children=[]
#         for child in children.values():
#             child=get_real_model(childmodel,child.get('id'))
#             real_children.append(child)


#         if parent:
#             parentmodelstring=parent.get('endpoint')
#             parentmodel=get_model(parentmodelstring)
#         else:

#             for real_child in real_children:
#                 real_child.delete()
#             model=get_model(childmodelstring)
#             models=model.objects.all()
#             serializer=get_serializer(childmodelstring)
#             models=serializer(models,many=True).data
#             return JsonResponse(models,safe=False)
        
        



#         real_parent=get_real_model(parentmodel,parent.get('id'))
#         child_related_manager=get_related_manager(real_parent,childmodelstring)
#         child_related_manager.remove(*real_children)
#         modelstoserialize=child_related_manager.all()
#         serializer=get_serializer(childmodelstring)
#         models=serializer(modelstoserialize,many=True).data

#         return JsonResponse(models,safe=False)







#     @action(detail=False, methods=['post'])
#     def move_objects(self,request,*args,**kwargs):
        
#         data=request.data
#         parents=data.get('parents')
#         children=data.get('children')


#         parentmodel=None
#         for parent in parents.values():
#             parentmodel=get_model(parent.get('endpoint'))
#             break

#         childmodel=None
#         for child in children.values():
#             childmodel=get_model(child.get('endpoint'))
#             break

#         real_parents=[]
#         for parent in parents.values():
#             real_parents.append(get_real_model(parentmodel,parent.get('id')))

#         real_children=[]
#         for child in children.values():
#             real_children.append(get_real_model(childmodel,child.get('id')))

#         for real_child in real_children:
#             parent_related_manager=get_related_manager(real_child,parentmodel.__name__)
#             parent_related_manager.clear()

#         for real_parent in real_parents:            
#             related_manager=get_related_manager(real_parent,childmodel.__name__)
#             related_manager.add(*real_children)
        
#         return JsonResponse({'move_objects':'move_objects'})

    
    
#     @action(detail=False, methods=['post'])
#     def copy_objects(self,request,*args,**kwargs):
        
#         data=request.data
#         parents=data.get('parents')
#         children=data.get('children')


#         parentmodel=None
#         for parent in parents.values():
#             parentmodel=get_model(parent.get('endpoint'))
#             break

#         childmodel=None
#         for child in children.values():
#             childmodel=get_model(child.get('endpoint'))
#             break

        
#         real_parents=[]
#         for parent in parents.values():
#             real_parents.append(get_real_model(parentmodel,parent.get('id')))

#         real_children=[]
#         for child in children.values():
#             real_children.append(get_real_model(childmodel,child.get('id')))

#         for real_parent in real_parents:
#             related_manager=get_related_manager(real_parent,childmodel.__name__)
#             related_manager.add(*real_children)
        
#         return JsonResponse({'copy_objects':'copy_objects'})

    



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

