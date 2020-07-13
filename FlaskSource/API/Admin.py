from datetime import date

from flask import render_template, flash, Blueprint, redirect, session
from FlaskSource.Model.ProductBrief import ProductBrief
from FlaskSource.Model.UserDetails import UserDetails
from FlaskSource.Model.OrderDetails import OrderDetails

from Database import DBQuery
import json

adminApi = Blueprint('adminApi', __name__)


# Python Flask API to Show Admin Statics
@adminApi.route('/admin')
def adminLogs():
    try:
        login_dictionary = {}
        user_list = []
        order_list = []
        if session.get('superAdmin'):
            login_dictionary["superAdmin"] = "true"
            user_data = DBQuery.getAllUser()
            for userData in user_data:
                userDetails = UserDetails(userData[0], userData[1], userData[2], userData[3], userData[4], userData[5],
                                          date.isoformat(userData[6]),
                                          userData[7], userData[8], userData[9])
                if userDetails.getUserName() != "admin":
                    if userDetails.getOrderedProducts() is None:
                        userDetails.setOrderedProducts([])
                        jsonUserDump = json.dumps(userDetails.__dict__)
                        user_list.append(json.loads(jsonUserDump))
                    else:
                        jsonUserDump = json.dumps(userDetails.__dict__)
                        user_list.append(json.loads(jsonUserDump))
                        # if userDetails.getOrderedProducts() is not None:
                        for value in json.loads(userDetails.getOrderedProducts()):
                            orderDetails = OrderDetails(value['id'], value['productName'], value['category'],
                                                        value['subCategory'],
                                                        value['description'], value['image'], value['price'],
                                                        value['numberOfItems'], value['totalCountOrdered'],
                                                        value['orderedBy'],
                                                        value['timeStamp'])
                            jsonDump = json.dumps(orderDetails.__dict__)
                            order_list.append(json.loads(jsonDump))
        elif session.get('logged_in'):
            login_dictionary['logged_in'] = "true"
        # Fetch All the products from Database
        product_data = DBQuery.getAllProducts()
        product_list = []
        for productFromDB in product_data:
            productBrief = ProductBrief(productFromDB[0], productFromDB[1], productFromDB[2],
                                        productFromDB[3],
                                        productFromDB[4], productFromDB[5], productFromDB[6],
                                        productFromDB[7])

            jsonData = json.dumps(productBrief.__dict__)
            product_list.append(json.loads(jsonData))
        login_dictionary['userList'] = user_list
        login_dictionary['orderList'] = order_list
        login_dictionary['productList'] = json.dumps(product_list)
        return render_template('admin.html', data=login_dictionary)
    except Exception as e:
        flash('Something went wrong')
        return redirect("/")
