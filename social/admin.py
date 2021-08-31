from django.contrib import admin
from social import models

# Register your models here.

admin.site.register([
    models.Post,
    models.Friend,
    models.Like,
    models.Comment
])
