from django.db import models

# Create your models here.
class Students(models.Model):
    student_code=models.SmallIntegerField()
    first_name = models.CharField(max_length= 20)
    last_name=models.CharField(max_length= 20)
    date_of_birth=models.DateField()
    email=models.EmailField()
    phone_number=models.CharField(max_length= 20)
    address=models.CharField(max_length= 20)
    GPA=models.PositiveSmallIntegerField()
    enrollment_date=models.DateField()
    classroom=models.CharField(max_length= 20)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

