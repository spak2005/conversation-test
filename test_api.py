import requests
import json

def test_process_endpoint():
    url = "http://localhost:8080/process"
    payload = {"message": "Hello, how are you?"}
    headers = {"Content-Type": "application/json"}
    
    try:
        print("Sending request to API...")
        response = requests.post(url, json=payload, headers=headers)
        
        print(f"Status code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Success! API responded with:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"❌ Exception occurred: {str(e)}")

if __name__ == "__main__":
    test_process_endpoint() 