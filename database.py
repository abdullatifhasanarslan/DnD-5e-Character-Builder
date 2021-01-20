from mysql.connector import connect, Error
import data
import yaml


delete_database = "DROP DATABASE POWER"
create_database = "CREATE DATABASE POWER"
use_database = "USE POWER"
create_login_table = "CREATE TABLE LOGIN(username varchar(40), password varchar(20), PRIMARY KEY (username))"
create_deneme_user = "INSERT INTO LOGIN(username, password) VALUES " + data.deneme
create_selections_table = "CREATE TABLE SELECTIONS(name varchar(40), type varchar(20), PRIMARY KEY (name))"
populate_selections_table = "INSERT INTO SELECTIONS(name, type) VALUES " + data.selections
create_features_table = "CREATE TABLE FEATURES(name varchar(40), explanation varchar(2000), PRIMARY KEY (name))"
populate_features_table = "INSERT INTO FEATURES(name, explanation) VALUES " + data.features
create_preqresuites_table = """	CREATE TABLE PREQRESUITES(selection varchar(40), feature varchar(40), 
								FOREIGN KEY (selection) REFERENCES SELECTIONS(name), 
								FOREIGN KEY (feature) REFERENCES FEATURES(name))"""
populate_preqresuites_table = "INSERT INTO PREQRESUITES(selection, feature) VALUES " + data.preqresuites

create_character_selections_table = """	CREATE TABLE CHARACTERSELECTIONS(username varchar(40), selection varchar(40), 
								FOREIGN KEY (username) REFERENCES LOGIN(username),
								FOREIGN KEY (selection) REFERENCES SELECTIONS(name))"""
populate_character_selections_table = "INSERT INTO CHARACTERSELECTIONS(username, selection) VALUES " + data.characterselection

	


connection=None

def create_connection():
	global connection
	try:
		#connect to mysql
		db = yaml.load(open("db.yaml"))
		connection = connect(host=db["mysql_host"],user=db["mysql_user"],password=db["mysql_password"])
		cursor = connection.cursor()
		cursor.execute(use_database)
		cursor.close()
	except Error as e:
		print(e)






def restart_database():
	
	try:
		cursor = connection.cursor()
		
		

		cursor.execute(delete_database)
		cursor.execute(create_database)
		cursor.execute(use_database)

		cursor.execute(create_login_table)
		cursor.execute(create_deneme_user)

		cursor.execute(create_selections_table)
		cursor.execute(populate_selections_table)

		cursor.execute(create_features_table)
		cursor.execute(populate_features_table)

		cursor.execute(create_preqresuites_table)
		cursor.execute(populate_preqresuites_table)

		cursor.execute(create_character_selections_table)
		cursor.execute(populate_character_selections_table)
		
		
		cursor.close()
		connection.commit()
	except Error as e:
		print(e)

def user_exists(username):
	check = "SELECT * FROM LOGIN WHERE username=%s"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(check,(username,))	
		matches = cursor.fetchall()
		cursor.close()
		if len(matches)>0:
			return True
	except Error as e:
		print(e)

	return False
	
def create_user(username,password):
	create = "INSERT INTO LOGIN(username, password) VALUES(%s, %s)"
	try:
		cursor = connection.cursor(buffered=True)
		#check if username is already taken
		if user_exists(username):
			cursor.close()
			return False
		#if not, why not
		cursor.execute(create,(username,password))	
		cursor.close()
		connection.commit()
		return True
	except Error as e:
		print(e)
	return False

def check_login(username,password):
	check = 'SELECT * FROM LOGIN WHERE username=%s AND password=%s'
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(check, (username, password))	
		matches = cursor.fetchall()
		cursor.close()
		if len(matches)>0:
			return True

	except Error as e:
		print(e)

	return False


def list_selections():
	check = """	SELECT SELECTIONS.name, FEATURES.name, FEATURES.explanation, SELECTIONS.type FROM CHARACTERSELECTIONS
				LEFT JOIN SELECTIONS ON CHARACTERSELECTIONS.selection=SELECTIONS.name
				LEFT JOIN PREQRESUITES ON CHARACTERSELECTIONS.selection=PREQRESUITES.selection
				LEFT JOIN FEATURES ON PREQRESUITES.feature=FEATURES.name
	"""

	
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(check)	
		selections = cursor.fetchall()
		seperated_selections={"Feat":[],"Class":[],"Race":[]}
		for selection in selections:
			seperated_selections[selection[3]].append(selection[:3])
		cursor.close()
		return seperated_selections
	except Error as e:
		print(e)

	return []

def list_feats():
	feats_check = """	SELECT SELECTIONS.name, FEATURES.explanation FROM PREQRESUITES
						LEFT JOIN SELECTIONS ON PREQRESUITES.selection=SELECTIONS.name
						LEFT JOIN FEATURES ON PREQRESUITES.feature=FEATURES.name
						WHERE SELECTIONS.type="Feat"
	"""
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(feats_check)	
		feats = cursor.fetchall()
		cursor.close()
		return feats
	except Error as e:
		print(e)

	return []

def list_classes():
	check = "SELECT * FROM SELECTIONS WHERE type=%s"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(check,("Class",))	
		matches = cursor.fetchall()
		cursor.close()
		return matches
	except Error as e:
		print(e)

	return []

def list_races():
	check = """	SELECT SELECTIONS.name, FEATURES.name, FEATURES.explanation FROM PREQRESUITES
						LEFT JOIN SELECTIONS ON PREQRESUITES.selection=SELECTIONS.name
						LEFT JOIN FEATURES ON PREQRESUITES.feature=FEATURES.name
						WHERE SELECTIONS.type="Race"
	"""
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(check)	
		matches = cursor.fetchall()
		cursor.close()
		races={}
		for feature in matches:
			if feature[0] in races:
				races[feature[0]].append([feature[1],feature[2]])
			else:
				races[feature[0]]=[[feature[1],feature[2]]]
		return races
	except Error as e:
		print(e)

	return []

def change_race(username, race):
	update = """UPDATE CHARACTERSELECTIONS CHARACTERSELECTIONS 
				LEFT JOIN SELECTIONS ON CHARACTERSELECTIONS.selection=SELECTIONS.name 
				SET CHARACTERSELECTIONS.selection=%s
				WHERE CHARACTERSELECTIONS.username=%s AND SELECTIONS.type="Race"
			"""
	try:
		cursor = connection.cursor(buffered=True)
		result = cursor.execute(update, (race,username))
		cursor.close()
	except Error as e:
		print(e)

def list_users():
	try:
		cursor = connection.cursor(buffered=True)
		result = cursor.execute("SELECT * FROM LOGIN")
		users = cursor.fetchall()
		cursor.close()
		return users
	except Error as e:
		print(e)

def close_connection():
	connection.close()

if __name__ == "__main__":
	if input("do you want to reset:")=="yes":
		create_connection()
		restart_database()
		close_connection()

		print("reset finished")
	else:
		print("did not reset")