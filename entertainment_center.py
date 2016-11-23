import fresh_tomatoes
import media

the_wolf_of_wall_street = media.Movie ("The Wolf of Wall Street",
                  "A millionaire stock broker who loses it all",
                  "http://www.goldenglobes.com/sites/default/files/films/wolf_of_wall_street.jpeg",
                  "https://www.youtube.com/watch?v=iszwuX1AK6A")

the_big_short = media.Movie ("The Big Short",
                  "A movie about when the housing market crashed",
                  "http://www.impawards.com/2015/posters/big_short_ver3.jpg",
                  "https://www.youtube.com/watch?v=vgqG3ITMv1Q")


forest_gump = media.Movie ("Forest Gump",
                  "A story about a man who loves to run",
                  "http://www.impawards.com/1994/posters/forrest_gump.jpg",
                  "https://www.youtube.com/watch?v=bLvqoHBptjg")


the_pursuit_of_happiness = media.Movie ("The Pursuit of Happiness",
                  "A homeless man turned stock broker",
                  "http://fontmeme.com/images/The-Pursuit-of-Happyness-Poster.jpg",
                  "https://www.youtube.com/watch?v=doLdmYhpNyc")

the_social_network = media.Movie ("The Social Network",
                  "A movie about Facebook",
                  "http://www.wearemoviegeeks.com/wp-content/uploads/socialnetwork.jpg",
                  "https://www.youtube.com/watch?v=lB95KLmpLR4")

wall_street_money_never_sleeps = media.Movie ("Wall Street Money Never Sleeps",
                  "About a corrupt business man",
                  "http://api.comingsoon.net//images//2010/Wall_Street_Money_Never_Sleeps_Poster.jpg",
                  "https://www.youtube.com/watch?v=r1YjwFty7-I")

movies = [the_wolf_of_wall_street, the_big_short,
          forest_gump, the_pursuit_of_happiness, the_social_network, wall_street_money_never_sleeps]
""" This is a long line of code that represents a list of all the movies used """
print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
fresh_tomatoes.open_movies_page (movies)
