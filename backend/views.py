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

from rest_framework import serializers, viewsets
from .models import Network

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'

class NetworkPredictView(viewsets.ReadOnlyModelViewSet):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()

    def get_queryset(self):
        # You can implement your prediction logic here and filter the queryset
        # For example, if 'prediction' is a field in your Network model indicating status:
        # return Network.objects.filter(prediction='No Risk')
        return Network.objects.all()  # For demonstration purposes
