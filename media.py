class Movie():
    """This class stores movie related information."""

    # Class variable containing valid movie ratings. Referenced by each movie
    # object during instantiation.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, poster_image, trailer_youtube, release_date,
                 director, genre, mpaa_rating, imdb_rating):
        """
        Constructs an instance of the Movie class and assigns argument values
        to the instance variables.
        """
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.director = director
        self.genre = genre
        self.mpaa_rating = mpaa_rating
        self.imdb_rating = imdb_rating
