  import requests

# Define the URL
url = 'https://httpbin.org/post'

# Define the data to be sent in the POST request
data = {
    'key1': 'value1',
    'key2': 'value2'
}

try:
    # Make the POST request
    response = requests.post(url, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request was successful.")
    else:
        print(f"Received response with status code: {response.status_code}")

    # Print the raw response text
    print("Response Text:")
    print("Response.text:")
except:
    print("Response Headers:")
    if response.status_code ==333:
        print("Response was not successful.")
    for response in response.json():
        print(response)
