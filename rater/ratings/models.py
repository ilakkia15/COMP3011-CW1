from django.db import models

# Create your models here.

class Professor(models.Model):
    professor_id = models.CharField(max_length=3, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.professor_id + " - " + self.first_name + " " + self.last_name

class Module(models.Model):
    module_code = models.CharField(max_length=3, unique=True)
    module_name = models.CharField(max_length=100)

    def __str__(self):
        return self.module_code + " - " + self.module_name

class Instance(models.Model):
    professor = models.ManyToManyField(Professor)
    module = models.ForeignKey(Module, on_delete=models.PROTECT)

    # Create a list to store the year choices.
    year_choices = [(year_choice, str(year_choice)) for year_choice in range(2000, 2025)]
    year = models.PositiveIntegerField(choices=year_choices)

    # Create a list to store the semester choices.
    semester_choices = [
        (1, 'Semester 1'),
        (2, 'Semester 2'),
    ]
    semester = models.PositiveIntegerField(choices=semester_choices)

    # TODO: Return the corresponding instance information
    def __str__(self):
        return self.professor + " - " + self.module

class Student(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Rating(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

    # Create a list to store the rating choices.
    rating_choices = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    rating = models.PositiveIntegerField(choices=rating_choices)

    def __str__(self):
        return self.rating
