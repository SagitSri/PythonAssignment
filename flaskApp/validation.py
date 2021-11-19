import datetime
import re
import db
from flask import json

def validate_user(usermail, userpsw):
    return db.checkUserExists(usermail, userpsw)

def validate_register_form_data(*args): 
    print(args)   
    userfname = args[0]['userfname']
    userlname = args[0]['userlname']
    userdob = args[0]['userdob']
    usermail = args[0]['usermail']
    userpassword =args[0]['userpassword']
    error_msgs = []
    success_msgs = []
    
    if len(userpassword) != 0:
        if len(userpassword) < 8:
            error_msgs.append('password length should be atleast 8.')
        elif len(userpassword) > 8:
            error_msgs.append('password should not above 8 characters')
        elif not any(x.isupper() for x in userpassword):
            error_msgs.append('password must have 1 upper case character.')
        elif not any(x.islower() for x in userpassword):
            error_msgs.append('password must have 1 lower case character.')
        elif not any(x.isdigit() for x in userpassword):
            error_msgs.append('password must have 1 number.')
    else:
        error_msgs.append("please enter password")

    if len(userfname) == 0:
        error_msgs.append('Please enter first name')

    if len(userlname) == 0:
        error_msgs.append('Please enter last name')
    
    if len(usermail) == 0:
        error_msgs.append('Please enter email')

    if len(userdob) == 0:
        error_msgs.append('Please enter date of birth')
    elif not datetime.datetime.strptime(userdob, "%Y-%m-%d"):
        error_msgs.append('Incorrect date format, should be YYYY-MM-DD')
        
    if userpassword == userlname:
        error_msgs.append('password must not be the first name')
    elif  userpassword == userlname:
        error_msgs.append('password must not be the last name')
    elif userpassword == userdob:
        error_msgs.append('password must not be the dob')

    if db.checkUserExists(usermail,userpassword):
        error_msgs.append('User Exists')
    elif not error_msgs:
        db.addUser(userfname, userlname, userdob, usermail, userpassword)
        success_msgs.append("user added!")
    
    print(error_msgs)
    response_msg = json.jsonify(error_msg = error_msgs, success_msg = success_msgs)
    error_msgs = []
    success_msgs = []
    return response_msg