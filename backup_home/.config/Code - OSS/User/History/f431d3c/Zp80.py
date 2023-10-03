from django.dispatch import receiver
from django.db.models.signals import (post_save)

# from students.models import Student
# from instructors.models import Instructor

from django.contrib.auth import get_user_model
User = get_user_model()




# @receiver(post_save,sender=User)
# def create_or_save_profile(sender,instance,created,*args,**kwargs):
#     print('signal getting triggered')
#     print(sender,instance,created)
#     if 'Admin' in instance.role:
#         print('dis guy admin')
#     elif 'Student' in instance.role:
#         if created:
#             profile=Student.objects.create(user=instance)
#             print('Student profile created')
#         else:
#             if instance.student_set.all():
#                 print('not empty')
#                 instance.student_set.all()[0].save()
#             else:
#                 profile=Student.objects.create(user=instance)
#                 instance.student_set.all()[0].save()
#             print('Student profile saved')

#     elif 'Instructor' in instance.role:
#         if created:
#             profile=Instructor.objects.create(user=instance)
#             print('Instructor profile created')
#         else:
#             if instance.instructor_set.all():
#                 print('not empty')
#                 instance.instructor_set.all()[0].save()
#             else:
#                 profile=Instructor.objects.create(user=instance)
#                 instance.instructor_set.all()[0].save()
#             print('Instructor profile saved')
