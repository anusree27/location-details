from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    ip = requests.get("https://api.ipify.org?format=json")
    ip_data = json.loads(ip.text)
    res = requests.get("http://ip-api.com/json/" + ip_data["ip"])
    data_location = res.text
    datas = json.loads(data_location)
    context = {'datas': datas}
    return render(request, 'base/index.html', context)