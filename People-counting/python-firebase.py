import pyrebase
import time

Config = {
    apiKey: "AIzaSyA_64nvoL4vycEjrq_Rb10acAgcwjLmu2E",
    authDomain: "st-pc-f86d8.firebaseapp.com",
    databaseURL: "https://st-pc-f86d8.firebaseio.com",
    storageBucket: ""
    }
  
firebase = pyrebase.initialize_App(Config)
db = firebase.database()



#build paths
# db.child("building").child("location1")

#save data
#data = {"location1": 123}
#db.child("building").push(data)

#update
for i in range(10):
    db.child("building").child("location1")
    db.child("building").updata({"location1":123+i})
    time.sleep(10)
    



