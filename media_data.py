import media
import fresh_tomatoes
import imdb

# list of movies' imdb ID numbers, along with links to youtube trailers
movie_ids = [['2428170','https://youtu.be/Kh-RXUh84NM'], ['2388715', "https://youtu.be/dYJrxezWLUk"], ['0051383', "https://youtu.be/NZXi_vOkMyU"], ['0069293', "https://youtu.be/9LMMn8czq2w"], ['0087363', "https://youtu.be/-14d51QTVjo"], ['0368226', "https://youtu.be/9-dIdFXeFhs"], ['1316037', 'https://youtu.be/P-y53CRSF9Q'], ['0450345', 'https://youtu.be/G8tHgGncPA0'], ['0072271', "https://youtu.be/AKqFfkassgo"]]
movies = []

# Create individual movie objects using IMDbPY API
def build_movie_object(movie_id, trailer):
    imdb_access = imdb.IMDb()
    info = imdb_access.get_movie(movie_id)
    title = info['title']
    plot = info['plot outline']
    poster = info['cover url']
    genre = info['genres']
    movie = media.Movie(title, plot, poster, trailer, genre)
    movie.show_attributes()
    movies.append(movie)

# Iterate through movie_ids to create array of movie objects
for movie in movie_ids:
    build_movie_object(movie[0], movie[1])

# Manually assemble show objects
parks_and_recreation = media.Show("Parks and Recreation", "Lesley Knope is a diligent parks department employee in Pawnee Indiana just trying to make a positive imact", "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.nbc.com%2Fsites%2Fnbcunbc%2Ffiles%2Ffiles%2F2013_0808_Parks_and_Rec_Show_KeyArt_1920x1080_0.jpg&f=1", 7, "https://en.wikipedia.org/wiki/Parks_and_Recreation", "comedy")
luther = media.Show("Luther", "A crime drama series starring Idris Elba as a near-genius murder detective whose brilliant mind can't always save him from the dangerous violence of his passions.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMWJiYTNjZDAtZDY2NS00YzA2LWE0MTAtMTQ0ZjAyMjQ1ZTQ1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_CR0,0,682,1000_AL_.jpg", 5, "https://en.wikipedia.org/wiki/Luther_(TV_series)", "crime drama")
the_wire = media.Show("The Wire", "Baltimore drug scene, seen through the eyes of drug dealers and law enforcement.", "https://images-na.ssl-images-amazon.com/images/M/MV5BNjc1NzYwODEyMV5BMl5BanBnXkFtZTcwNTcxMzU1MQ@@._V1_SY1000_CR0,0,735,1000_AL_.jpg", 5, "https://en.wikipedia.org/wiki/The_Wire", "crime drama")
shows = [parks_and_recreation, luther, the_wire]

# Build page using shows and movies arrays
fresh_tomatoes.open_movies_page(movies, shows)
