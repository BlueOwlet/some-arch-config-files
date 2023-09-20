# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer

# from users.models import User
# from users.serializers import UserSerializer


# from instructors.models import Instructor
# from instructors.serializers import InstructorSerializer

# from groups.models import Group

# from students.models import Student
# from students.serializers import StudentSerializer


# from djangochannelsrestframework.decorators import action
# from djangochannelsrestframework.observer import model_observer
# from djangochannelsrestframework import permissions
# from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
# from djangochannelsrestframework.mixins import (
#     ListModelMixin,
#     RetrieveModelMixin,
#     PatchModelMixin,
#     UpdateModelMixin,
#     CreateModelMixin,
#     DeleteModelMixin,
# )


# from channels.db import database_sync_to_async

# import secrets


# class Instructors_Consumer(
#         ListModelMixin,
#         # RetrieveModelMixin,
#         PatchModelMixin,
#         UpdateModelMixin,
#         CreateModelMixin,
#         DeleteModelMixin,
#         ObserverModelInstanceMixin,
#         GenericAsyncAPIConsumer):

#     permission_classes = (permissions.AllowAny,)
#     queryset=Instructor.objects.all()
#     serializer_class=InstructorSerializer

#     @action()
#     async def subscribe_to_instructors_feed(self, request_id, **kwargs):
#         await self.instructors_feed.subscribe(request_id=request_id)

#     @model_observer(Instructor,serializer_class=InstructorSerializer)
#     async def instructors_feed(self, data, action, subscribing_request_ids=[], **kwargs):
#         # print(data,action,subscribing_request_ids)
#         for request_id in subscribing_request_ids:
#             await self.reply(data=data, action=action, request_id=request_id)

#     @action()
#     async def create_model(self, *args, **kwargs):
#         data=kwargs.get('data')
#         object=await self.create_model_db(data)
#         return object,200

#     @database_sync_to_async
#     def create_model_db(self,data):
#         print(data)

#         email=f'{secrets.SystemRandom().randint(1,1000000)}@{secrets.SystemRandom().randint(1,1000000)}.com'
#         username=secrets.SystemRandom().randint(1,1000000)

#         new_user=User.objects.create(first_name='first_name',last_name='last_name',role="Instructor",email=email,username=username)

#         new_instructor=new_user.instructor_set.first()

#         new_instructor=InstructorSerializer(new_instructor).data
#         print(new_user)
#         print(new_instructor)

#         return new_instructor




# class Groups_Consumer(
#         ListModelMixin,
#         # RetrieveModelMixin,
#         PatchModelMixin,
#         UpdateModelMixin,
#         CreateModelMixin,
#         DeleteModelMixin,
#         ObserverModelInstanceMixin,
#         GenericAsyncAPIConsumer):

#     permission_classes = (permissions.AllowAny,)
#     queryset=Group.objects.all()
#     serializer_class=GroupSerializer


#     @action()
#     async def subscribe_to_groups_feed(self, request_id, **kwargs):
#         await self.groups_feed.subscribe(request_id=request_id)

#     @model_observer(Group,serializer_class=GroupSerializer)
#     async def groups_feed(self, data, action, subscribing_request_ids=[], **kwargs):

#         for request_id in subscribing_request_ids:
#             await self.reply(data=data, action=action, request_id=request_id)
#     @action()
#     async def create_and_add_student(self, *args, **kwargs):
#         data=kwargs.get('data')
#         new_group=await self.create_and_add_student_db(data)
#         return new_group,200

#     @database_sync_to_async
#     def create_and_add_student_db(self,data):
#         pk=int(data.get('pk'))
#         group=Group.objects.get(pk=pk)

#         email=f'{secrets.SystemRandom().randint(1,1000000)}@{secrets.SystemRandom().randint(1,1000000)}.com'
#         username=secrets.SystemRandom().randint(1,1000000)
#         first_name=secrets.SystemRandom().randint(1,1000000)
#         new_user=User.objects.create(first_name=first_name,role="Student",email=email,username=username)
#         new_student=new_user.student_set.first()
#         group.student.add(new_student)
#         group.save()
#         new_student=StudentSerializer(new_student).data

#         response={
#             'new_student':new_student,
#             'parent':pk,
#         }
#         return response





# class Students_Consumer(
#         ListModelMixin,
#         # RetrieveModelMixin,
#         PatchModelMixin,
#         UpdateModelMixin,
#         CreateModelMixin,
#         DeleteModelMixin,
#         ObserverModelInstanceMixin,
#         GenericAsyncAPIConsumer):

#     permission_classes = (permissions.AllowAny,)
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     @action()
#     async def subscribe_to_students_feed(self, request_id, **kwargs):
#         await self.students_feed.subscribe(request_id=request_id)

#     @model_observer(Student,serializer_class=StudentSerializer)
#     async def students_feed(self, data, action, subscribing_request_ids=[], **kwargs):
#         # print(data,action,subscribing_request_ids)
#         for request_id in subscribing_request_ids:
#             await self.reply(data=data, action=action, request_id=request_id)





# class Users_Consumer(
#         ListModelMixin,
#         # RetrieveModelMixin,
#         PatchModelMixin,
#         UpdateModelMixin,
#         CreateModelMixin,
#         DeleteModelMixin,
#         ObserverModelInstanceMixin,
#         GenericAsyncAPIConsumer):

#     permission_classes = (permissions.AllowAny,)
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

#     @action()
#     async def subscribe_to_users_feed(self, request_id, **kwargs):
#         await self.users_feed.subscribe(request_id=request_id)

#     @model_observer(User,serializer_class=UserSerializer)
#     async def users_feed(self, data, action, subscribing_request_ids=[], **kwargs):
#         # print(data,action,subscribing_request_ids)
#         for request_id in subscribing_request_ids:
#             await self.reply(data=data, action=action, request_id=request_id)





# from channels_demultiplexer.demultiplexer import WebsocketDemultiplexer
# class DMultiplexer(WebsocketDemultiplexer):
#     consumer_classes={
#         # "users":Users_Consumer,
#         # "groups":Groups_Consumer,
#         # "instructors":Instructors_Consumer,
#         # "students":Students_Consumer,

#     }
