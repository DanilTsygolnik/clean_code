import requests


my_url = "https://google.com"
file_name = "parse_result.html"
response = requests.get(my_url)
with open(file_name, 'w') as file:
    file.write(response.text)
