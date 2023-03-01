# dockerize-stackoverflow-fastapi
This is a python application that leverages on Stackoverflow api to get all questions and answers on Stackoveflow. 


## Project scaffold

* Makefile
* requirements.txt
* source code files

## Command Line Tool
* add fire to your requirments.txt
* create a new file `touch stackquestions.py`
* import the logic function to this file
* import fire
* Make the file executable `chmod +x stackquestions.py`
* Read the documentation `./stackquestions.py --help`
* Run the file ` ./stackquestions.py --name 'python' `

## Move to Production
* Build Dockerfile to containerize it
* Build Web app `FastAPI`
* Push to Cloud `AWS Cloud 9` -  `App runner`