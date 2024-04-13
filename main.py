import pandas
import requests
from requests_tor import RequestsTor
import searchutils

rt = RequestsTor(autochange_id=10)
rr = requests

df = pandas.read_excel('data.xlsx')
for r in df['Домен']:
    print(r, searchutils.get_inn(r, rr))

