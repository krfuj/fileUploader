from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    f_name = models.TextField(max_length=100)
    l_name = models.TextField(max_length=100)
    files_upload = models.FileField(upload_to ='uploads/% Y/% m/% d/')

    def __str__(self):
        return self.user.username
   