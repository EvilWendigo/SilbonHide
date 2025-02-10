import os
import stegano as so

def print_header():
    os.system("figlet SilbonHide")
    print("made by evilwendigo")
def show_help():
    print("commands:")
    print("image > Enter image to hide message")
    print("message > Enter message to hide in image")
    print("output > the output of the image and the message combanied")
    print("hide > hide messsage in the image once entered")
    print("reveal > reveal suspected hidden text in file")
    print("clear > clear screen")
    print("exit > exit program")
print_header()
while True:
    shell = input("丂ﾉﾚ乃の刀 >")
    if shell == "image":
        os.system("figlet Image")
        image = input("丂ﾉﾚ乃の刀 >")
    if shell == "message":
        os.system("figlet Message")
        message = input("丂ﾉﾚ乃の刀 >")
    if shell == "output":
        os.system("figlet output")
        output = input("丂ﾉﾚ乃の刀 >")
    if shell == "hide":
        secret_image = so.lsb.hide(image,message)
        secret_image.save(output)
        print(f"Message hidden in {output}")
    if shell == "reveal":
        os.system("figlet reveal")
        reveal_text = input("丂ﾉﾚ乃の刀 >")
        revealed_text = so.lsb.reveal(reveal_text)
        print(f"the text hidden is : {revealed_text}")
    if shell == "help":
        show_help()
    if shell == "clear":
        os.system("clear")
        print_header()
    if shell == "exit":
        exit()



"丂ﾉﾚ乃の刀 >"