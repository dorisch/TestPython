from pymongo import MongoClient

def put_items(mycol):
    mylist = []
    for i in range(1,101):
        mylist.append({ "val": i, "res": "null" })

    x = mycol.insert_many(mylist)
    return None

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycollection = mydb["tasks"]

if __name__ == "__main__":
    put_items(mycollection)
