import requests
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
parser = ArgumentParser(prog = 'python hkweather.py',
                        description = 'Hong Kong Weather Forecast香港天氣預報',
                        formatter_class = ArgumentDefaultsHelpFormatter)
parser.add_argument("-l", "--language", help="Language (en, tc)")
args = vars(parser.parse_args())

def gen_report():
    print("Time:", forecast['updateTime'])
    print("Description:", forecast['forecastDesc'])    
    print("Outlook:", forecast['outlook'])
    # print("Summary:", forecast)
    # for i in forecast.items():
    #     print(i)

try:
    language = args["language"]
    response = requests.get(f"https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc")
    forecast = response.json()
    gen_report()
except:
    print("usage: python hkweather.py [-h] [-l LANGUAGE]")