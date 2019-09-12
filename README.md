Original repository: https://github.com/oarriaga/face_classification


## Usage

1. Download and start the face-classifier container:

`git clone https://github.com/enric1994/face-classifier.git`

`cd face-classifier/docker`

`make run`


2. Use the following code to send images to the container and receive the features:

```
import requests

# Load multiple files
# image=dict(img=open('images/test_image.jpg', encoding="utf8"))

image = {'img': open('image_path_goes_here', 'rb')}


# Send files and parameters
response = requests.post('http://localhost:8084/classifyImage',
    files=image)

print(response.text)
```
