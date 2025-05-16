"""
This is a simple movie finder program that allows users to search for movies based on their wanted ratings and update the status of films (watched, not watched, or will rewatch).

"""
# Declare used libraries
import tkinter as tk
from tkinter import messagebox

""" 
List of 30 sci-fi movies with categorized ratings
Each movie is represented by a list with the following format:
[id, name, rating, status]
id: str - unique identifier of the movie (5 random characters)
name: str - name of the movie
rating: int - rating of the movie
status: int - status of the movie (0: Not Watched, 1: Watched, 2: Will rewatch)
"""

movies = [
    ["A1B2C", "The 5th Wave", 52, 0],
    ["D3E4F", "The Postman", 53, 0],
    ["G5H6I", "Waterworld", 58, 0],
    ["J7K8L", "Oblivion", 59, 0],
    ["M9N0O", "The Island", 55, 0],
    ["P1Q2R", "Tron: Legacy", 62, 0],
    ["S3T4U", "Pacific Rim", 66, 0],
    ["V5W6X", "Total Recall", 64, 0],
    ["Y7Z8A", "The Martian", 67, 0],
    ["B9C0D", "Gravity", 69, 0],
    ["E1F2G", "Looper", 79, 0],
    ["H3I4J", "Edge of Tomorrow", 78, 0],
    ["K5L6M", "Mad Max: Fury Road", 80, 0],
    ["N7O8P", "Blade Runner 2049", 82, 0],
    ["Q9R0S", "Interstellar", 84, 0],
    ["T1U2V", "The Matrix", 86, 0],
    ["W3X4Y", "Inception", 87, 0],
    ["Z5A6B", "The Terminator", 89, 0],
    ["C7D8E", "Minority Report", 87, 0],
    ["F9G0H", "Avengers: Endgame", 90, 0],
    ["I1J2K", "Dune", 91, 0],
    ["L3M4N", "Arrival", 92, 0],
    ["O5P6Q", "The Prestige", 93, 0],
    ["R7S8T", "Blade Runner", 92, 0],
    ["U9V0W", "Avengers: Infinity War", 95, 0],
    ["X1Y2Z", "2001: A Space Odyssey", 96, 0],
    ["A3B4C", "Star Wars: The Empire Strikes Back", 99, 0],
    ["D5E6F", "Star Wars: A New Hope", 98, 0],
    ["G7H8I", "The Dark Knight", 99, 0],
    ["J9K0L", "The Godfather", 100, 0]
]


# Sort movies by rating (descending) 
def sort_movies_by_rating():
    movies.sort(key=lambda x: x[2], reverse=True)



# Binary search to find movies with rating >= min_rating


def binary_search_movies(min_rating):
    left, right = 0, len(movies) - 1
    while left <= right:
        mid = (left + right) // 2
        if movies[mid][2] >= min_rating:
            left = mid + 1
        else:
            right = mid - 1
    return movies[:left]




# Find movies based on ID. If the ID is not found, it will return None.


def find_movie_by_id(query):
    for movie in movies:
        if movie[0].lower() == query.lower():
            return movie
    return None



# Update movie status
# Remember to enter a valid value. I use try and except here to prevent the user from entering a wrong value.

def update_movie_status(status):
    try:
        movie_id = entry_movie_id.get().strip()
        movie = find_movie_by_id(movie_id)
        if movie:
            movie[3] = status
            messagebox.showinfo("Success", f"Updated status of '{movie[1]}'!")
            find_movies()
        else:
            messagebox.showerror("Error", "Movie not found!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid movie ID!")



# Filter movies by status
def filter_movies_by_status(status):
    results = [movie for movie in movies if movie[3] == status]
    display_movies(results)




