# partial-match-wsgi

Proof of concept Python web service for serving partial match search results.

The goal is to learn more about [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), Python web services, Redis, and Heroku.

# Setup

```
python3 -m pip install --upgrade pip
pip install --user pipenv
pipenv install gunicorn
pipenv install falcon

pipenv shell
gunicorn sample:api
```

# References

* [virtualenv](https://docs.python-guide.org/dev/virtualenvs/)
* [Gunicorn](https://gunicorn.org/)
* [Falcon](http://falconframework.org/)
* [Heroku Redis](https://devcenter.heroku.com/categories/heroku-redis)

