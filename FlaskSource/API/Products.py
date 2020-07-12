from flask import render_template, session, request, redirect, Blueprint, flash, jsonify, logging
from FlaskSource.Model.ProductBrief import ProductBrief
from Database import DBQuery
import json

productApi = Blueprint('productApi', __name__)

# Python Flask API for home page
@productApi.route('/')
def homePage():
    try:
        login_dictionary = {}
        if session.get('logged_in'):
            login_dictionary['logged_in'] = "true"
        elif session.get('superAdmin'):
            login_dictionary["superAdmin"] = "true"
        return render_template('index.html', data=login_dictionary)
    except:
        flash('Something went wrong')
        return redirect("/")


@productApi.route('/shop')
def shop():
    try:
        login_dictionary = {}
        data = DBQuery.getAllProducts()
        product_list = []
        if session.get('logged_in'):
            login_dictionary['logged_in'] = "true"
        elif session.get('superAdmin'):
            login_dictionary["superAdmin"] = "true"
        login_dictionary['user'] = session['user']

        # Fetch All the products from Database
        for productFromDB in data:
            productBrief = ProductBrief(productFromDB[0], productFromDB[1], productFromDB[2], productFromDB[3],
                                        productFromDB[4], productFromDB[5], productFromDB[6], productFromDB[7])

            jsonData = json.dumps(productBrief.__dict__)
            product_list.append(json.loads(jsonData))
        login_dictionary['productList'] = json.dumps(product_list)
        return render_template('shop.html', data=login_dictionary)
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask API for adding a product
@productApi.route('/add', methods=['GET', 'POST'])
def addProduct():
    try:
        if request.method == "POST":
            postAction = request.form["postAction"]
            if postAction == 'cancel':
                return redirect("/admin")
            ProductName = request.form["ProductName"]
            Category = request.form["Category"]
            SubCategory = request.form["SubCategory"]
            Description = request.form["Description"]
            Image = request.form["Image"]
            Price = request.form["Price"]
            Discount = request.form["Discount"]
            if ProductName and Category and SubCategory and Price and Discount:
                DBQuery.addProduct('products', ProductName.title(), Category.title(), SubCategory.title(),
                                   Description.title(), Image, Price.title(), Discount.title())
                flash("product Added Successfully")
                return redirect("/admin")
            else:
                flash('Please fill in all the details')
                return redirect("/add")
        return render_template('add.html')
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask API for updating a product
@productApi.route('/update', methods=['GET', 'POST'])
def updateProduct():
    try:
        productId = request.args.get('id')
        product = []
        # Fetch product from Database using product ID
        if productId is not None:
            productFromDB = DBQuery.getProductUsingId(productId)
            productBrief = ProductBrief(productFromDB[0], productFromDB[1], productFromDB[2], productFromDB[3],
                                        productFromDB[4], productFromDB[5], productFromDB[6], productFromDB[7])
            product.append(productBrief.__dict__)
        else:
            if request.method == "POST":
                postAction = request.form["postAction"]
                if postAction == 'cancel':
                    return redirect("/admin")
                if postAction == 'delete':
                    return deleteproduct()
                productId = int(request.form["productId"])
                productName = request.form["productName"]
                category = request.form["category"]
                subCategory = request.form["subCategory"]
                description = request.form["description"]
                image = request.form["image"]
                price = request.form["price"]
                discount = request.form["discount"]
                if productName and category and subCategory and price and discount:
                    DBQuery.updateProduct(productId, productName, category, subCategory, description, image, price,
                                          discount)
                    flash("product Updated Successfully")
                    return redirect("/admin")
                else:
                    flash('Please fill in all the details')
                    return redirect("/update")
        jsonData = json.dumps(product)
        return render_template('update.html', update=json.loads(jsonData))
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask API for deleting a product
@productApi.route('/delete')
def deleteproduct():
    try:
        productId = request.form["productId"]
        DBQuery.deleteProductUsingId(productId)
        flash("Product Deleted Successfully")
        return redirect("/admin")
    except:
        flash('Something went wrong')
        return redirect("/")
