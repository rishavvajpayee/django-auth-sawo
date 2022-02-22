from re import S
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from sawo import createTemplate, getContext, verifyToken
import json

from .models import Config
# from decouple import config
# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, '/sample.env')
# Create your views here.

load = ''
loaded = 0


def setPayload(payload):
    global load
    load = payload

def setLoaded(reset=False):
    global loaded
    if reset:
        loaded=0
    else:
        loaded+=1

createTemplate("templates/partials")

def index(request):
    setLoaded()
    setPayload(load if loaded<2 else '')
    # print(config('api_key'))

    configuration = {
                "auth_key": "02e7db68-af85-4f14-bea3-08d8fbe63c6f",
                "identifier": "email",
                "to": receive
    }
    config = Config.objects.order_by('-api_key')[:1]
    context = {"sawo": configuration}
    # context = {"sawo":getContext(config,"login")}


    return render(request,"index.html", context=context)


def receive(request, method='POST'):
      # context = {"sawo":getContext(config,"login")}
    if request.method == 'POST':
        payload = json.loads(request.body)["payload"]
        setLoaded(True)
        setPayload(payload)
        print(payload)
        verifyToken(payload)

        if verifyToken(payload):
            return HttpResponse("hello world")
        else:
            status = 404
            print(status)
            print("----------------")
            response_data = {"status":status}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

def twitter(request):
    return render(request,"twitter.html")
