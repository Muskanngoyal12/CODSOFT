from tkinter import Button, Entry, Label, Tk
from tkinter import *
import tkinter.messagebox as MessageBox

screen = Tk()
screen.title("CONTACT BOOK")
screen.geometry('600x400')
screen.configure(background ="yellow")

text=Label(screen, text="CONTACT INFORMATION")
text.configure(font =("calibiri", 50))
text.configure(background ="sky blue", foreground="red",width=30)
text.pack()
text.place(x=200, y=10)

contact_list = []

def clear_entries():
    global Name, Phone_No, Email, Address
    Name.delete(0,'end')
    Phone_No.delete(0, 'end')
    Email.delete(0, 'end')
    Address.delete(0,'end')


def insert_contact():
        name = Name.get()
        phone = Phone_No.get()
        email = Email.get()
        address = Address.get()

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contact_list.append(contact)
        MessageBox.showinfo("Success", "Contact inserted successfully.")
        clear_entries()

def display_contact():
        
        if contact_list:
            display_window = Toplevel()
            display_window.title("Contact List")
            for i, contact in enumerate(contact_list):
                for j, (key, value) in enumerate(contact.items()):
                    label = Label(display_window, text=f"   {key}: {value}")
                    label.grid(row=i, column=j, sticky="w")
        else:
            MessageBox.showinfo("Info", "No contacts to display.")
        clear_entries()

def Search_contact():
        search_name = Name.get()
        for contact in contact_list:
            if contact["Name"] == search_name:
                MessageBox.showinfo("Search Result", f"Phone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
                return
        MessageBox.showinfo("Search Result", "Contact not found.")
        clear_entries()

def update_contact():
        update_name = Name.get()
        for contact in contact_list:
            if contact["Name"] == update_name:
                contact["Phone"] = Phone_No.get()
                contact["Email"] = Email.get()
                contact["Address"] = Address.get()
                MessageBox.showinfo("Success", "Contact updated successfully.")
                return
        MessageBox.showinfo("Error", "Contact not found.")
        clear_entries()

def delete_contact():
        delete_name = Name.get()
        for contact in  contact_list:
            if contact["Name"] == delete_name:
                contact_list.remove(contact)
                MessageBox.showinfo("Success", "Contact deleted successfully.")
                return
        MessageBox.showinfo("Error", "Contact not found.")
        clear_entries()

Add_Contact=Button(screen, text="CREATE A NEW CONTACT",width=30,height=2, font=('calibiri', 12),fg='white', background="black", command=insert_contact)
Add_Contact.pack()
Add_Contact.place(x=50, y=600)

Display_Contact=Button(screen,text="DISPLAY CONTACT DETAILS", width=30, height=2, font=('calibiri', 12), background="black", fg="white", command=display_contact)
Display_Contact.pack()
Display_Contact.place(x=350, y=600)

Search_Contact1=Button(screen,text="SEARCH CONTACT DETAILS ", width=30, height=2, font=('calibiri', 12), background="black", fg="white", command=Search_contact)
Search_Contact1.pack()
Search_Contact1.place(x=650, y=600)

Update_Contact=Button(screen,text="UPDATE CONTACT DETAILS", width=30, height=2, font=('calibiri', 12), background="black", fg="white", command=update_contact)
Update_Contact.pack()
Update_Contact.place(x=950, y=600)

Delete_Contact = Button(screen, text="DELETE CONTACT",width=30,height=2, font=('calibiri', 12),fg='white', background="black" , command= delete_contact)
Delete_Contact.pack()
Delete_Contact.place(x=1250, y=600)


label1=Label(screen, text="ENTER THE NAME OF THE PERSON", width=40, height=2, font=('calibiri', 14))
label1.pack()
label1.place(x=80, y=100)

label2=Label(screen, text="ENTER THE PHONE NUMBER OF THE PERSON", width=40, height=2, font=('calibiri', 14))
label2.pack()
label2.place(x=80, y=180)

label3=Label(screen, text="ENTER THE E-MAIL ADDRESS OF THE USER", width=40, height=2, font=('calibiri', 14))
label3.pack()
label3.place(x=80, y=260)

label4=Label(screen, text="ENTER THE ADDRESS OF EACH CONTACT", width=40, height=2, font=('calibiri', 14))
label4.pack()
label4.place(x=80, y=340)

Name=Entry(screen, font=('calibiri', 14, 'normal'))
Name.pack()
Name.place(x=550, y=120)

Phone_No=Entry(screen, font=('calibiri', 14, 'normal'))
Phone_No.pack()
Phone_No.place(x=550, y=200)

Email=Entry(screen, font=('calibiri', 14, 'normal'))
Email.pack()
Email.place(x=550, y=280)
   
Address=Entry(screen, font=('calibiri', 14, 'normal'))
Address.pack()
Address.place(x=550, y=360)


screen.mainloop()

