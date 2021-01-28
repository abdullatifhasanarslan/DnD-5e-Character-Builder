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

create_preqresuites_table = """	CREATE TABLE PREQRESUITES(selection varchar(40), feature varchar(40),  type varchar(20),
								FOREIGN KEY (selection) REFERENCES SELECTIONS(name), 
								FOREIGN KEY (feature) REFERENCES FEATURES(name))"""
populate_preqresuites_table = "INSERT INTO PREQRESUITES(selection, feature, type0) VALUES " + data.preqresuites

create_character_selections_table = """	CREATE TABLE CHARACTERSELECTIONS(username varchar(40), selection varchar(40), 
								FOREIGN KEY (username) REFERENCES LOGIN(username),
								FOREIGN KEY (selection) REFERENCES SELECTIONS(name))"""
populate_character_selections_table = "INSERT INTO CHARACTERSELECTIONS(username, selection) VALUES " + data.characterselection

create_preqresuite_satisfaction_table = """	CREATE TABLE PREQRESUITESATISFACTION(username varchar(40), feature varchar(40), 
								FOREIGN KEY (username) REFERENCES LOGIN(username),
								FOREIGN KEY (feature) REFERENCES FEATURES(name))"""
populate_preqresuite_satisfaction_table = "INSERT INTO PREQRESUITESATISFACTION(username, feature) VALUES " + data.preqresuitesatisfaction

create_character_feature_table = """CREATE TABLE CHARACTERFEATURE(username varchar(40), feature varchar(40), 
								FOREIGN KEY (username) REFERENCES LOGIN(username),
								FOREIGN KEY (feature) REFERENCES FEATURES(name))"""
populate_character_feature_table = "INSERT INTO CHARACTERFEATURE(username, feature) VALUES " + data.characterfeature

create_class_subclass_table = """CREATE TABLE CLASSSUBCLASS(class varchar(20), subclass varchar(20), 
								FOREIGN KEY (subclass) REFERENCES SELECTIONS(name),
								PRIMARY KEY (class,subclass))"""
populate_class_subclass_table = "INSERT INTO CLASSSUBCLASS(class, subclass) VALUES " + data.classsubclass	

create_resources_table = "CREATE TABLE RESOURCES(name varchar(20), PRIMARY KEY (name)"
populate_resources_table = "INSERT INTO RESOURCES(name) VALUES " + data.resources	

create_character_feature_table = """CREATE TABLE RESOURCECONSUMPTION(resource varchar(40), feature varchar(40), 
								FOREIGN KEY (resource) REFERENCES RESOURCES(name),
								FOREIGN KEY (feature) REFERENCES FEATURES(name))"""
populate_character_feature_table = "INSERT INTO RESOURCECONSUMPTION(resource, feature) VALUES " + data.resourceconsumption

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

		cursor.execute(create_class_subclass_table)
		cursor.execute(populate_class_subclass_table)

		cursor.execute(create_features_table)
		cursor.execute(populate_features_table)

		cursor.execute(create_preqresuites_table)
		cursor.execute(populate_preqresuites_table)

		cursor.execute(create_character_selections_table)
		cursor.execute(populate_character_selections_table)
		
		cursor.execute(create_preqresuite_satisfaction_table)
		cursor.execute(populate_preqresuite_satisfaction_table)
		
		cursor.execute(create_character_feature_table)
		cursor.execute(populate_character_feature_table)

		cursor.execute(create_resources_table)
		cursor.execute(populate_resources_table)

		cursor.execute(create_resource_consumption_table)
		cursor.execute(populate_resource_consumption_table)
		
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


