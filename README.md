# Premier-League
4th year project

Includes:
Keras CNN build with a tensorflow backend to identify football crests. Complete with a coreml conversion to be used in an ios app.

Script to download all images of all the premier league players and organise them in folders based on teams.

Django server app providing RestFul service to the ios app on https://github.com/seanjohn85/Elite-Premier-League.
The Django app scraps the internet and uses a premier league api to garther inforamtion on the efl football teams and stores it in an sqllite db. It also makes predictions on the teams next fixture using a Lamba fuction with Poisson Distribution algorithm(https://en.wikipedia.org/wiki/Poisson_distribution)


## Pyhton 2.7

Everthing is developed in Python 2.7 and it is recommended that a new virtual enviroment is set up for each fold using a system such as Anaconda.

All intructions are based on pip install.

# Keras Cnn set Up

open a terminal in a new python 2.7 enviroment and enter the following commands

sudo easy_install pip
pip install Keras==2.0.6 
pip install tensorflow == 1.2.1
pip install -U coremltools
pip install -U scikit-learn
pip install pillow
pip install h5py
pip install matplotlib

**** it is important the version numbers are correct as they are required for coreml 

## Run the CNN model

The CNN model is located at https://github.com/seanjohn85/Premier-League/tree/Downloaded-Images/Python%20model/ConVnet

model/ConVnet in this repo

Open this folder in an editor such as spider 

ensure that the file explorer is pointing to the location to where the images are taht are been feed into the CNN model (in this case its the dataset folder)

run the script CnnMain.py

When the script completes it should produce a new core ml file taht can be added to an iOS project 


# Get The Images

In order to get the image resources for the server set up a new enviroment

pip install requests
pip install beautifulsoup4 
pip install urllib

## Downloading 

To download the images run the save images script.py in the Scapping Folder in this repo.
Then all the images are downloaded they will be stored in 20 folders based on their theme code

Move all the folders to the following folder Server App -  epl - static - images



