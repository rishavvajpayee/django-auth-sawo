from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from sawo import createTemplate, getContext, verifyToken
import json
from django.shortcuts import redirect

loader = ''

def setPayload(payload):
    global loader
    loader = payload


createTemplate("templates/partials")

name = {"name" : "Rishav Vajpayee"}
def index(request):
    if(loader):
        return render(request, 'twitter.html', context=name)

    configuration = {
        "auth_key": "02e7db68-af85-4f14-bea3-08d8fbe63c6f",
        "identifier": "email",
        "to": "twitter"
    }
    context = {"sawo": configuration, "load": loader, "title": "Home"}
    return render(request, "index.html", context)


def twitter(request):
    if request.method == 'POST':
        payload = json.loads(request.body)["payload"]
        setPayload(payload)
        if verifyToken(payload):
            status = 200
            return redirect(twitter)
        else:
            status = 404
            response_data = {"status": status}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    return render(request,"twitter.html", context = name)
