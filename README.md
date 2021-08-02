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

If you haven't had `pip` yet, follow the instruction in this [link](https://github.com/pypa/pip)
to install `pip`.

Though it is not required, we encouraged you to use virtual environment for package management in this project. 
If you decide to try virtual environment for python, follow this [link](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).

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
## Project structure

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

## Future plan for deployment

Might use Docker and deploy on AWS.
