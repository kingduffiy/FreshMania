from pymongo import MongoClient
from pydantic import BaseModel, Field
#Importing libraries that we are going to use
#pydantic is essential to keep our code way smaller and clean

client = MongoClient("localhost", 27017)
db = client["mymongo"]
collection = db["test"]
#I really really tried to use pyMongo, but unfortunately i didn`t succeed =(


class Product(BaseModel):
    #here we create our class, using the BaseModel from pydantic,
    # which is going to validate the inputs
    name: str
    description: str
    price: float = Field(..., gt=0)
    #This is basically to validate if the price is greater than 0, 
    # which means that the price cannot be a negative number.
    image: str

    def post(self):
        #This is a function that will make the POST action (post method)
        database.append(self.copy())
        return self.json()

    @staticmethod
    def get():
        #This function will return our database (classic get method)
        return database

    @staticmethod
    def get_by_name(name):
        #This function let us search an item in our database by name
        return list(filter(lambda product: product.name == name, database))
        #Here we are using another class from pydantic(called filter) 
        # and a lambda only to filter our item at our database by name
    @staticmethod
    def update(name, new_name=None, description=None, price=None, image=None):
        #This will update an item at our database. The way that the code
        #  is writen let us update anything we want.
        products = Product.get_by_name(name)
        if len(products) > 0:
            #Here we validate if the database isn`t empty
            product = products[0]
            if new_name != None:
                product.name = new_name
            if description != None:
                product.description = description
            if price != None:
                product.price = price
            if image != None:
                product.image = image

        return product

    @staticmethod
    def delete(name):
        #Simple function to delete an item at our database (delete method)
        products = Product.get_by_name(name)
        if len(products) > 0:
            #Again, validating if the database has something
            database.remove(products[0])


if __name__ == "__main__":
    database = [
    ]  #This is our "database" (because i couldn`t create with pyMongo T_T)
    
    #Here we are inserting items at our database
    a = Product(
        name="caixa",
        description="sdfhgsdjkfhsjkdfhdj",
        price=120,
        image="isto e uma imagem",
    )
    a.post()
    #Here we are inserting items at our database AGAIN
    b = Product(
        name="controle",
        description="sdfhgsdjkfhsjkdfhdj",
        price=200,
        image="isto e uma imagem",
    )
    b.post()

    #And that`s it, i know i only make it through stage 1, but it was
    #  a long run trying to use pyMongo to make things work. 
    # unfortunately i did not managed to complete all the stages, 
    # but i`m definitely gonna learn how to do it. 
    # Thanks for your attention! =)