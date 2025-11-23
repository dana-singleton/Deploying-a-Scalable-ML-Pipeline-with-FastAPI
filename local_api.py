import requests

# Completed: send a GET using the URL http://127.0.0.1:8000
r = requests.get("http://127.0.0.1:8000/")  # Code updated

# Completed: print the status code
print("GET / status code:", r.status_code)
# Completed: print the welcome message
# r.json() will be {"message": "..."}
print("GET / response:", r.json())


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Completed: send a POST using the data above
r = requests.post("http://127.0.0.1:8000/data/", json=data)  # code updated

# Completed: print the status code
print("POST /data/ status code:", r.status_code)
# Completed: print the result
print("POST /data/ response:", r.json())
