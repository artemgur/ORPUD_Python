import requests
import bs4


def print_forecast(forecast_header, forecast_date, forecast_temp_day, forecast_temp_night, forecast_condition):
    print(f'{forecast_header:>7} {forecast_date} Днем: {forecast_temp_day:>3} Ночью: {forecast_temp_night:>3} {forecast_condition}')


website = requests.get('https://yandex.ru/pogoda/').text
website_bs = bs4.BeautifulSoup(website, 'html.parser')
for forecast_card in website_bs.select('.forecast-briefly__day-link')[1:8]:
    forecast_header = forecast_card.select_one('.forecast-briefly__name').text
    forecast_date = forecast_card.select_one('.forecast-briefly__date').attrs['datetime'].split()[0]
    forecast_temp_day = forecast_card.select_one('.forecast-briefly__temp_day')\
                                 .select_one('.temp__value_with-unit').text
    forecast_temp_night = forecast_card.select_one('.forecast-briefly__temp_night')\
                                 .select_one('.temp__value_with-unit').text
    forecast_condition = forecast_card.select_one('.forecast-briefly__condition').text
    print_forecast(forecast_header, forecast_date, forecast_temp_day, forecast_temp_night, forecast_condition)
