import click
from flask import Flask
from flask.cli import with_appcontext, AppGroup
import csv
from App.database import create_db
from App.main import app, migrate
from flask_login import LoginManager, current_user
from App.controllers import ( create_user, get_all_users_json, get_all_users, add_word, get_random_word, login_user )

# This commands file allow you to create convenient CLI commands
# for testing controllers

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''


# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 
word_cli = AppGroup('word', help='Word object commands')
# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

@word_cli.command("random", help="Gets a random word")
def random_word():
    word = get_random_word()
    print(word.toDict())

app.cli.add_command(word_cli)

'''
Generic Commands
'''
@app.cli.command("migrate")
def mig():
    return migrate

@app.cli.command("init")
def initialize():
    jsonArray = []

    with open('./App/dictionary.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['Word'] = row['Word'].lower()
            for key in row.keys():
                if row.get(key) == "":
                    swap = {key : None}
                    row.update(swap)
            jsonArray.append(row)
    

    for row in jsonArray: 
        add_word(row['Word'], row['PartsOfSpeech'], row['Meaning']) 
    create_db(app)
    print('database intialized')