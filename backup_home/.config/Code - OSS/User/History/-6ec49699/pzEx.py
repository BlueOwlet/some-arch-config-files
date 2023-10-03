from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()


from zoneinfo import ZoneInfo





# CUSTOM SERIALIZED FIELD

# class CustomDateTimeField(serializers.DateTimeField):
#     def to_representation(self, value):
#         mexico_tz=ZoneInfo('America/Mexico_City')
#         value=value.astimezone(mexico_tz)
#         formatted_datetime = value.strftime('%Y-%m-%dT%H:%M')

#         return formatted_datetime



# CUSTOM SERIALIZER

# class AdminMakerAttendance(serializers.ModelSerializer):
#     # instructor_confirmation=AdminMakerInstructorConfirmation(many=True,read_only=True)
#     # student_confirmation=AdminMakerStudentConfirmation(many=True,read_only=True)
#     # group=AdminMakerGroup()
#     datetime=CustomDateTimeField()
#     class Meta:
#         model=Attendance
#         fields='__all__'
#         depth=4