def list_selections(username):
	check = """	SELECT SELECTIONS.name, FEATURES.name, FEATURES.explanation, SELECTIONS.type FROM CHARACTERSELECTIONS
				LEFT JOIN SELECTIONS ON CHARACTERSELECTIONS.selection=SELECTIONS.name
				LEFT JOIN PREQRESUITES ON CHARACTERSELECTIONS.selection=PREQRESUITES.selection
				LEFT JOIN FEATURES ON PREQRESUITES.feature=FEATURES.name
				WHERE CHARACTERSELECTIONS.username=%s
	"""
	find_class = "SELECT CLASSSUBCLASS.class FROM CLASSSUBCLASS WHERE CLASSSUBCLASS.subclass=%s"
	
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(check,(username,))	
		selections = cursor.fetchall()
		seperated_selections={"Feat":[],"Class":{},"Race":[]}
		for selection in selections:
			if selection[3]=="Subclass":
				cursor.execute(find_class,(selection[0],))	
				class_ = cursor.fetchall()[0][0]
				if class_ in seperated_selections["Class"]:
					seperated_selections["Class"][class_].append(selection[:3])
				else:
					seperated_selections["Class"][class_]=[selection[:3]]
			else:
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
	check = """	SELECT SELECTIONS.name, FEATURES.name, FEATURES.explanation FROM SELECTIONS
				LEFT JOIN PREQRESUITES ON SELECTIONS.name=PREQRESUITES.selection
				LEFT JOIN FEATURES ON PREQRESUITES.feature=FEATURES.name
				WHERE SELECTIONS.type="Subclass" 
	"""
	find_class = "SELECT CLASSSUBCLASS.class FROM CLASSSUBCLASS WHERE CLASSSUBCLASS.subclass=%s"
	
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(check)	
		selections = cursor.fetchall()
		seperated_selections={}
		for selection in selections:
			cursor.execute(find_class,(selection[0],))	
			class_ = cursor.fetchall()[0][0]
			if class_ not in seperated_selections:
				seperated_selections[class_] = []
			seperated_selections[class_].append(selection)
		cursor.close()
		return seperated_selections
	except Error as e:
		print(e)

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

def check_if_user_has_race(username):
	check = """	SELECT * FROM CHARACTERSELECTIONS 
				LEFT JOIN SELECTIONS ON CHARACTERSELECTIONS.selection=SELECTIONS.name 
				WHERE CHARACTERSELECTIONS.username=%s AND SELECTIONS.type="Race"
			"""
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(check, (username,))
		result = cursor.fetchall()
		cursor.close()
		if len(result) > 0:
			return True
		return False
	except Error as e:
		print(e)

def create_selections(name, type):
	add = "INSERT INTO SELECTIONS(name, type) VALUES(%s, %s)"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(add,(name,type))	
		cursor.close()
		connection.commit()
	except Error as e:
		print(e)
def create_preqresuites(selection,feature):
	add = "INSERT INTO PREQRESUITES(selection, feature) VALUES(%s, %s)"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(add,(selection,feature))	
		cursor.close()
		connection.commit()
	except Error as e:
		print(e)
def create_features(name,explanation):
	add = "INSERT INTO FEATURES(name, explanation) VALUES(%s, %s)"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(add,(name,explanation))	
		cursor.close()
		connection.commit()
	except Error as e:
		print(e)
def create_classsubclass(class_,subclass):
	add = "INSERT INTO CLASSSUBCLASS(class, subclass) VALUES(%s, %s)"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(add,(class_,subclass))	
		cursor.close()
		connection.commit()
	except Error as e:
		print(e)


def change_race(username, race):
	add = "INSERT INTO CHARACTERSELECTIONS(username, selection) VALUES(%s, %s)"
			
	update = """UPDATE CHARACTERSELECTIONS CHARACTERSELECTIONS 
				LEFT JOIN SELECTIONS ON CHARACTERSELECTIONS.selection=SELECTIONS.name 
				SET CHARACTERSELECTIONS.selection=%s
				WHERE CHARACTERSELECTIONS.username=%s AND SELECTIONS.type="Race"
			"""
	try:
		cursor = connection.cursor(buffered=True)
		if not check_if_user_has_race(username):
			cursor.execute(add, (username,race))
		else:
			cursor.execute(update, (race,username))
		cursor.close()
		connection.commit()
	except Error as e:
		print(e)


def add_class(username, class_):
	add = "INSERT INTO CHARACTERSELECTIONS(username, selection) VALUES(%s, %s)"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(add,(username,class_))	
		cursor.close()
		connection.commit()
		return True
	except Error as e:
		print(e)
	return False

def add_feat(username, feat):
	add = "INSERT INTO CHARACTERSELECTIONS(username, selection) VALUES(%s, %s)"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(add,(username,feat))	
		cursor.close()
		connection.commit()
		return True
	except Error as e:
		print(e)
	return False

def remove_class(username, class_):
	remove = "DELETE FROM CHARACTERSELECTIONS WHERE username=%s AND selection=%s"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(remove,(username,class_))	
		cursor.close()
		connection.commit()
	except Error as e:
		print(e)

def remove_feat(username, feat):
	remove = "DELETE FROM CHARACTERSELECTIONS WHERE username=%s AND selection=%s"
	try:
		cursor = connection.cursor(buffered=True)
		cursor.execute(remove,(username,feat))	
		cursor.close()
		connection.commit()
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