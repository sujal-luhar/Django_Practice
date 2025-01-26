# You have to run the server of drinks project/app by 
# running `python manage.py runserver` 

import requests

response = requests.get("http://127.0.0.1:8000/drinks")
print(response.json())