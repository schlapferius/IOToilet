from chartit import DataPool, Chart
from django.shortcuts import render_to_response

from poow.models import Measure


def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': Measure.objects.all()},
              'terms': [
                'timestamp',
                'sensor_fr',
                'sensor_fl',
                'sensor_br',
                'sensor_bl',]}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'timestamp': [
                      'sensor_fr',
                      'sensor_fl',
                      'sensor_br',
                      'sensor_bl',
                    ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'Data on your shit'},
               'xAxis': {
                    'title': {
                       'text': 'Timestamp'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('index.html', {'weatherchart': cht})