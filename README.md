# Connected Tutoring Backend

## Setup

Git clone this repository to your local machine

```git clone https://github.com/b72u68/Connected-Tutoring-backend```

Go to the cloned repository and install the required libraries in `requirements.txt`. 
(This project uses `Python 3` so be sure to have `Python 3` in your local machine)

```pip install -r requirements.txt```

## Start the development server

Run the following command

```python app.py```

## Structure

```
Connected-Tutoring-backend
  |-- api
      |-- __init__.py
      |-- another api files
  |-- models
      |-- __init__.py
      |-- another models files
  app.py
  README.md
  .gitignore
  requirements.txt
```
  
Project API and routes will be contained in `api` directory. 

Any files or functions that related to database, tasks, workers, etc. will be placed in `models`.
