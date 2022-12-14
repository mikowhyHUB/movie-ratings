from tkinter import *
from backend import Database

database = Database('films.db')


def get_selected_row(event):
    # protecting program from index error
    try:
        global selected_tuple
        index = list_films.curselection()[0]  # grabing index 0 of the tuple
        selected_tuple = list_films.get(index)
        # item shows in entry box after selecting(then you can update it)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    # clearing list every time when we press view  button
    list_films.delete(0, END)
    for row in database.view_list():
        list_films.insert(END, row)


def search_command():

    list_films.delete(0, END)
    for row in database.search(title_text.get(), year_text.get(), director_text.get(), rating_text.get()):
        list_films.insert(END, row)


def add_command():
    database.add_film(title_text.get(), year_text.get(),
                      director_text.get(), rating_text.get())
    list_films.delete(0, END)
    list_films.insert(END, (title_text.get(), year_text.get(),
                      director_text.get(), rating_text.get()))


def delete_command():
    database.delete(selected_tuple[0])
    # restarting list after deleting item
    list_films.delete(0, END)


def update_command():
    database.update(selected_tuple[0], title_text.get(
    ), year_text.get(), director_text.get(), rating_text.get())


window = Tk()
window.title('Movie Ratings')
# assigning labels
l1 = Label(window, text='Film')
l1.grid(row=6, column=0)

l2 = Label(window, text='Year')
l2.grid(row=7, column=0)

l3 = Label(window, text='Director')
l3.grid(row=6, column=2)

l4 = Label(window, text='Rating')
l4.grid(row=7, column=2)
# assigining entry boxes
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=6, column=1)

year_text = StringVar()
e2 = Entry(window, textvariable=year_text)
e2.grid(row=7, column=1)

director_text = StringVar()
e3 = Entry(window, textvariable=director_text)
e3.grid(row=6, column=3)

rating_text = StringVar()
e4 = Entry(window, textvariable=rating_text)
e4.grid(row=7, column=3)
# assigning listbox
list_films = Listbox(window, height=8, width=35)
list_films.grid(row=0, column=0, columnspan=2, rowspan=6)
# assigning scrollbar to list of films
scrollbar = Scrollbar(window)
scrollbar.grid(row=1, column=2)

# list_films.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=list_films.yview)

list_films.bind('<<ListboxSelect>>', get_selected_row)
# assigining buttons
b0 = Button(window, text='View all', width=12, command=view_command)
b0.grid(row=0, column=3)

b1 = Button(window, text='Search', width=12, command=search_command)
b1.grid(row=1, column=3)

# b2 = Button(window, text='Sort', width=12)
# b2.grid(row=2, column=3)

b3 = Button(window, text='Delete', width=12, command=delete_command)
b3.grid(row=3, column=3)

b4 = Button(window, text='Update', width=12, command=update_command)
b4.grid(row=4, column=3)

b5 = Button(window, text='Add', width=12, command=add_command)
b5.grid(row=5, column=3)

window.mainloop()
