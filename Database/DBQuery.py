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
    cur.execute("SELECT * FROM products where ProductID=" + productID)
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
    print("Query", productId, productName, category, subCategory, description, image, price, discount)
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "UPDATE products SET ProductName=%s,Category=%s,SubCategory=%s,Description=%s,Image=%s,Price=%s,Discount=%s where ProductID=%s",
        (productName, category, subCategory, description, image, price, discount, productId))
    db_connection.commit()
    cur.close()
