from tkinter import *
'''
Dodać: nazwę, rezysera, rok produkcji, ocena, opcje, lista filmów

Uzytkownik moze:
-prejrzeć wszystkie filmy
-wyszukać film
-segregowac filmy po ocenie
-segregować po roku produkcji
-updateowac inofmracje o filmie
-usuwać film
'''

window = Tk()

l1 = Label(window, text='Film')
l1.grid(row=5, column=0)

l2 = Label(window, text='Year')
l2.grid(row=6, column=0)

l3 = Label(window, text='Director')
l3.grid(row=5, column=2)

l4 = Label(window, text='Rating')
l4.grid(row=6, column=2)

film_text = StopIteration()
e1 = Entry(window, textvariable=film_text)
e1.grid(row=5, column=1)

year_text = StopIteration()
e2 = Entry(window, textvariable=year_text)
e2.grid(row=6, column=1)

director_text = StopIteration()
e3 = Entry(window, textvariable=director_text)
e3.grid(row=5, column=3)

rating_text = StopIteration()
e4 = Entry(window, textvariable=rating_text)
e4.grid(row=6, column=3)

list_films = Listbox(window, height=6, width=35)
list_films.grid(row=0, column=0, columnspan=2, rowspan=6)

scrollbar = Scrollbar(window)
scrollbar.grid(row=1, column=2)
# assigning scrollbar to list of films
list_films.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_films.yview)

b1 = Button(window, text='Search', width=12)
b1.grid(row=0, column=3)

b2 = Button(window, text='Sort', width=12)
b2.grid(row=1, column=3)

b4 = Button(window, text='Delete', width=12)
b4.grid(row=2, column=3)

b5 = Button(window, text='Update', width=12)
b5.grid(row=3, column=3)

b6 = Button(window, text='Add', width=12)
b6.grid(row=4, column=3)


window.mainloop()
