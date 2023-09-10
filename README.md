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


## We will first use google colab to train the model 


- Google Drive URL: [https://drive.google.com/drive/folders/16qo-WE2glfSrz5gEDGDMzCi7wLKpUeAu?usp=sharing]


- YOLO GitHub Repository: [https://github.com/ultralytics/yolov5]


- URL to Clone Repository: [https://github.com/ultralytics/yolov5.git]



## Later we will use azure to train and deploy the model. 


-reference [https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-train-model?view=azureml-api-2]

