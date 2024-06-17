from django.db import models

# Create your models here.
class Teachers(models.Model):
    teacher_number = models.SmallIntegerField()
    first_name= models.CharField(max_width=20)
    last_name= models.CharField(max_width=20)
    email= models.EmailField()
    phone_number= models.CharField(max_width=20)
    subject_specialization= models.CharField(max_width=20)
    office_hours= models.PositiveSmallIntegerField()
    years_of_experience= models.PositiveSmallIntegerField()
    courses_taught= models.PositiveSmallIntegerField()
    Age= models.PositiveSmallIntegerField()


    def __str__(self) -> str:
        return super().__str__()


