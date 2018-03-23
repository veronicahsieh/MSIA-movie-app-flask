# Movies Revenue Prediction App

Web application for analytics value chain class

### Project Overview
The goal of this project is to build a movie prediction model that enable users to enter movie information and see an estimated box office revenue. Due to the nature of the dataset (categorical variables & continuous variables with different scaling), a tree based model was used to generate the revenue predictions.

### Team Members:
* Product Owner: Varun Gupta
* QA: Will Song
* Developer: Veronica Hsieh

### Package Requirements

* Refer to ```requirements.txt```

### Directory Structure

```
├── _README.md 
├── _develop                        # Folder with all the necessary files for data cleaning & model creation
|   └── genres_map.py 
|   └── movies_data_cleaning.py
|   └── make_model.py          
|   └── predict.py                  # Script that takes user input to generate movie revenue prediction
|   └── test.py                     # Script with unit testing for app
|   └── movie_tree.pkl          
|   └── notebooks                   # Jupyter notebooks with initial exploratory data analysis and model building

├── _requirements.txt               # Required packages to run app
├── _msiapp 
|   ├── forms.py
|   └── models.py
|   └── __init__.py
|   └── static                      # Images used for web app 
|   └── templates                   # HTML pages

├── _docs                           # Documentation around data cleaning, model building, and unit-testing scripts
├── _create_db.py                   # Script to instantiate database
├── genres_map.csv                  # File used to map user input to genre code for model predictions
├── _config.py                      # Configuration for AWS and RDS instance
├── movieapp_presentation.pdf       # Final presentation for demo of web app 
└── application.log                 # Logging from application.py
```

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

* 3a. Download "movies_metadata.csv" dataset from the [Kaggle site](https://www.kaggle.com/rounakbanik/the-movies-dataset/data)

* 3b. Run scripts to clean data and create model. Note - ```clean_movies.csv``` is the name of the csv output from ```movies_data_cleaning.py```

```
$ cd develop
$ python movies_data_cleaning.py movies_metadata.csv
$ python make_model.py clean_movies.csv
```
> **Additional Documentation:** To learn more about the specific functions for each script, navigate to ```docs/_build/html```

4. Run application; note create_db.py is a one-time setup only

```
$ cd ..
$ python create_db.py
$ python application.py
```
### Unit Tests & Logging
* Unit tests checked that the output the data cleaning functions and user-entered data from the HTML form returned the proper output - all unit tests can be found in ```test.py```
* To run the unit tests:
```
$ cd develop
$ pytest test.py
```
* Logging was performed at the application level - see example ```application.log``` 

### Project Management
Development of this project was managed in Pivotal Tracker. Link to this specific project can be found 
[here](https://www.pivotaltracker.com/n/projects/2143653).

### Final Presentation
Demo of the final web app was accompanied by 
[this presentation](https://github.com/vhsieh920/MSIA_movie_webapp/blob/web_page/movieapp_presentation.pdf).
