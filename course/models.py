from django.db import models

# Create your models here.
class Course(models.Model):
    course_code= models.PositiveSmallIntegerField()
    course_title= models.CharField(max_length=20)
    description= models.TextField()
    prerequisites= models.CharField(max_length=20)
    credits= models.PositiveSmallIntegerField()
    department= models.CharField(max_length=20)
    level= models.CharField(max_length=20)
    instructor_name= models.CharField(max_length=20)
    students_offering_course = models.PositiveSmallIntegerField()
    classes = models.CharField(max_length=20)

    def __str__(self) -> str:
         return super().__str__()
        


