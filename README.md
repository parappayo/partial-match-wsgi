# partial-match-wsgi

Proof of concept Python web service for serving partial match search results.

The goal is to learn more about [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), Python web services, Redis, and Heroku.

# Setup

Install pip3
```
sudo apt update
sudo apt install python3-pip
```

Install pipenv
```
python3 -m pip install --upgrade pip
pip install --user pipenv
```

Install dependencies
```
pipenv install gunicorn
pipenv install falcon
```

Run the service
```
pipenv shell
gunicorn service:api
```

Test the service
```
wget -qO - http://localhost:8000/match
```

# References

* [virtualenv](https://docs.python-guide.org/dev/virtualenvs/)
* [Gunicorn](https://gunicorn.org/)
* [Falcon](http://falconframework.org/)
* [Heroku Redis](https://devcenter.heroku.com/categories/heroku-redis)
* [List of Every Video Game Ever (v3)](https://pastebin.com/DG1CsVXk)
