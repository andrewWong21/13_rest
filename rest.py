from flask import Flask, render_template
import urllib2, json

rest_api = Flask(__name__)

@rest_api.route("/")
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=susxL6ipI7cwKgM49WOqU8nCyM8kO5WrYhwkhORO")
    d=json.loads(u.read())
    return render_template("nasa.html", img = d['url'], desc = d['explanation'], title = d['title'])
    
if __name__ == "__main__":
    rest_api.debug = True
    rest_api.run()