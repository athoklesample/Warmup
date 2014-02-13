
import unittest
import sys
from Login.models import UsersModel

class UnitTests(unittest.TestCase):
    
    def testAddBasic(self):
        self.assertEquals(UsersModel.SUCCESS, UsersModel().add("alex1","test"))

    def testAddRepeat(self):
        self.assertEquals(UsersModel.SUCCESS, UsersModel().add("alex2","test"))
        self.assertEquals(UsersModel.ERR_USER_EXISTS, UsersModel().add("alex2","test"))

    def testAddIllegalUser(self):
        self.assertEquals(UsersModel.ERR_BAD_USERNAME, UsersModel().add("",""))
        self.assertEquals(UsersModel.ERR_BAD_USERNAME, UsersModel().add("testtesttetesttesttesttesttesttesttesttesttesttesttestteststtesttesttesttetesttesttesttesttesttesttesttesttesttesttestteststtesttesttesttetesttesttesttesttesttesttesttesttesttesttestteststtesttesttesttetesttesttesttesttesttesttesttesttesttesttestteststtest",""))

    def testIllegalPassword(self):
        self.assertEquals(UsersModel.ERR_BAD_PASSWORD, UsersModel().add("akex","testtesttetesttesttesttesttesttesttesttesttesttesttestteststtesttesttesttetesttesttesttesttesttesttesttesttesttesttestteststtesttesttesttetesttesttesttesttesttesttesttesttesttesttestteststtesttesttesttetesttesttesttesttesttesttesttesttesttesttestteststtest"))

    def testLoginBasic(self):
        self.assertEquals(UsersModel.SUCCESS, UsersModel().add("alex3","test"))
        self.assertEquals(2, UsersModel().login("alex3","test"))

    def testLoginCount(self):
        self.assertEquals(UsersModel.SUCCESS, UsersModel().add("alex4","test"))
        self.assertEquals(2, UsersModel().login("alex4","test"))
        self.assertEquals(3, UsersModel().login("alex4","test"))
        self.assertEquals(4, UsersModel().login("alex4","test"))

    def testLoginFail(self):
        self.assertEquals(UsersModel.ERR_BAD_CREDENTIALS, UsersModel().login("alex5","test"))
        self.assertEquals(UsersModel.SUCCESS, UsersModel().add("alex5","test"))
        self.assertEquals(2, UsersModel().login("alex5","test"))
        self.assertEquals(UsersModel.ERR_BAD_CREDENTIALS, UsersModel().login("alex5","tests"))

    def testDB(self):
        p = UsersModel(user="user",password="password")
        p.save()
        self.assertEquals(UsersModel.SUCCESS, p.count)
        self.assertEquals(UsersModel.SUCCESS, UsersModel.objects.filter(user="user")[0].count)

    def testLoginBlanks(self):
        self.assertEquals(UsersModel.ERR_BAD_CREDENTIALS, UsersModel().login("",""))
        self.assertEquals(UsersModel.ERR_BAD_CREDENTIALS, UsersModel().login("","a"))
    
    def testWipe(self):
        self.assertEquals(UsersModel.SUCCESS, UsersModel().add("b",""))
        self.assertEquals(UsersModel.SUCCESS,UsersModel().TESTAPI_resetFixture())
        self.assertEquals(UsersModel.ERR_BAD_CREDENTIALS, UsersModel().login("b",""))
