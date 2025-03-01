import requests

def create_api(name, job):
    url = "https://reqres.in/api/users"
    payload = {
        "name" : name,
        "job" : job
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            json_response = response.json()
            if "id" in json_response and "createdAt" in json_response:
                print("✅ API is healthy!")
            else:
                print("⚠️ API responded, but missing expected fields!")
                return False
        else:
            print(f"❌ API is not healthy! Status code: {response.status_code}")
            return False
    except requests.RequestException as error:
        print(f"❌ Error occurred: {error}")
        return False