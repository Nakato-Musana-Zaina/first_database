from django.db import models

# Create your models here.
class Classroom(models.Model):
    class_code = models.PositiveSmallIntegerField()
    room_number=models.PositiveSmallIntegerField()
    capacity=models.PositiveSmallIntegerField()
    teacher=models.PositiveSmallIntegerField()
    course=models.CharField(max_length =20)
    start_time=models.TimeField()
    end_time=models.TimeField()
    day_of_week=models.PositiveSmallIntegerField()
    seating_arrangement=models.CharField(max_length =20)
    equipment=models.TextField()


    def __str__(self) -> str:
        return super().__str__()
