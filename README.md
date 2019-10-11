# partial-match-wsgi

Proof of concept Python web service for serving partial match search results.

The goal is to learn more about [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), Python web services, Redis, and Heroku.

## Environment Setup

Install pip3
```
sudo apt update
sudo apt install python3-pip
```

Install pipenv
```
python3 -m pip install --upgrade pip
python3 -m pip install --user pipenv
```

## Project Setup

Install dependencies

```
pipenv install falcon
```

## Testing with Gunicorn

```
pipenv install gunicorn
pipenv shell
gunicorn service:api
wget -qO - http://localhost:8000/match?search=the
```

## Running on Windows

Note that uwsgi and gunicorn (depends on fcntrl) are not available on Windows 10. [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/faq) can be used to get around this limitation. Failing that, a VM solution such as [VirtualBox](https://www.virtualbox.org/) can be used to run Linux or BSD.

## References

Python Web Service Libs

* [Falcon](http://falconframework.org/)
* [Falcon Docs](https://falcon.readthedocs.io/en/stable/)
* [Flask](https://github.com/pallets/flask)
* [Gunicorn](https://gunicorn.org/)
* [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)

Python Dependency Management

* [virtualenv](https://docs.python-guide.org/dev/virtualenvs/)
* [pip freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/)

Data

* [Redis](https://redis.io/)
* [Heroku Redis](https://devcenter.heroku.com/categories/heroku-redis)
* [Python bsddb3](https://pypi.org/project/bsddb3/)
* [MongoDB](https://www.mongodb.com/)
* [List of Every Video Game Ever (v3)](https://pastebin.com/DG1CsVXk)
