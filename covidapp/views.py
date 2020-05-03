from django.shortcuts import render
import requests
import json


def index(request):
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring = {"country": "India"}
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "88aaa12733mshb20c46d202fe0a6p108a23jsn0cf39c257d7b"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring).json()
    d = response['response']
    s = d[0]
    print(d)
    context = {
        'all': s['cases']['total'],
        'recovered': s['cases']['recovered'],
        'deaths': s['deaths']['total'],
        'new': s['cases']['new'],
        'serious': s['cases']['critical'],
    }
    return render(request, 'covidapp/index.html', context)
