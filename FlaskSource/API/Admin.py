from flask import render_template, flash, Blueprint, redirect, session
from FlaskSource.Model.ProductBrief import ProductBrief
from FlaskSource.Model.UserDetails import UserDetails

from Database import DBQuery
import json

adminApi = Blueprint('adminApi', __name__)


# Python Flask API to Show Admin Statics
@adminApi.route('/admin')
def adminLogs():
    try:
        login_dictionary = {}
        data = DBQuery.getAllProducts()
        product_list = []
        if session.get('superAdmin'):
            login_dictionary["superAdmin"] = "true"
        elif session.get('logged_in'):
            login_dictionary['logged_in'] = "true"
        # Fetch All the products from Database
        for productFromDB in data:
            productBrief = ProductBrief(productFromDB[0], productFromDB[1], productFromDB[2], productFromDB[3],
                                        productFromDB[4], productFromDB[5], productFromDB[6], productFromDB[7])

            jsonData = json.dumps(productBrief.__dict__)
            product_list.append(json.loads(jsonData))
        login_dictionary['productList'] = json.dumps(product_list)
        return render_template('admin.html', data=login_dictionary)
    except:
        flash('Something went wrong')
        return redirect("/")
