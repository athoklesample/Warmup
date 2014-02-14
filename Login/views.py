from django.shortcuts import render_to_response
from django.http import HttpResponse
from Login.models import UsersModel
from django.template import RequestContext
import json
from django.views.decorators.csrf import csrf_exempt
from subprocess import Popen,PIPE

# Create your views here.

@csrf_exempt
def main(request):
    if request.method == "POST":
        value = 0
        if request.path == "/user/login/":
            value = UsersModel().login(user=request.POST['user'],password=request.POST['password'])
        elif request.path == "/user/add/":
            value = UsersModel().add(user=request.POST['user'],password=request.POST['password'])
        if value > 0:
            return HttpResponse(json.dumps({"errCode":1,"count":value}),content_type='application/json', status=200)
        elif value < 0:
            return HttpResponse(json.dumps({"errCode":value}),content_type='application/json', status=200)
        if request.path =="/TESTAPI/resetFixture/":
            return HttpResponse(json.dumps({"errCode":UsersModel().TESTAPI_resetFixture()}),content_type='application/json', status=200)
        elif request.path == "/TESTAPI/unitTests/":
            results = Popen("python manage.py test Login".split(),stderr=PIPE,shell=True).communicate()[1]
            char = results.rfind("Ran")+4
            numTests = int(results[char:char+2])
            echar = results.rfind("failures=")+7
            if echar < 7:
                numFailed = 0
            else :
                numFailed = results[echar:echar+1]
            output = ""
            return HttpResponse(json.dumps({"nrFailed":numFailed,"output":results,"totalTests":numTests}),content_type='application/json', status=200)
    else:
        return render_to_response('Login/client.html',{})


