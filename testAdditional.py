import unittest
import os
import testLib

# Create your tests here.
class TestAddUser(testLib.RestTestCase):
    SUCCESS =              1     # : a success
    ERR_BAD_CREDENTIALS = -1     # : (for login only) cannot find the user/password pair in the database
    ERR_USER_EXISTS     = -2     #: (for add only) trying to add a user that already exists
    ERR_BAD_USERNAME    = -3     #: (for add, or login) invalid user name (only empty string is invalid for now)
    ERR_BAD_PASSWORD    = -4
    """Testing adding users"""
    def testcorrectAdd(self):
        """Adds a new user."""
        response = self.makeRequest("/user/add/",method="POST", data = { 'user':'test1','password':'1234'})
        self.assertDictEqual(response,{'errCode':SUCCESS,'count':1})

    def testrepeatAdd(self):
        """adds the same user"""
        init = self.makeRequest("/user/add/",method="POST", data = { 'user':'test2','password':'1234'})
        response = self.makeRequest("/user/add/",method="POST", data = { 'user':'test2','password':'1234'})
        self.assertDictEqual(response,{'errCode':ERR_USER_EXISTS})

    def testlengthCheckUser(self):
        response = self.makeRequest("/user/add/",method="POST", data = { 'user':'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest','password':'1234'})
        self.assertDictEqual(response,{'errCode':ERR_BAD_USERNAME})
        response = self.makeRequest("/user/add/",method="POST", data = { 'user':'','password':''})
        self.assertDictEqual(response,{'errCode':ERR_BAD_USERNAME})


    def testlengthCheckPass(self):
        response = self.makeRequest("/user/add/",method="POST", data = { 'user':'longpass','password':'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest'})
        self.assertDictEqual(response,{'errCode':ERR_BAD_PASSWORD})

class TestLogin(testLib.RestTestCase):
    SUCCESS =              1     # : a success
    ERR_BAD_CREDENTIALS = -1     # : (for login only) cannot find the user/password pair in the database
    ERR_USER_EXISTS     = -2     #: (for add only) trying to add a user that already exists
    ERR_BAD_USERNAME    = -3     #: (for add, or login) invalid user name (only empty string is invalid for now)
    ERR_BAD_PASSWORD    = -4


    def testloginSuccess(self):
        init = self.makeRequest("/user/add/",method="POST", data = { 'user':'test3','password':'1234'})
        response = self.makeRequest("/user/login/",method="POST", data = { 'user':'test3','password':'1234'})
        self.assertDictEqual(response,{'errCode':SUCCESS,'count':1})

    def testcounter(self):
        init = self.makeRequest("/user/add/",method="POST", data = { 'user':'test4','password':'1234'})
        first = self.makeRequest("/user/login/",method="POST", data = { 'user':'test4','password':'1234'})
        second = self.makeRequest("/user/login/",method="POST", data = { 'user':'test4','password':'1234'})
        third = self.makeRequest("/user/login/",method="POST", data = { 'user':'test4','password':'1234'})
        self.assertDictEqual(third,{'errCode':SUCCESS,'count':3})

    def testloginFailUser(self):
        response = self.makeRequest("/user/login/",method="POST", data = { 'user':'test5','password':'1234'})
        self.assertDictEqual(response, {'errCode':ERR_BAD_CREDENTIALS})

    def testloginFailPass(self):
        init = self.makeRequest("/user/add/",method="POST", data = { 'user':'test6','password':'1234'})
        response = self.makeRequest("/user/login/",method="POST", data = { 'user':'test6','password':'abcd'})
        self.assertDictEqual(response, {'errCode':ERR_BAD_CREDENTIALS})



