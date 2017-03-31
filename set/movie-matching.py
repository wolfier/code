# You've built an in-flight entertainment system with on-demand movie streaming.
# Users on longer flights like to start a second movie right when their first one ends,
# but they complain that the plane usually lands before they can see the ending.
# So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

# Write a function that takes an integer flight_length (in minutes)
# and a list of integers movie_lengths (in minutes) and returns a boolean
# indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

def find_movies( flight_length, movie_lengths ):
	seen_lengths = set()
	for length in movie_lengths:
		diff = flight_length - length
		if diff in seen_lengths:
			return True
		seen_lengths.add(diff)
	return False