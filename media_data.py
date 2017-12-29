import media
import fresh_tomatoes
import wikipedia
import re

# array of movies' wikipedia pageid numbers, along with links to youtube trailers
movie_ids = [
['39469456', "https://youtu.be/dYJrxezWLUk"],
['9597495', "https://youtu.be/NZXi_vOkMyU"],
['20181213', "https://youtu.be/9LMMn8czq2w"],
['382387', "https://youtu.be/-14d51QTVjo"],
['5443971', "https://youtu.be/9-dIdFXeFhs"],
['25581548', 'https://youtu.be/P-y53CRSF9Q'],
['5515243', 'https://youtu.be/G8tHgGncPA0'],
['1134373', 'https://youtu.be/3nj5MMURCm8'],
['2829485', 'https://youtu.be/B3DcWtkKeIY']
]

# Create individual movie objects using wikipedia python package to interact with wikipedia API
movies = []
def build_movie_object(movie_id, trailer):
    wiki = wikipedia.page(pageid = movie_id)
    title = wiki.title
    plot = wiki.summary
    poster = find_poster(wiki.images)

    genre = wiki.categories[0]
    movie = media.Movie(title, plot, poster, trailer, genre)
    movies.append(movie)

#posters are apparently always the last jpeg on images object list due to the page layout
#so they can be gotten by iterating backwards through the list of image urls and
#grabbing the first .jpg via regex
def find_poster(images):
    for image in reversed(images):
        matchObj = re.search( '.jpg', image, re.M|re.I)
        if matchObj:
            #last .jpg in list = poster
            return image

# Iterate through movie_ids to create array of movie objects
for movie in movie_ids:
    build_movie_object(movie[0], movie[1])
    print(movies[-1].title + " loaded")

print("loading shows...")

# Manually assemble show objects (just for variety's sake)
parks_and_recreation = media.Show("Parks and Recreation", "Lesley Knope is a diligent parks department employee in Pawnee Indiana just trying to make a positive imact", "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.nbc.com%2Fsites%2Fnbcunbc%2Ffiles%2Ffiles%2F2013_0808_Parks_and_Rec_Show_KeyArt_1920x1080_0.jpg&f=1", 7, "https://en.wikipedia.org/wiki/Parks_and_Recreation", "comedy")
luther = media.Show("Luther", "A crime drama series starring Idris Elba as a near-genius murder detective whose brilliant mind can't always save him from the dangerous violence of his passions.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMWJiYTNjZDAtZDY2NS00YzA2LWE0MTAtMTQ0ZjAyMjQ1ZTQ1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_CR0,0,682,1000_AL_.jpg", 5, "https://en.wikipedia.org/wiki/Luther_(TV_series)", "crime drama")
the_wire = media.Show("The Wire", "Baltimore drug scene, seen through the eyes of drug dealers and law enforcement.", "https://images-na.ssl-images-amazon.com/images/M/MV5BNjc1NzYwODEyMV5BMl5BanBnXkFtZTcwNTcxMzU1MQ@@._V1_SY1000_CR0,0,735,1000_AL_.jpg", 5, "https://en.wikipedia.org/wiki/The_Wire", "crime drama")
shows = [parks_and_recreation, luther, the_wire]
print("Launching site with movie and show data...")

# Build page using shows and movies arrays
fresh_tomatoes.open_movies_page(movies, shows)
