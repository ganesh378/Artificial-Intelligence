frame(book(Author,Title,Year)):-
      atom(Author),atom(Title),integer(Year).
book("J.K.Rowling","Harry Potter",2022).
