from django.db import models

# Create your models here.

# vo와 비슷한 개념이나 이를 기반으로 table만듬

# 모든 모델은 Model 상속
class Emaillist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)






    def __str__(self):
        return f'Emaillist({self.first_name}, {self.last_name}, {self.email})'

