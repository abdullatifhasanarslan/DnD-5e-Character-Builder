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


@app.route("/create_selections", methods=["GET","POST"])
def create_selections():
	if request.method == "POST" and session["user"]=="deneme":
		data = request.form
		print(data["SELECTIONS.name"])
		name = data["SELECTIONS.name"]
		type = data["SELECTIONS.type"]

		database.create_selections(name,type)

		return redirect("/create")
	else:
		return redirect("/")

@app.route("/create_preqresuites", methods=["GET","POST"])
def create_preqresuites():
	if request.method == "POST" and session["user"]=="deneme":
		data = request.form
		print(data)
		selection = data["PREQRESUITES.selection"]
		feature = data["PREQRESUITES.feature"]

		database.create_preqresuites(selection,feature)
		#redirect to main page
		return redirect("/create")
	else:
		return redirect("/")

@app.route("/create_features", methods=["GET","POST"])
def create_features():
	if request.method == "POST" and session["user"]=="deneme":
		data = request.form
		name = data["FEATURES.name"]
		explanation = data["FEATURES.explanation"]

		database.create_features(name,explanation)
		#redirect to main page
		return redirect("/create")
	else:
		return redirect("/")

@app.route("/create_classsubclass", methods=["GET","POST"])
def create_classsubclass():
	if request.method == "POST" and session["user"]=="deneme":
		data = request.form
		class_ = data["CLASSSUBCLASS.class"]
		subclass = data["CLASSSUBCLASS.subclass"]

		database.create_classsubclass(class_,subclass)
		#redirect to main page
		return redirect("/create")
	else:
		return redirect("/")



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

@app.route("/add_class/<class_>", methods=['GET'])
def add_class(class_):
	if "user" in session:
		database.add_feat(session["user"], class_)
		return redirect("/classes")
	else:
		return redirect("/")

@app.route("/add_feat/<feat>", methods=['GET'])
def add_feat(feat):
	if "user" in session:
		database.add_feat(session["user"], feat)
		return redirect("/feats")
	else:
		return redirect("/")

@app.route("/remove_class/<class_>", methods=['GET'])
def remove_class(class_):
	if "user" in session:
		database.remove_feat(session["user"], class_)
		return redirect("/character")
	else:
		return redirect("/")

@app.route("/remove_feat/<feat>", methods=['GET'])
def remove_feat(feat):
	if "user" in session:
		database.remove_feat(session["user"], feat)
		return redirect("/character")
	else:
		return redirect("/")

@app.route("/character")
def character_page():
	if "user" in session:
		return render_template("character.html", selections=database.list_selections(session["user"]))
	else:
		return redirect("/")

@app.route("/create", methods=["GET","POST"])
def edit_page():
	if "user" in session and session["user"] == "deneme":
		return render_template("add.html")
	return redirect("/")


@app.route("/logout")
def logout():
	session.pop("user",None)
	return redirect("/")


if __name__=="__main__":
	database.create_connection()
	app.run(debug=True)
	database.close_connection()
