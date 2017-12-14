import media
import fresh_tomatoes

texas_chainsaw_massacre = media.Movie("The Texas Chainsaw Massacre", "Kids get trapped with a family of crazy cannibals", "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.insidethemagic.net%2Fwp-content%2Fuploads%2F2016%2F04%2FThe-Texas-Chain-Saw-Massacre-Comes-to-Universal-Orlandos-Halloween-Horror-Nights.jpg&f=1","https://youtu.be/AKqFfkassgo","horror")
parks_and_recreation = media.Show("Parks and Recreation", "Lesley Knope is a diligent parks department employee in Pawnee Indiana just trying to make a positive imact", "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.nbc.com%2Fsites%2Fnbcunbc%2Ffiles%2Ffiles%2F2013_0808_Parks_and_Rec_Show_KeyArt_1920x1080_0.jpg&f=1", 7, "https://en.wikipedia.org/wiki/Parks_and_Recreation", "comedy")

movies = [texas_chainsaw_massacre]
shows = [parks_and_recreation]
fresh_tomatoes.open_movies_page(movies, shows)
