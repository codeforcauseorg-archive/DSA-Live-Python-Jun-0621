class Human:
    def __init__(self):
        self.hands = 2
        self.money = 1000

    def party(self):
        if self.money >= 200:
            self.money -= 200
            print("Yayyy. party party")
        else:
            print("oh noooo")

    def borrow(self, friend):
        if friend.money >= 500:
            friend.money -= 500
            self.money += 500
        else:
            print("I got nothing bro")


anuj = Human()
bharat = Human()

bharat.party()
bharat.party()
bharat.party()
bharat.party()
bharat.party()
bharat.party()

bharat.borrow(anuj)

bharat.party()
bharat.party()
bharat.party()
bharat.party()

bharat.borrow(anuj)

bharat.party()
bharat.party()
bharat.party()

bharat.borrow(anuj)





# Human.party(bharat)



print(bharat.money)
print(anuj.money)


