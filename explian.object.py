class Movie:
    def __init__(self,title,director,release_year,genre):
        self.title=title
        self.director=director
        self.release_year=release_year
        self.genre=genre


    def display_task(self):
        
        print(f"Title :{self.title}")
        print(f"Director :{self.director}")
        print(f"Release_year :{self.release_year}")
        print(f"Genre :{self.genre}")
        print("")
    
    def update_director(self,new_dirictor):

        self.director=new_dirictor


movie1=Movie("inception","christopher nolan",2010,"sci-fi")
movie2=Movie("The godfather","francis ford coppola",1972,"crime")
movie3=Movie("Prasita","bong joon",2019,"Thriller")



print("_______Movies list_______")
print("")
movie1.display_task()
movie2.display_task()
movie3.display_task()

movie1.update_director("jackchan")
movie2.update_director("Ahmed mazher")
movie3.update_director("noor hamed")


print("_______Changing movie directors _______")

movie1.display_task()
movie2.display_task()
movie3.display_task()