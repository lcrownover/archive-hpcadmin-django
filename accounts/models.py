from django.db import models


# class Index(models.Model):
#     code = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.code


class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    is_pi = models.BooleanField()
    sponsor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username


class Pirg(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pirg_owner",
    )
    users = models.ManyToManyField(
        User,
        related_name="pirg_users",
    )
    admins = models.ManyToManyField(
        User,
        related_name="pirg_admins",
    )
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
