from flask import Flask,render_template,request
app= Flask(__name__)


@app.route("/")
def load_page():
	return render_template ("index.html")

@app.route("/feeding")
def feeding_page():
	return render_template ("feeding.html")


@app.route("/development")
def development_page():
	return render_template ("development.html")

@app.route("/contact")
def contact():
	return render_template ("contact.html")



if __name__=="__main__":
	app.run(port=5050) 
