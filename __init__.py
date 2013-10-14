from flask import Flask, request, session, g, redirect, url_for, render_template

#importing api keys
keyfile = open("dev_keys/yt_v3.txt","r")
yt_key = keyfile.readline()
keyfile.close()

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

#route generates nice URLS
@app.route("/rects/")
def rects():
 	return render_template('rects.html')

@app.route("/nodes/")
def nodes():
 	return render_template('nodes.html')

@app.route("/sort_bars/")
def sort_bars():
 	return render_template('sort_bars.html')

@app.route("/donuts/")
def donuts():
 	return render_template('donuts.html',yt_key=yt_key)

@app.route("/learnbydoing/")
def learnbydoing():
 	return render_template('learnbydoing.html') 	

@app.route("/life/")
def womp():
	return "It doesn't make much sense."

	#run the app
if __name__ == "__main__":
	app.run()


