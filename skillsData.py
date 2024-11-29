import sqlite3
from unittest import result
############## Creat Database And Connect #####################################################
db = sqlite3.connect("skills.db")

##################### Setting Up The Cursor ###################################################
cr = db.cursor()

#################### Creat The Tables And Fields ##############################################
db.execute("CREATE TABLE IF NOT EXISTS skills(user_id integer, skill text, progress integer)")

################## My User Id  ################################################################
uid = 2

######################### Commit and Close Method  ##########################################
def commit_and_close():
    
    """Commit Changes and Close Connection To Database"""
    
    # Save Commit Change
    db.commit()
    
    # Close Database
    db.close()
    
    print("Connection Closed")

# Input Big Message
input_message = """
What Do You Want To Do ?
"S" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill
"q" => Quit The App
Choose Option: 
"""
# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]

# Define The Methods

def show_skills():
    cr.execute(f"select * from skills where user_id = {uid}")
    
    results = cr.fetchall()
    
    print(f"You Have {len(results)} Skills")
    
    if len(results) > 0:
        
        print("Showing Skills With Progress: ")
    
    for row in results:
        
        print(f"Skill => {row[1]}", end=" ")
        
        print(f"Progress => {row[2]}%")
        
    commit_and_close()
    
def add_skill():
    
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"select skill from skills where skill = '{sk}' and user_id = '{uid}'")
    
    results = cr.fetchone()
    
    if results == None:
        print("Skill Is Not  Exists, You Can Add It : ")
        prog = input("Write Skill Progress").strip()
        cr.execute(
                f"insert into skills(user_id, skill, progress) values('{uid}', '{sk}', '{prog}')")
        
    else:
        print("Skill Is Exists, You Cannot Add It! ")
            
    commit_and_close()
    
def delete_skill():
    
    sk = input("Write Skill Name: ").strip().capitalize()
    
    cr.execute(
        f"delete from skills where skill = '{sk}' and user_id = '{uid}'")
    
    commit_and_close()

def update_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    
    prog = input("Write The New Skill Progress").strip()
    
    cr.execute(
        f"update skills set progress = '{prog}' where skill = '{sk}' and user_id = '{uid}'")
    
    commit_and_close()
    
    
def quit_app():
    print("Quit The App")
    commit_and_close()
#########################################

# Check If Command Is Exists
if user_input in commands_list:
    
    print(f"Command Found {user_input}")
    
    if user_input == "s":
        
        show_skills()
        
    elif user_input == "a":
        
        add_skill()
        
    elif user_input == "d":
        
        delete_skill()
        
    elif user_input == "u":
        
        update_skill()
        
    else:
        
        quit_app()
    
else:
    
    print(f"Sorry This Command \"{user_input}\" Is Not Found")

