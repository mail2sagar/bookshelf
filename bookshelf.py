
class Citizen:
    def __init__(self,name,author,date):
        print("Book added")
        self.name = name
        self.author = author
        self.date = date
    def add_details(self):
        print("Book details added") 
        print(self.name) 
        print(self.author)
        print(self.date)  

obj3 = Citizen("Book name : ","Harry Potter and the Philosopher's Stone","By J.K. Rowling")

obj4 = Citizen("Book name : ","Diary of the whimpy kid,","by Jeff Kinney")

obj3.add_details()

obj4.add_details()