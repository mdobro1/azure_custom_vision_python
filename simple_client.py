import requests

base_url = 'https://customvisionclassifiercartoon-prediction.cognitiveservices.azure.com'
endpoint_url = '/customvision/v3.0/Prediction/0fcdbc74-d040-4e80-b6ad-ef819eb32223/classify/iterations/Iteration2/image'
url = base_url + endpoint_url

headers = {
    'Prediction-Key': 'place-your-prediction-key-here',
    'Content-Type': 'application/json'
}
data = {
    'Url': 'https://i.pinimg.com/474x/57/59/28/575928a72613c7d4a4e751c315b28888--lisa-simpson-female-characters.jpg'
}
response = requests.post(url, headers=headers, json=data)
print(response.json())