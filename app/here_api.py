import requests


# url = r'https://geocode.search.hereapi.com/v1/geocode?q=5+Rue+Daunou%2C+75000+Paris%2C+France'
# api_key = '9HXnYe3FieeH_k-QYuPTquU600_UXKWXU7iD-8wjfTg'
# response = requests.get(url)

api_key = 'gzZneSuZsB0WMAkBY465pY4pXrycgBC3n2I3AF2_J3s'
url = rf'https://geocoder.ls.hereapi.com/search/6.2/geocode.json?languages=en-UK&maxresults=4&searchtext=Sellindge&apiKey={api_key}'
response = requests.get(url)
print(response.content)

