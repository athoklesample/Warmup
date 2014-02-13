from django.test import TestCase
import sys
from Login.models import UsersModel

class UnitTests(TestCase):
    
    def setUp(self):
        self.users = models.UsersModel()
        self.users.TESTAPI_resetFixture()

    def addBasic(self):
        self.assertEquals(UsersModel.SUCCESS, self.users.add("alex","test"))

    def addRepeat(self):
        self.assertEquals(UsersModel.SUCCESS, self.users.add("alex","test"))
        self.assertEquals(UsersModel.ERR_USER_EXISTS, self.users.add("alex","test"))

    def addIllegalUser(self):
        self.assertEquals(UsersModel.ERR_BAD_USERNAME, self.users.add("",""))
        self.assertEquals(UsersModel.ERR_BAD_PASSWORD, self.users.add("akex","testtesttetesttesttesttesttesttesttesttesttesttesttestteststtesttesttesttetesttesttesttesttesttesttesttesttesttesttestteststtest"))

    def loginBasic(self):
        self.assertEquals(UsersModel.SUCCESS, self.users.add("alex","test"))
        self.assertEquals(UsersModel.SUCCESS, self.users.login("alex","test"))

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
