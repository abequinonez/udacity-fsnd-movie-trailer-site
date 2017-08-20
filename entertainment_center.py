# coding=utf-8
# This character encoding declaration was required in order to run
# the application without any errors. Encoding declaration learned
# from this Stack Overflow discussion:
# https://stackoverflow.com/questions/26899235/python-nltk-syntaxerror-non-ascii-character-xc3-in-file-senitment-analysis

import media
import fresh_tomatoes

# The following 6 movies are instances of the Movie class. Each movie
# object is created with unique arguments representing movie information.
blade_runner = media.Movie(
    "Blade Runner",
    # Poster image source: https://madspoon.net/images/filmovi/blade-runner.jpeg # NOQA
    "img/bladerunner.jpeg",
    "https://www.youtube.com/watch?v=eogpIG53Cis",
    1982,
    "Ridley Scott",
    "Neo-noir science fiction",
    media.Movie.VALID_RATINGS[3],
    8.2)

robocop = media.Movie(
    "RoboCop",
    # Poster image source: https://www.theterminatorfans.com/wp-content/uploads/2013/09/RoboCop-1987-Poster.jpg # NOQA
    "img/robocop.jpg",
    "https://www.youtube.com/watch?v=qaNRzjGsOeA",
    1987,
    "Paul Verhoeven",
    "Cyberpunk action",
    media.Movie.VALID_RATINGS[3],
    7.5)

kill_bill = media.Movie(
    "Kill Bill",
    # Poster image source: https://img.csfd.cz/files/images/user/profile/159/451/159451641_729a41.jpg # NOQA
    "img/kill-bill.jpg",
    "https://www.youtube.com/watch?v=7kSuas6mRpk",
    2003,
    "Quentin Tarantino",
    "Martial arts action",
    media.Movie.VALID_RATINGS[3],
    8.1)

the_revenant = media.Movie(
    "The Revenant",
    # Poster image source: http://s3.foxmovies.com/foxmovies/production/films/96/images/posters/455-film-page-large.jpg # NOQA
    "img/revenant.jpg",
    "https://www.youtube.com/watch?v=LoebZZ8K5N0",
    2015,
    "Alejandro González Iñárritu",
    "Western",
    media.Movie.VALID_RATINGS[3],
    8)

akira = media.Movie(
    "Akira",
    # Poster image source: https://mindreels.files.wordpress.com/2013/07/akira.jpg # NOQA
    "img/akira.jpg",
    "https://www.youtube.com/watch?v=pC6Qk5XxGIY",
    1988,
    "Katsuhiro Otomo",
    "Science fiction",
    media.Movie.VALID_RATINGS[3],
    8.1)

spirited_away = media.Movie(
    "Spirited Away",
    # Poster image source: http://www.nausicaa.net/miyazaki/sen/poster_images/USA_full.jpg # NOQA
    "img/spirited.jpg",
    "https://www.youtube.com/watch?v=ByXuk9QqQkk",
    2001,
    "Hayao Miyazaki",
    "Fantasy",
    media.Movie.VALID_RATINGS[1],
    8.6)

# List of movies containing the 6 movies above
movies = [blade_runner, robocop, kill_bill, the_revenant, akira, spirited_away]

# Call the open_movies_page() function with the movies list as an argument
fresh_tomatoes.open_movies_page(movies)
