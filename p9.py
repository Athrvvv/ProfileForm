from tkinter import *
from tkinter.messagebox import *
import sqlite3

def save():
    con = None
    try:
        con = sqlite3.connect("profile.db")
        cursor = con.cursor()
        sql = "insert into Profile values(?,?,?,?)"
        name = ent_name.get()
        contact = ent_contact.get()

        gender = "Male" if g.get() == 1 else "Female"

        prg_lang = ""
        if py.get():
            prg_lang += "Python "
        if jv.get():
            prg_lang += "Java "
        if js.get():
            prg_lang += "JavaScript "

        cursor.execute(sql, (name, contact, gender, prg_lang))
        con.commit()
        showinfo("Success", "Profile Received")
        ent_name.delete(0, END)
        ent_contact.delete(0, END)
        g.set(1)
        ent_name.focus()
    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

root = Tk()
root.title("Profile Form")
root.geometry("800x600")
f=("Arial", 14)

# Title Label
lab_title = Label(root, text="Profile Form", font=("Arial", 20, "bold"))
lab_title.grid(row=0, column=0, columnspan=2, pady=20)

# Name Label and Entry
lab_name = Label(root, text="Enter your name:", font=f)
lab_name.grid(row=1, column=0, padx=10, sticky='w')
ent_name = Entry(root, font=f)
ent_name.grid(row=1, column=1, padx=10)

# Contact Label and Entry
lab_contact = Label(root, text="Enter your phone number:", font=f)
lab_contact.grid(row=2, column=0, padx=10, sticky='w')
ent_contact = Entry(root, font=f)
ent_contact.grid(row=2, column=1, padx=10)

# Gender Label and Radiobuttons
lab_gender = Label(root, text="Gender:", font=f)
lab_gender.grid(row=3, column=0, padx=10, sticky='w')
g = IntVar()
g.set(1)
rb_male = Radiobutton(root, text="Male", variable=g, value=1, font=f)
rb_female = Radiobutton(root, text="Female", variable=g, value=2, font=f)
rb_male.grid(row=3, column=1, padx=10, sticky='w')
rb_female.grid(row=4, column=1, padx=10, sticky='w')

# Programming Languages Label and Checkbuttons
lab_prg = Label(root, text="Programming Languages:", font=f)
lab_prg.grid(row=5, column=0, padx=10, sticky='w')
py, jv, js = IntVar(), IntVar(), IntVar()
cb_py = Checkbutton(root, text="Python", variable=py, font=f)
cb_jv = Checkbutton(root, text="Java", variable=jv, font=f)
cb_js = Checkbutton(root, text="JavaScript", variable=js, font=f)
cb_py.grid(row=5, column=1, padx=10, sticky='w')
cb_jv.grid(row=6, column=1, padx=10, sticky='w')
cb_js.grid(row=7, column=1, padx=10, sticky='w')

# Submit Button
btn_submit = Button(root, text="Submit", font=f, command=save)
btn_submit.grid(row=8, column=1, pady=20)

root.mainloop()
