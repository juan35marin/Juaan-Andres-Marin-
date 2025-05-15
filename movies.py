movies = {}

def add_movie(title):
    if title not in movies:
        movies[title] = []
        print(f"Movie '{title}' added.")
    else:
        print("Movie already exists.")

def add_rating(title, rating):
    if title in movies:
        if 1 <= rating <= 5:
            movies[title].append(rating)
            print("Rating added.")
        else:
            print("Rating must be between 1 and 5.")
    else:
        print("Movie not found.")

def average_rating(title):
    if title in movies:
        ratings = movies[title]
        if ratings:
            avg = sum(ratings) / len(ratings)
            print(f"Average rating for '{title}': {avg:.2f}")
        else:
            print("This movie has no ratings yet.")
    else:
        print("Movie not registered.")
