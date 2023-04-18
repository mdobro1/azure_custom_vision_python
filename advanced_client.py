import requests

base_url = 'https://customvisionclassifiercartoon-prediction.cognitiveservices.azure.com'
endpoint_url = '/customvision/v3.0/Prediction/0fcdbc74-d040-4e80-b6ad-ef819eb32223/classify/iterations/Iteration2/image'
url = base_url + endpoint_url

headers = {
    'Prediction-Key': 'place-your-prediction-key-here',
    'Content-Type': 'application/json'
}

while True:
    url_input = input("Enter the URL of the image to classify (or 'exit' to quit): ")
    if url_input.lower() == 'exit':
        break
    
    data = {
        'Url': url_input
    }
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        predictions = response.json()['predictions']
        if predictions:
            for prediction in predictions:
                tag = prediction['tagName']
                probability = prediction['probability']
                print(f"Tag: {tag}, Probability: {probability}")
        else:
            print("No predictions found for the input image.")
    else:
        print(f"Error: {response.status_code} - {response.reason}")
