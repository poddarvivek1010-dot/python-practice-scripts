class MovieRecord:
    # storing simple information about movies
    def __init__(self, movie_title, movie_genre):
        self.title = movie_title
        self.genre = movie_genre

    # function to print out the details
    def display_movie(self):
        print(f"Movie Title: {self.title}")
        print(f"Movie Genre: {self.genre}")


#Creating unique objects

# details of the first movie
movie_1 = MovieRecord("Inception", "Sci-Fi")

# details for the second movie
movie_2 = MovieRecord("The Lion King", "Animation")


#Running the class functions
print(" Displaying Movie Database....")
movie_1.display_movie()

print()  #for layout spacing

movie_2.display_movie()