# Display movies with selected status
def display_movies(results):
    if results:
        header = f"{'ID':<8} {'Name':<40} {'Rating':<10} {'Status':<15}\n"
        separator = "-" * 80 + "\n"
        movie_list = "\n".join([
            f"{movie[0]:<8} {movie[1]:<40} {movie[2]:<10} {'Not Watched' if movie[3] == 0 else 'Watched' if movie[3] == 1 else 'Will Rewatch':<15}"
            for movie in results
        ])
        movie_display.config(state=tk.NORMAL)
        movie_display.delete(1.0, tk.END)
        movie_display.insert(tk.END, header + separator + movie_list)
        movie_display.config(state=tk.DISABLED)
    else:
        movie_display.config(state=tk.NORMAL)
        movie_display.delete(1.0, tk.END)
        movie_display.insert(tk.END, "No movies found with the selected criteria.")
        movie_display.config(state=tk.DISABLED)




# Display movies with rating >= min_rating
# Remember to enter a valid value. I use try and except here to prevent the user from entering a wrong value.
def find_movies():
    try:
        min_rating = int(entry_rating.get())
        results = binary_search_movies(min_rating)
    
        if results:
            header = f"{'ID':<8} {'Name':<40} {'Rating':<10} {'Status':<15}\n"
            separator = "-" * 80 + "\n"
            movie_list = "\n".join([
                f"{movie[0]:<8} {movie[1]:<40} {movie[2]:<10} {'Not Watched' if movie[3] == 0 else 'Watched' if movie[3] == 1 else 'Will Rewatch':<15}"
                for movie in results
            ])
            movie_display.config(state=tk.NORMAL)
            movie_display.delete(1.0, tk.END)
            movie_display.insert(tk.END, header + separator + movie_list)
            movie_display.config(state=tk.DISABLED)
        else:
            movie_display.config(state=tk.NORMAL)
            movie_display.delete(1.0, tk.END)
            movie_display.insert(tk.END, "No movies found with the selected criteria.")
            movie_display.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid rating!")




# Sort movies by rating for binary search and impressive display, it is also good when the user needs to find movies many times.
sort_movies_by_rating()


"""
After entering a value, you must keep it until you complete the "marking" process, 
which means labeling the movie as watched, not watched, or will rewatch. 

If you do not do the marking process, it's alright to enter a new value.

During the "marking" process, you can still enter a new a value, but the display will change.
"""
# Display
root = tk.Tk()
root.title("Movie Finder")
root.geometry("1920x1080")
# Function 1
label_rating = tk.Label(root, text="Enter minimum rating (0-100):")
label_rating.pack()
label_suggestion = tk.Label(root, text="\"Enter value 0 to display all movies\"")
label_suggestion.pack()
# Enter a number between 0 and 100 to find the movies, you can enter 0 to display all movies.
entry_rating = tk.Entry(root)
entry_rating.pack()
btn_find = tk.Button(root, text="Find Movies", command=find_movies)
btn_find.pack()

movie_display = tk.Text(root, height=20, width=80, font=("Courier", 10))
movie_display.pack()

# Function 2
label_movie_id = tk.Label(root, text="Enter movie ID to update status:")
label_movie_id.pack()
# Enter a movide ID to update the status of the movie, you can see the ID in the list of movies. 
# Otherwise, you can copy the ID by using Ctrl + C and paste it by using Ctrl + V.
entry_movie_id = tk.Entry(root)
entry_movie_id.pack()

btn_not_watched = tk.Button(root, text="Mark as Not Watched", command=lambda: update_movie_status(0))
btn_not_watched.pack()
btn_watched = tk.Button(root, text="Mark as Watched", command=lambda: update_movie_status(1))
btn_watched.pack()
btn_will_rewatch = tk.Button(root, text="Mark as Will Rewatch", command=lambda: update_movie_status(2))
btn_will_rewatch.pack()

# Function 3
label_movie_status = tk.Label(root, text="Filter movies by status:")
label_movie_status.pack()
# These three buttons are used to filter the movies by status, you can see the status in the list of movies
btn_show_not_watched = tk.Button(root, text="Show Not Watched", command=lambda: filter_movies_by_status(0))
btn_show_not_watched.pack()
btn_show_watched = tk.Button(root, text="Show Watched", command=lambda: filter_movies_by_status(1))
btn_show_watched.pack()
btn_show_will_rewatch = tk.Button(root, text="Show Will Rewatch", command=lambda: filter_movies_by_status(2))
btn_show_will_rewatch.pack()
root.mainloop()
