from datetime import datetime
from flask import render_template, session, redirect, Blueprint, flash, jsonify, logging, request
import requests
from Database import DBQuery
import json

from FlaskSource.Model.OrderDetails import OrderDetails

locationApi = Blueprint('locationApi', __name__)


# Python Flask API for Location
@locationApi.route('/location', methods=['GET', 'POST'])
def getLocation():
    try:
        location_data = {}
        if request.method == "POST":
            userOrderList = []
            if request.get_json():
                userOrderHistory = DBQuery.getUserByUserName(session.get("userName"))
                ajaxData = json.loads(request.get_json()['data'])
                session['walletBalance'] = request.get_json()['wallet']
                # post  location
                if userOrderHistory[9] is None:
                    userOrderList = []
                else:
                    userOrderList = json.loads(userOrderHistory[9])
                for order in ajaxData:
                    productFromDB = DBQuery.getProductUsingId(order['id'])
                    # print("request.json", productFromDB)
                    orderDetails = OrderDetails(productFromDB[0], productFromDB[1], productFromDB[2], productFromDB[3],
                                                productFromDB[4],
                                                productFromDB[5], productFromDB[6], productFromDB[7],
                                                order['count'],
                                                session.get("userName"),
                                                datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
                    userOrderList.append(orderDetails.__dict__)
                session['userOderList'] = userOrderList
                # Sending back AJAX Response Call
                return jsonify(flash("Proceed to order"))
            elif request.form:
                location = request.form["location"]
                address = request.form['address']
                postAction = request.form["postAction"]
                if postAction == 'cancel':
                    return redirect("/shop")
                elif postAction == 'submit':
                    URL = "https://geocode.search.hereapi.com/v1/geocode"
                    location = location#input("Enter the location here: ")  # taking user input
                    api_key = 'oILvnb3yIsakFmQI-UJafpCXmRvN4INE2EZSwgt0R8s'  # Acquire from developer.here.com
                    PARAMS = {'apikey': api_key, 'q': location}

                    # sending get request and saving the response as response object
                    r = requests.get(url=URL, params=PARAMS)
                    data = r.json()

                    # Acquiring the latitude and longitude from JSON
                    latitude = data['items'][0]['position']['lat']
                    longitude = data['items'][0]['position']['lng']
                    location_data['data'] = data
                    location_data['api_key'] = api_key
                    location_data['latitude'] = latitude
                    location_data['longitude'] = longitude
                    location_data['postAction'] = postAction
                    location_data['address'] = address
                    return render_template('location.html', data=location_data)
                elif postAction == 'confirm':
                    userOrderList = session.get('userOderList')
                    DBQuery.updateOrders(json.dumps(userOrderList), session.get("userName"))
                    DBQuery.walletBalance(session.get('walletBalance'), session.get('userName'))
                    # userDetailsFromDB = DBQuery.getUserByUserName(session.get('userName'))
                    session['user'][6] = session.get('walletBalance')
                    flash('Order has been placed successfully! Continue shopping')
                    return redirect('/shop')
        # Default ballsbridge dublin location data
        location_data = {'data': {'items': [{'title': 'Ballsbridge, Dublin, Ireland', 'id': 'here:cm:namedplace:23217387', 'resultType': 'locality', 'localityType': 'district', 'address': {'label': 'Ballsbridge, Dublin, Ireland', 'countryCode': 'IRL', 'countryName': 'Ireland', 'county': 'County Dublin', 'city': 'Dublin', 'district': 'Ballsbridge', 'postalCode': '4'}, 'position': {'lat': 53.33061, 'lng': -6.23343}, 'mapView': {'west': -6.25266, 'south': 53.31556, 'east': -6.20429, 'north': 53.3392}, 'scoring': {'queryScore': 1.0, 'fieldScore': {'district': 1.0}}}]}, 'api_key': 'oILvnb3yIsakFmQI-UJafpCXmRvN4INE2EZSwgt0R8s', 'latitude': 53.33061, 'longitude': -6.23343}
        return render_template('location.html', data=location_data)
    except Exception as e:
        print('Exception:: Location::', e)
        flash('Something went wrong')
        return redirect("/location")

