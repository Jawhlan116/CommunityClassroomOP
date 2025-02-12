class GroceryStore:
    def __init__(self, applekg, applecost, orangekg, orangecost):
        self.applekg=applekg
        self.applecost=applecost
        self.orangekg=orangekg
        self.orangecost=orangecost
        self.orlogo=(applekg*applecost+orangekg*orangecost)
bambaruush=GroceryStore(534, 5000, 487, 10000)
print("Бамбарууш дэлгүүрийн орлого: "+str(bambaruush.orlogo))
jimshen=GroceryStore(764, 4800, 423, 9300)
print("Жимсхэн дэлгүүрийн орлого: "+str(jimshen.orlogo))
fruits=GroceryStore(136, 5000, 228, 10000)
print("Fruits дэлгүүрийн орлого: "+str(fruits.orlogo))