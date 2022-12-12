import requests 

def get_users():
	response = requests.get("https://reqres.in/api/users?page=2")
	return response.json()