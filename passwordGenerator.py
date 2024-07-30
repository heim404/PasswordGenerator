import random
import tkinter as tk
from tkinter import messagebox

#All possible characters
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!@#%&*()_+-=[]{}|;:<>,.?/'

checkLower, checkUpper, checkNumber, checkSymbol = 0, 0, 0, 0

def generate_password():
    global checkLower, checkUpper, checkNumber, checkSymbol
    checkLower, checkUpper, checkNumber, checkSymbol = 0, 0, 0, 0
    try:
        size = int(pwsize.get())
        if size <= 12:
            raise ValueError("Must be a positive number bigger than 12")
    except ValueError as e:
        messagebox.showerror("Must be a positive number bigger than 12", str(e))
        return
    
    #Generating the character array and then joining it
    array = [random.choice(upper + lower + numbers + symbols) for _ in range(size)]
    checkIfPasswordIsStrong(array)
    password = ''.join(array)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def checkIfPasswordIsStrong(temparray):
    global checkLower, checkUpper, checkNumber, checkSymbol
    for char in temparray:
        if char.isupper():
            checkUpper += 1
        if char.islower():
            checkLower += 1
        if char.isnumeric():
            checkNumber += 1
        if char in symbols:
            checkSymbol += 1

    #Checks for the requirement of 1 lower,upper, number and symbol        
    if checkLower == 0 or checkUpper == 0 or checkNumber == 0 or checkSymbol == 0:
        generate_password()
    else:
        pass
        

#Tkinter UI
root = tk.Tk()
root.title("Password Generator")
label_size = tk.Label(root, text="Enter the size of the password:")
label_size.pack(pady=5)
pwsize = tk.Entry(root)
pwsize.pack(pady=5)
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=5)
entry_password = tk.Entry(root, width=50)
entry_password.pack(pady=5)
copy_button = tk.Button(root, text="Copy password", command=lambda: root.clipboard_append(entry_password.get()))
copy_button.pack(pady=2)

#Run APP
root.mainloop()


