class OrderDetails:
    def __init__(self, productId, productName, category, subCategory, description, image, price, numberOfItems, totalCountOrdered, orderedBy, timeStamp):
        self.id = productId
        self.category = category
        self.productName = productName
        self.subCategory = subCategory
        self.description = description
        self.image = image
        self.price = price
        self.numberOfItems = numberOfItems
        self.totalCountOrdered = totalCountOrdered
        self.orderedBy = orderedBy
        self.timeStamp = timeStamp

    def getproductId(self):
        return self.id

    def getcategory(self):
        return self.category

    def getMovie(self):
        return self.productName

    def getsubCategory(self):
        return self.subCategory

    def getDescription(self):
        return self.description

    def getImage(self):
        return self.image

    def getPrice(self):
        return self.Price

    def getNumberOfItems(self):
        return self.numberOfItems

    def getTotalCountOrdered(self):
        return self.totalCountOrdered

    def getOrderedBy(self):
        return self.orderedBy

    def getTimeStamp(self):
        return self.timeStamp
