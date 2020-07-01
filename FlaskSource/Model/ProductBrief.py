class ProductBrief:
    def __init__(self, productId, productName, category, subCategory, description, image, price, discount):
        self.id = productId
        self.productName = productName
        self.category = category
        self.subCategory = subCategory
        self.description = description
        self.image = image
        self.price = price
        self.discount = discount

    def getproductId(self):
        return self.id

    def getproduct(self):
        return self.productName
    
    def getCategory(self):
        return self.category

    def getSubCategory(self):
        return self.subCategory

    def getDescription(self):
        return self.description

    def getImage(self):
        return self.image

    def getprice(self):
        return self.price

    def getDiscount(self):
        return self.discount
