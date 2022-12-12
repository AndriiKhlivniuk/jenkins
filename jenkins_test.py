import requests

headers={

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

data ={
  "id": 0,
  "category": {
    "id": 12,
    "name": "dog"
  },
  "name": "puppy",
  "photoUrls": [
    "none"
  ],
  "tags": [
    {
      "id": 0,
      "name": "newdog"
    }
  ],
  "status": "available"
}

response = requests.post("https://petstore.swagger.io/v2/pet", json = data, headers = headers)
pet_id = response.json()["id"]