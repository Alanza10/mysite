from chartit import DataPool, Chart

def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    tempdata = \
        DataPool(
           series=
            [{'options': {
               'source': Temperatura.objects.all()},
              'terms': [
                'temperatura',
                'pub_date']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(tempdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'temperatura': [
                    'pub_date']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Temperatura Diaria'},
               'xAxis': {
                    'title': {
                       'text': 'Temperatura'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response({'weatherchart': cht})



  

