from pymongo import MongoClient
import time
import random

def update_res(mycol):

    r = None
    i = 1
    while True:
        print(i)
        i += 1
        r = mycol.find_one({"res": "null"})
        if r is None:
            break
        mycol.find_and_modify({"_id": r["_id"]},
                            {
            "$set": {
                "res": r["val"] * r["val"]
            }
        })
        time.sleep(random.uniform(1, 2))

    return None

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycollection = mydb["tasks"]

if __name__ == "__main__":
    update_res(mycollection)