import requests 
import logging

logging.basicConfig(level=logging.INFO, filename='results.log', encoding='utf-8')

def get_users():
	response = requests.get("https://reqres.in/api/users?page=2")
	return response.json()

def api_requests():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    logging.info(str(response.json()))
    print(response.json())

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    logging.info(str(response.json()))
    print(response.json())

    response = requests.get("https://jsonplaceholder.typicode.com/posts/2/comments")
    logging.info(str(response.json()))
    print(response.json())

api_requests()
