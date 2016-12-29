import feedparser
from datetime import datetime
from flask import Flask, request
from werkzeug.contrib.atom import AtomFeed


def feed_entries():
    results = []

    d = feedparser.parse('http://treasurydirect.gov/NP/debt/rss')

    for entry in d.entries:
        # The data is published the next business day, but that date is the
        # date to show, not the "close of business" date which the value is for.
        entry_pub_date = \
            datetime.strptime(entry['published'], '%a, %d %b %Y %H:%M:%S GMT')
        # Parse content, pulling the number value for 'Public Debt Outstanding'
        # which happens to be the last part.    E.g.,
        # "Total Public Debt Outstanding:&lt;/em&gt; 19,443,266,164,413.41"
        formatted_num_val = entry['content'][0]['value'].split()[-1]
        entry_text = \
            "Total U.S. National Public Debt: ${}".format(formatted_num_val)
        results.append({
            "pubDate": entry_pub_date,
            "entryTitle": "{:%Y-%m-%d}".format(entry_pub_date),
            "entryText": entry_text})

    return results


app = Flask(__name__)


@app.route('/feed/', methods=['GET'])
@app.route('/rss/', methods=['GET'])
def feed():
    feed = \
        AtomFeed('Recent entries', feed_url=request.url, url=request.url_root)
    for entry in feed_entries():
        feed.add(
            entry["entryTitle"], entry["entryText"],
            id='https://treasurydirect.gov/{:%Y%m%d%H%M%S}'.format(entry["pubDate"]),
            content_type='text',
            author='U.S. Treasury RSS Feed treasurydirect.gov/NP/debt/current',
            url='http://treasurydirect.gov/NP/debt/current',
            updated=entry["pubDate"],
            published=entry["pubDate"])
    return feed.get_response()
