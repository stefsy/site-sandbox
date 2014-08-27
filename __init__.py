from flask import Flask

#configure
DEBUG = False #DO NOT USE THIS ON PRODUCTION

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
@app.route("/mm_sketch/")
def mm_sketch():
	return render_template('mm_sketch.html')

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

@app.route("/pyconph2014/")
def pyconph2014():
	return render_template('pyconph2014.html')

@app.route("/ferns/")
def ferns():
	return render_template('ferns.html')

@app.route("/hexbins/")
def hexbins():
	return render_template('hexbins.html')

@app.route("/zoomtree/")
def zoomtree():
	return render_template('zoomtree.html')

@app.route("/git-time-machine")
def timemachine():
	return render_template('timemachine.html')

@app.route("/ds_toolkit/")
def ds_toolkit():
	return render_template('ds_may2014.html')

@app.route("/pandas_devcon/")
def pandas_devcon():
	return render_template('pandas_devcon_july2014.html')

@app.route("/life/")
def womp():
	return "It doesn't make much sense."

@app.route("/wark/")
def wark():
	return "bork bork wark bork"



	#run the app
if __name__ == "__main__":
	app.run()
