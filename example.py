import requests

# Load multiple files
# image=dict(img=open('images/test_image.jpg', encoding="utf8"))

image = {'img': open('images/test_image.jpg', 'rb')}


# Send files and parameters
response = requests.post('http://localhost:8084/classifyImage',
    files=image)

print(response.text)