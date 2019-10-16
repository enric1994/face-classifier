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
## Output

For each face, the score of the 7 emotions (angry, disgust, fear, happy, sad,surprise, neutral), gender scores and spatial information

```
{
  "results": [
    {
      "angry": "0.00155284", 
      "disgust": "3.50381e-06", 
      "fear": "1.85862e-05", 
      "gender_prediction_female": "0.023314", 
      "gender_prediction_male": "0.976686", 
      "happy": "0.988147", 
      "neutral": "0.00960139", 
      "sad": "0.000135331", 
      "surprise": "0.000541203", 
      "x1": "369", 
      "x2": "429", 
      "y1": "427", 
      "y2": "487"
    }, 
    {
      "angry": "0.00293696", 
      "disgust": "0.000161379", 
      "fear": "0.00637031", 
      "gender_prediction_female": "0.0162435", 
      "gender_prediction_male": "0.983757", 
      "happy": "0.326245", 
      "neutral": "0.652848", 
      "sad": "0.0109506", 
      "surprise": "0.000487321", 
      "x1": "647", 
      "x2": "700", 
      "y1": "494", 
      "y2": "547"
    }, 
    {
      "angry": "0.00323381", 
      "disgust": "5.36696e-05", 
      "fear": "0.00129802", 
      "gender_prediction_female": "0.221083", 
      "gender_prediction_male": "0.778917", 
      "happy": "0.782257", 
      "neutral": "0.188827", 
      "sad": "0.0237087", 
      "surprise": "0.000621749", 
      "x1": "244", 
      "x2": "305", 
      "y1": "468", 
      "y2": "529"
    }, 
    {
      "angry": "0.00110312", 
      "disgust": "1.50307e-07", 
      "fear": "0.00111691", 
      "gender_prediction_female": "0.0271439", 
      "gender_prediction_male": "0.972856", 
      "happy": "0.879081", 
      "neutral": "0.11332", 
      "sad": "0.00459207", 
      "surprise": "0.000786571", 
      "x1": "791", 
      "x2": "852", 
      "y1": "489", 
      "y2": "550"
    }, 
    {
      "angry": "0.0046174", 
      "disgust": "0.00198305", 
      "fear": "0.0176383", 
      "gender_prediction_female": "0.210827", 
      "gender_prediction_male": "0.789173", 
      "happy": "0.93071", 
      "neutral": "0.0166545", 
      "sad": "0.00715159", 
      "surprise": "0.0212453", 
      "x1": "494", 
      "x2": "549", 
      "y1": "497", 
      "y2": "552"
    }
  ]
}

```
