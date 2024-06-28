import requests

def make_prediction():
    # Define the API endpoint
    url = 'http://localhost:5001/predict'

    # Define the headers
    headers = {'Content-Type': 'application/json'}

    # Define the data payload
    data = {
        "features": {
            "sbp": 129.0, 
            "dbp": 78.0, 
            "bmi": 39.0, 
            "trig": 187.0, 
            "hdl": 54.0, 
            "total_chol": 113.0, 
            "ldl": 22.0
        }
    }

    try:
        # Send a POST request
        response = requests.post(url, json=data, headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            # Print the response
            print(response.json())
        else:
            print(f"Failed to retrieve data: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    make_prediction()
