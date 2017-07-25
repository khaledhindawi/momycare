from flask import Flask,render_template,request
import dataset
<<<<<<< HEAD
import random
app= Flask(__name__)
db = dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4") 
table= db["momycare_user"]
=======
app= Flask(__name__)
#db = dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4") 
#table= db["momycare_user"]
>>>>>>> bf1fe3c5ed824553e0e6b795c4668cab6ed93231
#table.insert(dict(name="Renan Sa'ed",age=16,subject="English"))
#print(db.tables)
#table.insert(dict(name="Ishan",age=22,subject="programming"))
@app.route("/")
def load_page():
	# return render_template ("index.html")
	quotes=[" Remember a name is a lifetime gift. Make sure that it will wear well",
	"Don't expect your baby to eat much solid food at first; a teaspoonful or two, a couple of times a day, is a lot.","Taking your baby outside for an afternoon walk might help her sleep better at night.",
	"Do not clutter the nursery; there should be a place for play.","For a baby, things that aren't toys are often as much fun as toys."]
	return render_template("index.html",Advice=random.choice(quotes))


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

	
	user_stories=request.form["stories"]
	user_gender=request.form["gender"]
	table.insert(dict(user_firstname=user_firstname,user_lastname=user_lastname,user_messege=user_messege,thestories=user_stories,thegender=user_gender))

	return render_template("data.html")

	
@app.route("/stories")
def stories():
	story=table.find(story=stories)
	return render_template ("stories.html")




if __name__=="__main__":
	app.run(port=50500) 
