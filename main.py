#JH UI: The trick is to use small width and height
import tkinter as tk

def add_f():
    x=entry_web.get()
    y=entry_email.get()
    z=entry_password.get()
    with open("Results.txt","a") as results:
        results.write(f" {x} | {y} | {z} \n")

    entry_web.delete(0,tk.END)
    entry_password.delete(0, tk.END)




window1=tk.Tk()
window1.title("Password Manager")
window1.config (padx=30, pady=30)

canvas1= tk.Canvas(width=200,height=200)
photo1=tk.PhotoImage(file="logo.png")
canvas1.create_image(125,100,image=photo1,state="normal") #the numbers are x and y
# canvas1.grid(column=2,row=0)
canvas1.grid(column=1,row=0)

website_label=tk.Label(text="Webiste")
website_label.grid(column=0,row=1)

email_label=tk.Label(text="Email")
email_label.grid(column=0,row=2)

password_label=tk.Label(text="Password")
password_label.grid(column=0,row=3)

entry_web = tk.Entry(width=30, font=("Helvetica", 22))
entry_web.grid(column=1,row=1,columnspan=2)
entry_web.focus()

entry_email = tk.Entry(width=30, font=("Helvetica", 22))
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "something@email.com")

entry_password = tk.Entry(width=20, font=("Helvetica", 14))
entry_password.grid(column=1, row=3)

button1 = tk.Button(text="Generate Password", width=15,font=("Helvetica", 12),fg="Blue",bg="white")
button1.grid(column=2, row=3)

button2 = tk.Button(text="Add", width=7,font=("Helvetica", 15),fg="Blue",bg="white",command=add_f)
button2.grid(column=1, row=4)

window1.mainloop()