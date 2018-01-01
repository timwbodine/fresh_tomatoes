import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <script>
    //script to handle popovers for movie/show info
          $(document).ready(function(){
              $('[data-toggle="popover"]').popover();
          });
    </script>

    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .top-buffer { margin-top:40px; }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;

        //widen popover to full width of container and decrease font to
        //accomodate longer descriptions
        }
        .popover-content {
            font-size: 8px;
        }
        .popover {
            width = 100%;
        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <!-- Create separate sections for movies and shows. -->
    <div class="container">
        <div class="col-md-12 col-lg-12">
            <h1> Movies </h1>
        </div>
        {movie_tiles}
        <div class="col-md-12 col-lg-12">
            <h1> Shows </h1>
        </div>
        {show_tiles}
    </div>
  </body>

</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 top-buffer movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img data-toggle="popover" data-placement="bottom" data-trigger="hover" title="{movie_title}" data-content="{description}" src="{poster_image_url}" width="220" height="342"  >
    <h3 class="title">{movie_title}</h3>
</div>
'''
# A single show entry html template, links to main wiki and episodes section of wiki
show_tile_content = '''
<div class="col-md-6 col-lg-4 top-buffer movie-tile text-center">
    <a href="{wiki_link}">
        <img data-toggle="popover" data-placement="center" data-trigger="hover" title="{show_title}" data-content="{description}" src="{poster_image_url}" width="220" height="342">
    </a>
    <h3 class=title>{show_title}</h3>
    <h4><a href="{seasons_link}"> {seasons_number} Seasons </a><h4>


</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.representative_image,
            trailer_youtube_id=trailer_youtube_id,
            description = movie.description.encode('utf-8')
        )
    return content

def create_show_tiles_content(shows):
    # The HTML content for this section of the page
    content = ''
    for show in shows:
        # Append the tile for the show with its content filled in
        content += show_tile_content.format(
            show_title = show.title,
            poster_image_url=show.representative_image,
            wiki_link = show.wiki,
            seasons_link = show.wiki + "#Episodes",
            seasons_number = show.seasons,
            description = show.description

        )
    return content


def open_movies_page(movies, shows):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    # Replace the movie tiles and show tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        show_tiles=create_show_tiles_content(shows))


    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
