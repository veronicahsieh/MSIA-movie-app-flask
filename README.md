# Movies Revenue Prediction App

Web application for analytics value chain class

### Project Overview
The goal of this project is to build a movie prediction model that enable users to enter movie information and be able to see the estimated box office revenue.

### Package Requirements

*see requirements.txt

### Directory Structure


### Steps to Launch App
To get the app running locally:

1. Create a new virtual environment (assume environment name is 'msiapp')
```
$ conda create -n msiapp python=3
```

2. Navigate to the project directory, launch the virtual environment, and load the required packages

```
$ cd MSIA-webapp
$ source activate msiapp
$ pip install -r requirements.txt
```

3. Data Processing & Model Development

3a. Download "movies_metadata.csv" dataset from the Kaggle site

3b. Run scripts to cleanup data and create model

```
$ cd develop
$ python movies_data_cleaning.py
$ python make_model.py
```
4. Run application

```
$ cd ..
$ python create_db.py (one-time setup only)
$ python application.py
```
### Unit Tests & Logging
* Unit tests checked that the output the data cleaning functions and user-entered data from the HTML form returned the proper output - all unit tests can be found in test.py
* Logging was performed - examples can be in found in the "application.log" file

### Project Management
Development of this project was tracked in Pivotal Tracker. Link to this specific project can be found [here] (https://www.pivotaltracker.com/n/projects/2143653).
