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



@app.route("/form_response",methods=["POST"])
def form_res():
	user_firstname=request.form["firstname"]
	user_lastname=request.form["lastname"]
	user_Messges=request.form["messege"]
	user_inquiries=request.form["inquiries"]
	user_gender=request.form["gender"]
	return render_template("data.html",thefirstname=user_firstname,
							thelastname=user_lastname,themessege=user_Messges,thegender=user_gender,theinquiries="user_inquiries")


if __name__=="__main__":
	app.run(port=50500) 
