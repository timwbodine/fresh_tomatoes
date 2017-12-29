# ud036_StarterCode
This is the first project in the Udacity full stack web development nanodegree.  It is essentially a page listing movies and shows I like.
The main change made from the starter code is adding a class for shows, as distinct from movies.
Movies and Shows are displayed in two sections.  When clicked, movies show trailers while shows link to the show's wiki.  You can also hover over any movie or show for more data about it.  I used the IMDbPY package to retrieve movie data from the IMDB API.
UPDATE: IMDbPY data retrieval was broken due to IMDB redesign.  As a substitute I am using wikipedia
API via the wikipedia python package.  Instructions amended for this changed requirement.

## QuickStart
1. Clone or download this repo
2. Ensure that you have python 3 installed.
3. Install the wikipedia python library using pip install wikipedia
4. run media_data.py and check out some of my favorite movies and shows.
