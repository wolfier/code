# Source: Interview Cakes

# You've built an in-flight entertainment system with on-demand movie streaming.
# Users on longer flights like to start a second movie right when their first one ends,
# but they complain that the plane usually lands before they can see the ending.
# So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

# Write a function that takes an integer flight_length (in minutes)
# and a list of integers movie_lengths (in minutes) and returns a boolean
# indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
 
def find_movies( flight_length, movie_lengths ):
	seen_lengths = set()

	# Loop through the movies
	for length in movie_lengths:
		# Find the difference bewteen a movie and the flight length
		# the result is the length of the second movie
		diff = flight_length - length
		# If the movie length is in the set meaning it will fulfil the rest of the flight time
		if diff in seen_lengths:
			return True
		# Otherwise add the difference to the set for other movies 
		seen_lengths.add(diff)
	return False