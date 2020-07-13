import binascii
import hashlib
import os
from flask import render_template, request, flash, redirect, Blueprint
from Database import DBQuery
from FlaskSource.Model.UserDetails import UserDetails

userApi = Blueprint('userApi', __name__)


# Hashing Password based on reference https://www.vitoshacademy.com/hashing-passwords-in-python/
# Python Flask API to fetch the data from MYSQL
@userApi.route('/create', methods=['GET', 'POST'])
def createUser():
    try:
        if request.method == "POST":
            postAction = request.form["postAction"]
            if postAction == 'cancel':
                return redirect("/login")
            user_data = DBQuery.getAllUser()
            userName = request.form['UserName']
            email = request.form['Email']
            for userData in user_data:
                userDetails = UserDetails(userData[0], userData[1], userData[2], userData[3], userData[4], userData[5],
                                          userData[6], userData[7], userData[8], userData[9])
                if userName == userDetails.getUserName():
                    flash('User Name Already Taken, Please try with a different user name')
                    return redirect("/create")
            gender = request.form['Gender']
            date_of_birth = request.form['DateofBirth']
            name = request.form['FullName']
            phoneNumber = request.form['PhoneNumber']
            password = request.form['Password']
            confirmPassword = request.form['ConfirmPassword']
            walletBalance = 50
            if name and userName and password and email:
                if password == confirmPassword:
                    DBQuery.createUser(name.capitalize(), userName, hash_password(password), email, gender,
                                       date_of_birth,
                                       phoneNumber, walletBalance)
                    flash('User Account Created Successfully')
                    return redirect("/login")
                else:
                    flash('Passwords don\'t match')
                    return redirect("/create")
            else:
                flash('Please fill in all the details')
                return redirect("/create")
        return render_template("user.html")
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask hash password method
def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    hashPassword = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                       salt, 100000)
    hashPassword = binascii.hexlify(hashPassword)
    return (salt + hashPassword).decode('ascii')
