import fresh_tomatoes
import media 

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to li", "https://upload.wikimedia.org/wikipedia/en/1/13/toy_sory.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")
						
#print (toy_sory.storyline)
avatar = media.Movie("Avatar",
                     "A rine on adfaffds",
                     "https://www.wikimedia.org/static/images/project-logos/mediawikiwiki.png",
					 "https://www.youtube.com/watch?v=B7bqAsxee4I")
					 
school_of_rock = media.Movie("School of Rock",
                     "any description",
                     "https://www.wikimedia.org/static/images/project-logos/mediawikiwiki.png",
					 "https://www.youtube.com/watch?v=eNHJjGkTLy4")
					 
any_instance  = media.Movie("any instance",
                     "any description",
                     "https://www.wikimedia.org/static/images/project-logos/mediawikiwiki.png",
					 "https://www.youtube.com/watch?v=eNHJjGkTLy4")

toy_stor = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to li", "https://upload.wikimedia.org/wikipedia/en/1/13/toy_sory.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")
						
#print (toy_sory.storyline)
avata = media.Movie("Avatar",
                     "A rine on adfaffds",
                     "https://www.wikimedia.org/static/images/project-logos/mediawikiwiki.png",
					 "https://www.youtube.com/watch?v=B7bqAsxee4I")
movies = (avata, toy_stor,  toy_story, any_instance ,school_of_rock, avatar)					 
fresh_tomatoes.open_movies_page(movies)

print (media.Movie.__doc__)