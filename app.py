from flask import Flask,render_template,request
import dataset
app= Flask(__name__)
#db = dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4") 
#table= db["momycare_user"]
#table.insert(dict(name="Renan Sa'ed",age=16,subject="English"))
#print(db.tables)
#table.insert(dict(name="Ishan",age=22,subject="programming"))
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
	user_stories=request.form["stories"]
	user_gender=request.form["gender"]
	#table.insert(dict(user_firstname=user_firstname,user_lastname=user_lastname,user_messege=user_messege))
	return render_template("data.html",thefirstname=user_firstname,
							thelastname=user_lastname,themessege=user_Messges,theinquiries=user_inquiries,thestories=user_stories,thegender=user_gender)


if __name__=="__main__":
	app.run(port=50500) 
