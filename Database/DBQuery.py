from Database import DBConnection


# Fetch all the products from Database
def getAllProducts():
    cur = DBConnection.connection().cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    cur.close()
    return data


# Add products to Database
def addProduct(tableName, ProductName, Category, SubCategory,
               Description, Image, Price, Discount):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "INSERT INTO " + tableName + "(ProductName, Category, SubCategory,Description, Image, Price, Discount) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (ProductName, Category, SubCategory, Description, Image, Price, Discount))
    db_connection.commit()
    cur.close()


# Fetch Product using Product ID
def getProductUsingId(productID):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM products where ProductID=" + str(productID))
    data = cur.fetchone()
    db_connection.commit()
    cur.close()
    return data


# Delete  product using  product ID
def deleteProductUsingId(productId):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute("DELETE from products where ProductID=" + productId)
    db_connection.commit()
    cur.close()


# Update product using product ID
def updateProduct(productId, productName, category, subCategory, description, image, price, discount):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "UPDATE products SET ProductName=%s,Category=%s,SubCategory=%s,Description=%s,Image=%s,Price=%s,Discount=%s where ProductID=%s",
        (productName, category, subCategory, description, image, price, discount, productId))
    db_connection.commit()
    cur.close()


# update password using userName
def updatePassword(userName, newPassword):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "UPDATE users SET Password=%s where userName=%s",
        (newPassword, userName))
    db_connection.commit()
    cur.close()


# Fetch all users
def getAllUser():
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "Select * from users ")
    data = cur.fetchall()
    db_connection.commit()
    cur.close()
    return data


# Create User in Database
def createUser(name, userName, password, email, gender, dob, phoneNumber, walletBalance):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "INSERT INTO users (FullName,UserName, Password,Email,Gender,DateOfBirth,PhoneNumber, Wallet) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (name, userName, password, email, gender, dob, phoneNumber, walletBalance))
    db_connection.commit()
    cur.close()


# Get User by User Name
def getUserByUserName(userName):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "Select * from users where UserName=%s", userName)
    data = cur.fetchone()
    db_connection.commit()
    cur.close()
    return data


# update ordered products
def updateOrders(product_list, userName):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "update users set OrderedProducts='{0}' where UserName='{1}'".format(product_list, userName))
    db_connection.commit()
    cur.close()


# update wallet balance
def walletBalance(wallet, userName):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "UPDATE users SET Wallet=%s where userName=%s", (wallet, userName))
    db_connection.commit()
    cur.close()
