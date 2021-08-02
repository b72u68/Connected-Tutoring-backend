# Connected Tutoring Backend

## Setup

Git clone this repository to your local machine

```bash
git clone https://github.com/b72u68/Connected-Tutoring-backend
```

Go to the cloned repository and install the required libraries in `requirements.txt`
(This project uses __Python 3__ so be sure to have __Python 3__ in your local machine).

```bash
pip install -r requirements.txt
```

## Start the development server

Run the following command

```bash
python app.py
```

or 

```bash
export FLASK_DEBUG=True
flask run --host=0.0.0.0
```
## Structure

```
Connected-Tutoring-backend
  |-- api
      |-- __init__.py
      |-- another api files
  |-- models
      |-- __init__.py
      |-- another models files
  |-- utils
  |-- inputs
  app.py
  README.md
  .gitignore
  requirements.txt
```
  
`api`: project API and routes. 

`models`: files or functions that related to database, tasks, workers, etc.

`utils`:  utility functions and tools.

`inputs`: input format and validation.
