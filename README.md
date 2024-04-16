# ARSO weather forecast

[Home Assistant](https://home-assistant.io/) sensor for [ARSO Weather Forecast](https://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl/forecast_si/index.html) which pulls data from ARSO ([Slovenian Environment Agency](https://www.arso.gov.si/en/)) in XML format.

Weather Forecast is for *Ljubljana in okolica* for morning and afternoon next day (2 day forecast) which is momentary the most precise weather forecast.

Template example for use of sensor:
````python
{% for i in state_attr('sensor.arso_forecast','metData') %}
Time/Day: {{ i['valid'] }} {{ i['valid_day'] }} ({{ i['valid_daypart'] }})
Temperatura: {{ i['t'] }} {{ i['t_var_unit'] }}
Hitrost vetra: {{ i['ff_value'] }} {{ i['ff_var_unit'] }}
Padavine: {{ i['rr_decodeText'] }}
Vremenska napoved: {{ i['nn_shortText'] }} ({{ i['wwsyn_shortText'] }})
{% endfor %}
````
Template output:

![plot](./img/Zajeta%20slika-arso-forecast-template.PNG)