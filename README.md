# Deployment TBD


# OpenCV_Streamlit_APP

Try to make an online application with Streamlit App combined with modern vision ML technology, YOLO, OpenCV. Deploy it on Azure with CI/CD. 


## Running Locally  

- create virtual environment in current folder

    virtualenv .venv

- start virtual environment 

    source .venv/bin/activate

- deactivate virtual environment

    deactivate

## Automatically go to virtual vironment in VSCode:

- first setting all up and activate your virtual environment

- then choose file --> Preference -->settings  select workspace tab then click open setting json icon from top right

- put this code in


    {
        "python.terminal.activateEnvInCurrentTerminal": true
    }


- see reference [https://www.youtube.com/watch?v=g7bg2ADfx4c&ab_channel=JohnSolly]


## Streamlit 

- I include stream tutorial folder called 3_Streamlit_crash_course

- Streamlit treats multiple apps as pages, you need to make a fold named "pages" exactly to activate this feature. also name 1_,2_,--- infront of each page name so it will detect sequence. Remember that

see reference in udemy [https://www.udemy.com/course/yolo-custom-object-detection/learn/lecture/33903494#notes]

## Web Video Streaming

- you need to install webrtc library to work on video stream project

- streamlit has streamlit-webrtc so you just need to install it from requirement txt.

- Reference [https://github.com/whitphx/streamlit-webrtc]


## We will first use google colab to train the model 


- Google Drive URL: [https://drive.google.com/drive/folders/16qo-WE2glfSrz5gEDGDMzCi7wLKpUeAu?usp=sharing]


- YOLO GitHub Repository: [https://github.com/ultralytics/yolov5]


- URL to Clone Repository: [https://github.com/ultralytics/yolov5.git]



## Later we will use azure to train and deploy the model. 


-reference [https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-train-model?view=azureml-api-2]

-webrtc may not work in this environment due the security on the network. but still can deploy for image object detection.

    HTTPS
    streamlit-webrtc uses getUserMedia() API to access local webcams, and this method does not work in an insecure context.

    This document says

    A secure context is, in short, a page loaded using HTTPS or the file:/// URL scheme, or a page loaded from localhost.

    So, when hosting your app on a remote server, it must be served via HTTPS.

