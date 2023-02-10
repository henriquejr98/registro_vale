from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Register(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return f'{self.employee} - R${self.amount} - {self.pub_date.strftime("%d %B")}'