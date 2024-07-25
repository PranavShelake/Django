from faker import Faker
from home.models import Student
import random

def seed_student(n):
    fake = Faker()
    for i in range(n):
        name = fake.name()
        email =fake.email()
        mark = random.randint(0, 100)
        Student.objects.create(name=name, mark=mark ,email=email)
