import requests


user_message = "Create an event titled 'Meeting with project team' for tomorrow at 10 AM. Use the calendar tool."

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/972c69ba-120f-454f-acda-ee52000e4b41"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])
