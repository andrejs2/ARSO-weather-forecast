import requests
from bs4 import BeautifulSoup

# Fetch XML data
url = "https://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl/fcast_SI_OSREDNJESLOVENSKA_latest.xml"
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse XML content
    soup = BeautifulSoup(response.content, 'xml')

    # Find all metData elements
    met_data_list = soup.find_all('metData')

    # Iterate over each metData element
    for met_data in met_data_list:
        # Extract time or day information
        valid_day = met_data.find('valid_day').text
        valid_daypart = met_data.find('valid_daypart').text
        valid_time = met_data.find('valid').text
        
        # Extract temperature information
        t_var_desc = met_data.find('t_var_desc').text
        t_var_unit = met_data.find('t_var_unit').text
        t = met_data.find('t').text
        
        # Extract wind speed information
        ff_var_desc = met_data.find('ff_var_desc').text
        ff_var_unit = met_data.find('ff_var_unit').text
        ff_value = met_data.find('ff_value').text
        
        # Extract precipitation information
        rr_decode_text = met_data.find('rr_decodeText').text
        
        # Extract weather forecast information
        nn_short_text = met_data.find('nn_shortText').text
        wwsyn_short_text = met_data.find('wwsyn_shortText').text

        # Print the information
        print(f"Time/Day: {valid_time} {valid_day} ({valid_daypart})")
        print(f"Temperatura: {t} {t_var_unit}")
        print(f"Hitrost vetra: {ff_value} {ff_var_unit}")
        print(f"Padavine: {rr_decode_text}")
        print(f"Vremenska napoved: {nn_short_text} ({wwsyn_short_text})")
        print()  # Print newline after each metData element

else:
    print("Failed to fetch XML data from the URL.")
