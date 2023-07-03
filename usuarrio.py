from tkinter import *
root = Tk()
root.title("Herencia")
root.geometry("600x600")
label_name = Label(root, text="Nombre del usuario: ")
label_name.place(relx=0.3,rely=0.2, anchor=CENTER)
entry_name = Entry(root)
entry_name.place(relx=0.6,rely=0.2, anchor=CENTER)
label_email = Label(root, text="Correo electrónico: ")
label_email.place(relx=0.3,rely=0.3, anchor=CENTER)
entry_email = Entry(root)
entry_email.place(relx=0.6,rely=0.3, anchor=CENTER)
label = Label(root)
dictionary = {}

class Users():
    def AddUser(key, value):
        global dictionary
        dictionary[key] = value
        label["text"] = dictionary
            
class GetUsers(Users):
    def GetUser(self):
        username = entry_name.get()
        email_id = entry_email.get()
        Users.AddUser(username, email_id)
        
        
user = GetUsers()
btn = Button(root, text="agregar detalles del usuario", command=user.GetUser)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()