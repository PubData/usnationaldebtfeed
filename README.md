# usnationaldebtrss
Feed of the recent U.S. Public Debt

## Synopsis
The U.S. Treasury publishes an RSS feed daily with various metrics regarding the debt.

This replicates that feed, but publishes just the Total Public Debt number.


## Installation
This is a Flask app (Python3).

``` sh
$ cd [your workspace]
$ git clone https://github.com/pubdata/usnationaldebtrss.git
$ cd usnationaldebtrss
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
``` 

Further deploy instructions will vary based on production system requirements.

For testing, use gunicorn:

``` sh
$ gunicorn usnationaldebtrss:app
``` 

From a browser, access the app using: [http://localhost:8000/rss](http://localhost:8000/rss)

## Example

This is running at [DebtToThePenny.com/rss](http://www.debttothepenny.com/rss), which is used to publish the [@DebtToThePenny](https://twitter.com/debttothepenny) Twitter feed.

## License

MIT
