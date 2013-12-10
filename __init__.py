from flask import Flask, request, session, g, redirect, url_for, render_template


#configure
DEBUG = True #DO NOT USE THIS ON PRODUCTION
SECRET_KEY = 'development key'

#actual app creation
app = Flask(__name__)

# loading the configuration from the all caps chunk above
# usually it's a better idea to load it from a file using from_envvar()
app.config.from_object(__name__)

#static pages
@app.route("/")
def homepage():
	return render_template('homepage.html')

#route generates URLS
@app.route("/learnbydoing/")
def learnbydoing():
 	return render_template('learnbydoing.html') 

@app.route("/rects/")
def rects():
 	return render_template('rects.html')

@app.route("/nodes/")
def nodes():
 	return render_template('nodes.html')

@app.route("/sort_bars/")
def sort_bars():
 	return render_template('sort_bars.html')

@app.route("/channelstats/")
def channelstats():
 	return render_template('channelstats.html')

@app.route("/donuts/")
def donuts():
	return render_template('donuts.html')

@app.route("/life/")
def womp():
	return "It doesn't make much sense."

@app.route("/multiline/")
def linechart():
	return render_template('multiline.html')

@app.route("/easeofbusinessph/")
def easeph():
	return render_template('easeofbusinessph.html')

@app.route("/reliefpatrol/")
def patrolph():
	return render_template('reliefpatrol.html')

@app.route("/mapschools/")
def mapschools():
	return render_template('mapschools.html')

@app.route("/test/")
def test():
	return "works"

	#run the app
if __name__ == "__main__":
	app.run()

