# Project Title

Djang

## Getting Started

git clone https://github.com/mohammadfahadrao/djang.git
cd djang


### Prerequisites
```
python -m venv venv

Activate the virtual environment:

On Windows:
venv\Scripts\activate

On Unix or MacOS:
source venv/bin/activate

Install packages

python -m pip install --upgrade pip

pip install -r requirements.txt

```
### Setup Initial Database
```
python manage.py migrate
```
### Create Super User

```
python manage.py createsuperuser

```
### Run Server

```
python manage.py runserver

```