import media
import fresh_tomatoes
import wikipedia
import re

# array of movies' wikipedia pageid numbers,
# along with links to youtube trailers
movie_ids = [
            ['39469456', "https://youtu.be/dYJrxezWLUk"],
            ['9597495', "https://youtu.be/NZXi_vOkMyU"],
            ['582398', "https://youtu.be/eI6Ol7aX6mk"],
            ['382387', "https://youtu.be/-14d51QTVjo"],
            ['5443971', "https://youtu.be/9-dIdFXeFhs"],
            ['213246', 'https://youtu.be/-qJjiq72WOo'],
            ['5515243', 'https://youtu.be/G8tHgGncPA0'],
            ['1134373', 'https://youtu.be/3nj5MMURCm8'],
            ['2829485', 'https://youtu.be/B3DcWtkKeIY']
            ]

# Create individual movie objects using wikipedia
# python package to interact with wikipedia API
movies = []


def build_movie_object(movie_id, trailer):
    wiki = wikipedia.page(pageid=movie_id)
    title = wiki.title
    plot = wiki.summary
    poster = find_poster(wiki.images, title)
    genre = wiki.categories[0]
    movie = media.Movie(title, plot, poster, trailer, genre)
    movies.append(movie)

# To find the poster we first strip out useless characters
# and capitalization in the title.
# Then we do the same for the image name.
# Then we check all the images for any mention of the word "poster"
# Then if that doesn't work we check for the name of the film itself.
# This seems to pretty much always find the right image.


def find_poster(images, title):

    title_stripped = ("".join(title[0:title.find("(")].split(" "))).lower()
    if title_stripped.startswith('the'):
        title_stripped = title_stripped[3:-1]
    for image in images:
        image_stripped = "".join(re.split('/|_|-|\.', image.lower()))
        if image_stripped.find("poster") > -1:
            print(image)
            return image
    for image in images:
        image_stripped = "".join(re.split('/|_|-|\.', image.lower()))
        if image_stripped.find(title_stripped) > -1:
            print(image)
            return image
    return images[-1]

# Iterate through movie_ids to create array of movie objects
for movie in movie_ids:
    build_movie_object(movie[0], movie[1])
    print(movies[-1].title + " loaded")

print("loading shows...")

# Manually assemble show objects (just for variety's sake)
descriptions = [("Lesley Knope is a diligent parks department employee in "
                 "Pawnee Indiana just trying to make a positive imact"),
                ("A crime drama series starring Idris Elba as a near-genius"
                 " murder detective whose brilliant mind can't always save"
                 " him from the dangerous violence of his passions."),
                ("Baltimore drug scene, seen through the eyes of drug dealers"
                 " and law enforcement.")]
images = [("https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.nbc.com%2"
           "Fsites%2Fnbcunbc%2Ffiles%2Ffiles%2F2013_0808_Parks_and_Rec_Show"
           "_KeyArt_1920x1080_0.jpg&f=1"),
          ("https://images-na.ssl-images-amazon.com/images/M/MV5BMWJiYTNjZDAtZ"
           "DY2NS00YzA2LWE0MTAtMTQ0ZjAyMjQ1ZTQ1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._"
           "V1_SY1000_CR0,0,682,1000_AL_.jpg"),
          ("https://images-na.ssl-images-amazon.com/images/M/MV5BNjc1NzYwOD"
           "EyMV5BMl5BanBnXkFtZTcwNTcxMzU1MQ@@._V1_SY1000_CR0,0,735,1000_AL"
           "_.jpg")]
wikis = [("https://en.wikipedia.org/wiki/Parks_and_Recreation"),
         ("https://en.wikipedia.org/wiki/Luther_(TV_series)"),
         ("https://en.wikipedia.org/wiki/The_Wire")]
parks_and_recreation = media.Show("Parks and Recreation",
                                  descriptions[0],
                                  images[0],
                                  7,
                                  wikis[0],
                                  "comedy")
luther = media.Show("Luther",
                    descriptions[1],
                    images[1],
                    5,
                    wikis[1],
                    "crime drama")
the_wire = media.Show("The Wire",
                      descriptions[2],
                      images[2],
                      5,
                      wikis[2],
                      "crime drama")
shows = [parks_and_recreation, luther, the_wire]
print("Launching site with movie and show data...")

# Build page using shows and movies arrays
fresh_tomatoes.open_movies_page(movies, shows)
