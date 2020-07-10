import binascii
import hashlib
from flask import render_template, request, flash, redirect, session, Blueprint, logging
from Database import DBQuery
from FlaskSource.Model.UserDetails import UserDetails
from FlaskSource.API.User import hash_password

loginApi = Blueprint('loginApi', __name__)


# Creating Session taken from the reference https://pythonhosted.org/Flask-Session/
# Python Flask API for login
@loginApi.route('/login', methods=['GET', 'POST'])
def loginPage():
    try:
        if request.method == "POST":
            userName = request.form["username"]
            password = request.form["password"]
            postAction = request.form["postAction"]
            if postAction == 'create':
                return redirect("/create")
            elif postAction == 'home':
                return redirect("/")
            userDetailsFromDB = DBQuery.getUserByUserName(userName)

            print(userDetailsFromDB)
            if userDetailsFromDB:
                # Based on Database Details, Passing it in UserDetails Class
                userDetails = UserDetails(userDetailsFromDB[0], userDetailsFromDB[1], userDetailsFromDB[2],
                                          userDetailsFromDB[3], userDetailsFromDB[4], userDetailsFromDB[5],
                                          userDetailsFromDB[6], userDetailsFromDB[7])
                if verify_password(userDetails.getPassword(), password):
                    if userName == 'admin' and password == 'admin':
                        print("super admin logged in")
                        session['superAdmin'] = True
                    else:
                        print("User Logged in")
                        session['logged_in'] = True
                    session['userName'] = userName
                    return redirect("/")
                else:
                    flash('Please enter a valid password')
                    return redirect("/login")
            else:
                flash('No Username and Password found in our records, Please try again')
                return redirect("/login")
        return render_template('login.html')
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask API for Logout
@loginApi.route("/logout")
def logout():
    try:
        if session.get("superAdmin"):
            session['superAdmin'] = False
        else:
            session['logged_in'] = False
        return redirect("/")
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask API for Forgot password
@loginApi.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    try:
        if request.method == "POST":
            userName = request.form["username"]
            newPassword = request.form["NewPassword"]
            password = request.form["ConfirmPassword"]
            postAction = request.form["postAction"]
            if postAction == 'cancel':
                return redirect("/login")
            if postAction == 'submit' and userName and password and newPassword:
                if newPassword == password:
                    DBQuery.updatePassword(userName, hash_password(newPassword));
                    flash("Password Updated Successfully")
                    return redirect("/login")
                else:
                    flash("Passwords don't match")
                    return redirect('/forgotPassword')
            else:
                flash("Enter the details")
        return render_template('forgotPassword.html')
    except:
        flash('Something went wrong')
        return redirect("/")


def verify_password(stored_password, database_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    hashPassword = hashlib.pbkdf2_hmac('sha512',
                                       database_password.encode('utf-8'),
                                       salt.encode('ascii'),
                                       100000)
    hashPassword = binascii.hexlify(hashPassword).decode('ascii')
    print(hashPassword,stored_password)
    return hashPassword == stored_password
