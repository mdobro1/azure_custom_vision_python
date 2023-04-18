import os
import requests

base_url = 'https://customvisionclassifiercartoon-prediction.cognitiveservices.azure.com'
endpoint_url = '/customvision/v3.0/Prediction/0fcdbc74-d040-4e80-b6ad-ef819eb32223/classify/iterations/Iteration2/image'
url = base_url + endpoint_url

headers = {
    'Prediction-Key': 'place-your-prediction-key-here',
    'Content-Type': 'application/octet-stream'
}

while True:
    dir_path = input("Enter the directory path of the images to classify (or 'exit' to quit): ")
    if dir_path.lower() == 'exit':
        break
    
    file_paths = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    file_count = len(file_paths)
    file_index = 0
    
    while file_index < file_count:
        file_path = file_paths[file_index]
        with open(file_path, 'rb') as file:
            print(f"Classifying image: {file_path}")
            data = file.read()
        
        response = requests.post(url, headers=headers, data=data)
        if response.ok:
            predictions = response.json()['predictions']
            if predictions:
                for prediction in predictions:
                    tag = prediction['tagName']
                    probability = prediction['probability']
                    print(f"Tag: {tag}, Probability: {probability}")
            else:
                print(f"No predictions found for the image: {file_path}")
        else:
            print(f"Error: {response.status_code} - {response.reason}")
        
        file_index += 1
        if file_index < file_count:
            next_file_input = input(f"{file_index}/{file_count} images classified. Enter 'n' to classify next image, 'exit' to quit: ")
            if next_file_input.lower() == 'exit':
                break

    if file_index >= file_count:
        print("All images classified.")
        break