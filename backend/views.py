from django.shortcuts import render
from django.http import JsonResponse
from .models import Network

def get_network_statistics(request):
    # Query your database to get the statistics
    no_risk_count = Network.objects.filter(status='No risk of failure').count()
    risk_count = Network.objects.filter(status='Risk of failure').count()
    risk_confirmed_count = Network.objects.filter(status='Risk confirmed').count()

    statistics = {
        'no_risk': no_risk_count,
        'risk': risk_count,
        'risk_confirmed': risk_confirmed_count,
    }
    return JsonResponse(statistics)

def get_network_lists(request):
    # Query your database to get the lists
    risk_networks = Network.objects.filter(status='Risk of failure')
    confirmed_networks = Network.objects.filter(status='Risk confirmed')

    risk_list = [network.name for network in risk_networks]
    confirmed_list = [network.name for network in confirmed_networks]

    data = {
        'risk_list': risk_list,
        'confirmed_list': confirmed_list,
    }
    return JsonResponse(data)
