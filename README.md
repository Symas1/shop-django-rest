# How to run the project?
## Run the following commands in your command line step-by-step
```sh
$ git clone https://github.com/Symas1/shop-django-rest.git
$ cd shop-django-rest
$ set PIPENV_VENV_IN_PROJECT=1
$ pipenv install
$ pipenv shell
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py loadtestdata shop.Category:20 shop.Item:100
$ python manage.py runserver
```
# Available URLs
- http://localhost:8000/users/
- http://localhost:8000/users/<int:pk>
- http://localhost:8000/items/
- http://localhost:8000/items/<int:pk>
- http://localhost:8000/categories/
- http://localhost:8000/categories/<int:pk>
### Registration/Authorization URLs
- http://localhost:8000/login/
- http://localhost:8000/logout/
- http://localhost:8000/registration/