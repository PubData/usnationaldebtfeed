# usnationaldebtfeed
Syndiated Feed (Atom) of the recent U.S. National Public Debt

## Synopsis
The U.S. Treasury publishes a feed (RSS) daily with various metrics regarding the debt.

This replicates that feed (Atom), but publishes just the Total Public Debt number.


## Installation
This is a Flask app (Python3).

``` sh
$ cd [your workspace]
$ git clone https://github.com/pubdata/usnationaldebtfeed.git
$ cd usnationaldebtfeed
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install --upgrade setuptools
$ pip install -r requirements.txt
``` 

Further deploy instructions will vary based on production system requirements.

For testing, use gunicorn:

``` sh
$ gunicorn usnationaldebtfeed:app
``` 

From a browser, access the app using: [http://localhost:8000/feed](http://localhost:8000/feed)

## Example

This is running at [DebtToThePenny.com/feed](https://www.debttothepenny.com/feed), which is used to publish the [@DebtToThePenny](https://twitter.com/debttothepenny) Twitter feed.

## License

MIT
