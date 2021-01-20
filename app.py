from flask import Flask, render_template, request, redirect, url_for, session
import database

app = Flask(__name__)
app.secret_key = "wubalubadubd"

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "POST":
		data = request.form
		username = data["username"]
		password = data["password"]

		if data["button"]=="register":
			#check if username exist
			if database.create_user(username,password):
				session["user"] = username
				return redirect("/character")
			#redirect to main page
			return render_template("index.html", message="register fail")
	
		elif data["button"]=="login":
			#check if login success
			if database.check_login(username, password):
				session["user"] = username
				return redirect("/character")
			#redirect to main page
			return render_template("index.html", message="login fail")
	else:
		if "user" in session:
			return redirect("/character")
		return render_template("index.html")

@app.route("/users")
def users():
	users = database.list_users()
	return render_template("users.html", users=users)

@app.route("/classes")
def classes_page():
	if "user" in session:
		return render_template("classes.html", classes=database.list_classes())
	else:
		return redirect("/")

@app.route("/feats")
def feats_page():
	if "user" in session:
		feats = (database.list_feats())
		# feats_list = []
		# for i, feat in enumerate(feats):
		# 	feats_list.append([feats[i][0],feats[i][1]])
		# 	feats_list[i][1].replace("\n","<br>")
		return render_template("feats.html", feats=feats)
	else:
		return redirect("/")
	
@app.route("/races")
def races_page():
	if "user" in session:
		return render_template("races.html", races=database.list_races())
	else:
		return redirect("/")

@app.route("/change_race/<race>", methods=['GET'])
def change_race(race):
	if "user" in session:
		database.change_race(session["user"], race)
		return redirect("/races")
	else:
		return redirect("/")

@app.route("/character")
def character_page():
	if "user" in session:
		return render_template("character.html", selections=database.list_selections())
	else:
		return redirect("/")
	

@app.route("/logout")
def logout():
	session.pop("user",None)
	return redirect("/")


if __name__=="__main__":
	database.create_connection()
	app.run(debug=True)
	database.close_connection()
