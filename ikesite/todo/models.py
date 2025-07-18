from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User  # User model to link with Todo

class Todo(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5, "Todo title must contain at least 5 characters")])
    description = models.TextField(blank=True, null=True)
    date_deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link to the User model

    def __str__(self):
        return self.title



