import media
import fresh_tomatoes

# The following 6 movies are instances of the Movie class
blade_runner = media.Movie("Blade Runner",
							# Poster image source: https://madspoon.net/images/filmovi/blade-runner.jpeg
							"img/bladerunner.jpeg",
							"https://www.youtube.com/watch?v=eogpIG53Cis",
							1982,
							"Ridley Scott",
							"Neo-noir science fiction",
							media.Movie.VALID_RATINGS[3])

robocop = media.Movie("Robocop",
						# Poster image source: https://www.theterminatorfans.com/wp-content/uploads/2013/09/RoboCop-1987-Poster.jpg
						"img/robocop.jpg",
						"https://www.youtube.com/watch?v=qaNRzjGsOeA",
						1987,
						"Paul Verhoeven",
						"Cyberpunk action",
						media.Movie.VALID_RATINGS[3])

kill_bill = media.Movie("Kill Bill",
						# Poster image source: https://img.csfd.cz/files/images/user/profile/159/451/159451641_729a41.jpg
						"img/kill-bill.jpg",
						"https://www.youtube.com/watch?v=7kSuas6mRpk",
						2003,
						"Quentin Tarantino",
						"Martial arts action",
						media.Movie.VALID_RATINGS[3])

ghost_in_the_shell = media.Movie("Ghost in the Shell",
								# Poster image source: https://68.media.tumblr.com/bbf0183b4e3d85f806930d0dbc4dc756/tumblr_n9c3rc55Bp1qbluruo2_r1_1280.jpg
								"img/ghost.jpg",
								"https://www.youtube.com/watch?v=Dfqnbp8AJ9U",
								1995,
								"Mamoru Oshii",
								"Science fiction",
								media.Movie.VALID_RATINGS[3])

akira = media.Movie("Akira",
					# Poster image source: https://mindreels.files.wordpress.com/2013/07/akira.jpg
					"img/akira.jpg",
					"https://www.youtube.com/watch?v=pC6Qk5XxGIY",
					1988,
					"Katsuhiro Otomo",
					"Science fiction",
					media.Movie.VALID_RATINGS[3])

spirited_away = media.Movie("Spirited Away",
							# Poster image source: http://www.nausicaa.net/miyazaki/sen/poster_images/USA_full.jpg
							"img/spirited.jpg",
							"https://www.youtube.com/watch?v=ByXuk9QqQkk",
							2001,
							"Hayao Miyazaki",
							"Fantasy",
							media.Movie.VALID_RATINGS[1])

# List of movies containing the 6 movies above
movies = [blade_runner, robocop, kill_bill, ghost_in_the_shell, akira, spirited_away]

# Call the open_movies_page function with the movies list as an argument
fresh_tomatoes.open_movies_page(movies)