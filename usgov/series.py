import os
import csv
import json
import requests
import xmltodict

FRED_BASE_URL = 'https://api.stlouisfed.org/fred/'

def append_fred_token(url):
    token = os.getenv('FRED_TOKEN')
    return f'{url}&api_key={token}'

SERIES_OBS_URL = FRED_BASE_URL + 'series/observations?'
def fred_series(series, file_type=None, realtime_start=None, realtime_end=None, limit=None, offset=None, sort_order=None, observation_start=None, observation_end=None, units=None, frequency=None, aggregation_method=None, output_type=None, vintage_dates=None):
    url = SERIES_OBS_URL + f'series_id={series}'
    url += f'&file_type={file_type}' if file_type else ''
    url += f'&realtime_start={realtime_start}' if realtime_start else ''
    url += f'&realtime_end={realtime_end}' if realtime_end else ''
    url += f'&limit={limit}' if limit else ''
    url += f'&offset={offset}' if offset else ''
    url += f'&sort_order={sort_order}' if sort_order else ''
    url += f'&observation_start={observation_start}' if observation_start else ''
    url += f'&observation_end={observation_end}' if observation_end else ''
    url += f'&units={units}' if units else ''
    url += f'&frequency={frequency}' if frequency else ''
    url += f'&aggregation_method={aggregation_method}' if aggregation_method else ''
    url += f'&output_type={output_type}' if output_type else ''
    url += f'&vintage_dates={vintage_dates}' if vintage_dates else ''
    url = append_fred_token(url)
    result = requests.get(url)
    return result

print(fred_series('GNPCA', 'json'))
