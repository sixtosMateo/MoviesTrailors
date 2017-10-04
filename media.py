class Movie():
    """This class is the structure of each movie instance."""
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """The init function will allow to set value to the class varibles"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
