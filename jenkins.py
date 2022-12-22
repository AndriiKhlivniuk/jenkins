import requests 
import logging

logging.basicConfig(level=logging.INFO, filename='results.log', encoding='utf-8')

def get_users():
	response = requests.get("https://reqres.in/api/users?page=2")
	return response.json()

def api_requests():
	response = requests.get("https://reqres.in/api/users/2")
	logging.info(str(response.json()))
	print(response.json())

	data = {
	    "name": "John",
	    "job": "Architect"
	}
	
	response = requests.post("https://reqres.in/api/users", json = data)
	logging.info(str(response.json()))
	print(response.json())
	data = {
	    "name": "John",
	    "job": "Programmer"
	}
	response = requests.patch("https://reqres.in/api/users/2", json = data)
	logging.info(str(response.json()))
	print(response.json())

	response = requests.get("https://reqres.in/api/users")
	logging.info(str(response.json()))
	print(response.json())

api_requests()
