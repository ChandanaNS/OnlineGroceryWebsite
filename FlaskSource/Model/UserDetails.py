class UserDetails:
    def __init__(self, loginId, name, userName, password, email, gender, dateOfBirth, phoneNumber, walletBalance, orderedProducts):
        self.loginId = loginId
        self.name = name
        self.userName = userName
        self.password = password
        self.email = email
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.phoneNumber = phoneNumber
        self.walletBalance = walletBalance
        self.orderedProducts = orderedProducts

    def getName(self):
        return self.name

    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password

    def getLoginId(self):
        return self.loginId

    def getEmail(self):
        return self.email

    def getGender(self):
        return self.gender

    def getDateOfBirth(self):
        return self.dateOfBirth

    def getPhoneNumber(self):
        return self.phoneNumber

    def getWalletBalance(self):
        return self.walletBalance

    def getOrderedProducts(self):
        return self.orderedProducts

    def setOrderedProducts(self, x):
        self.orderedProducts = x
