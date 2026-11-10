# Movie class project
class MovieRecord:
    # storing simple information about movies
    def __init__(self, movie_title, movie_genre, movie_leads, movie_co_stars):
        self.title = movie_title
        self.genre = movie_genre
        self.leads = movie_leads
        self.co_stars = movie_co_stars

    # function to print out the details
    def display_movie(self):
        print(f"Movie Title: {self.title}")
        print(f"Movie Genre: {self.genre}")
        print(f"Movie Lead Actors: {self.leads}")
        print(f"Movie Co Stars: {self.co_stars}")

#Creating unique objects

# details of the first movie
movie_1 = MovieRecord("Inception", "Sci-Fi", "Leonardo Di Caprio", "Joseph Gordon Levitt, Cillian Murphy, Tom Hardy and more...")

# details of the second movie
movie_2 = MovieRecord("Dead Poet Society", "Class Drama and Poetry", "Robin Williams", "Robert Sean Leonard and Ethan Hawke")

# detail of the third movie
movie_3 = MovieRecord("Good Will Hunting", "Psychological Drama", "Matt Damon", "Robin Williams and Ben Affleck")

# detail of the fourth movie
movie_4 = MovieRecord("Interstellar", "Sci-Fi", "Matthew McConaughey", "Anne Hathaway, Jessica Chastain and more...")

#Running the class functions
print("Displaying Movie Database....")
movie_1.display_movie()

print()  #for layout spacing

movie_2.display_movie()

print()

movie_3.display_movie()

print()

movie_4.display_movie()
