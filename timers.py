import threading

def myFun():
    print("Alarm ringing")
    
 timer = threading.Timer(5.0,myFun)
 timer.start()
