class Genre:
    def __init__(self, name:str):
        self.name:str = name

class Ticket:
    def __init__(self, price:float, seat_number:str):
        self.price:float = price
        self.seat_number:str = seat_number
    
    def get_ticket_info(self):
        return f"Price: ${self.price}, Seat Number: {self.seat_number}"


class Poster:
    def __init__(self, release_date:str, tagline:str):
        self.release_date:str = release_date
        self.tagline:str = tagline

class Cinema:
    def __init__(self, title:str, director:str, genre_name:str, price:float, seat_number:str, release_date:str, tagline:str):
        self.title:str = title
        self.director:str = director
        self.genre:Genre = Genre(genre_name)
        self.ticket:Ticket = Ticket(price, seat_number)
        self.poster:Poster = Poster(release_date, tagline)

    def get_info(self):
        return (f"Title: {self.title}, Director: {self.director}, "
                f"{self.ticket.get_ticket_info()}, ")

hall1:Cinema = Cinema('Stranger thing', 'Tom Holland', 'Action', 24.99, '12A', '01/22/26', 'Comming soon')