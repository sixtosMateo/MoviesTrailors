import media
import fresh_tomatoes

# Rocky movie: movie title, movie poster, trailer link
rocky = media.Movie(
        "Rocky",
        "https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
        "https://www.youtube.com/watch?v=7RYpJAUMo2M"
                   )

# Prefontaine movie:  movie title, movie poster, trailer link
prefontaine = media.Movie(
        "Without Limits",
        "https://upload.wikimedia.org/wikipedia/en/7/7f/Without_limits.jpg",
        "https://www.youtube.com/watch?v=aQojAJAClIY&t=19s"
                    )

# saving_private_ryan movie: movie title, movie poster, trailer link
saving_private_ryan = media.Movie(
        "Saving Private Ryan",
        "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=e2MpP3M9oCk"
                    )
# striped_pajama movie: movie title, movie poster, trailer link
striped_pajama = media.Movie(
        "The boy in the striped pyjamas",
        "https://upload.wikimedia.org/wikipedia/en/3/34/Theboyposter.jpg",
        "https://www.youtube.com/watch?v=9ypMp0s5Hiw"
                    )
# war_z movie: movie title, movie poster, trailer link
war_z = media.Movie(
        "World War Z",
        "https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=HcwTxRuq-uk"
                    )
# jeeper_creepers movie: movie title, movie poster, trailer link
jeeper_creepers = media.Movie(
        "Jeepers Creepers",
        "https://upload.wikimedia.org/wikipedia/en/6/6d/Jeepers_Creepers_film.jpg",  # NOQA
        "https://www.youtube.com/watch?v=ouUO42AkZV0"
                    )


# create list with instances: rocky,
# prefontaine, striped_pajama,war_z, jeeper_creepers
movies_list = [rocky, prefontaine, saving_private_ryan,
               striped_pajama, war_z, jeeper_creepers]


# function will call the html file that displays the set of movies'
# trailers from fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies_list)
