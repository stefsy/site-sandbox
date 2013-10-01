from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, _app_ctx_stack

#configure
DEBUG = True #DO NOT USE THIS ON PRODUCTION
SECRET_KEY = 'development key'

#actual app creation
app = Flask(__name__)

# loading the configuration from the all caps chunk above
# usually it's a better idea to load it from a file using from_envvar()
app.config.from_object(__name__) 


#static empty pages
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

@app.route("/life/")
def womp():
	return "It doesn't make much sense."


	#run the application
if __name__ == "__main__":
	app.run()


