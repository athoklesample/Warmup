from django.db import models


# Create your models here.
class UsersModel(models.Model):
    user = models.CharField(max_length=128, primary_key=True)
    password = models.CharField(max_length=128)
    count = models.IntegerField(default=1)

    SUCCESS = 1
    ERR_BAD_CREDENTIALS = -1
    ERR_USER_EXISTS = -2
    ERR_BAD_USERNAME = -3
    ERR_BAD_PASSWORD = -4
    MAX_USERNAME_LENGTH = 128
    MAX_PASSWORD_LENGTH = 128

    def login(self, user, password):
        users = UsersModel.objects.filter(user=user)
        if len(users) == 0:
            return self.ERR_BAD_CREDENTIALS
        if users[0].password == password:
            users[0].count += 1
            users[0].save()
            return users[0].count
        return self.ERR_BAD_CREDENTIALS
        

    def add(self,user, password):
        if user =="" or len(user) > self.MAX_USERNAME_LENGTH:
            return self.ERR_BAD_USERNAME
        if len(password) > self.MAX_PASSWORD_LENGTH:
            return self.ERR_BAD_PASSWORD
        if len(UsersModel.objects.filter(user=user))>0:
            return self.ERR_USER_EXISTS
        newLogin = UsersModel(user=user,password=password)
        newLogin.save()
        return newLogin.count
        

    def TESTAPI_resetFixture(self):
        UsersModel.objects.all().delete()
        return self.SUCCESS
    
