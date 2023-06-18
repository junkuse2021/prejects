import requests
import tkinter as tk
import json



def get_color(rating_val):
    red = int((10-rating_val) * 25.5)
    green = int(rating_val * 25.5)
    blue = 0
    return f"#{red:02x}{green:02x}{blue:02x}"


default = 71712
series_id = input("Enter the series id [default: good doctor]: ") or default
series_id = int(series_id)
url = f"https://api.themoviedb.org/3/tv/{series_id}?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmUzOWNkMzIzZjgwM2U5YWVjNDc3YzY5NDA5Yjk3NyIsInN1YiI6IjY0OGQyNTg0MjYzNDYyMDE0ZTU3NjJjZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gU3Ez4fyvsvn5cMs-jwavvW1eoqf-FxxSCFkP8j19Do"
}

response = requests.get(url, headers=headers)
response = response.json()
with open('show_details.json', 'w') as f:
    json.dump(response, f, indent=1)

with open('show_details.json', 'r') as f:
    show_details = json.load(f)

show = {}
all_seasons = []

no_of_seasons = show_details['number_of_seasons']
show['number_of_seasons'] = no_of_seasons
for i in range(no_of_seasons):
    url = f"https://api.themoviedb.org/3/tv/{series_id}/season/{i+1}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmUzOWNkMzIzZjgwM2U5YWVjNDc3YzY5NDA5Yjk3NyIsInN1YiI6IjY0OGQyNTg0MjYzNDYyMDE0ZTU3NjJjZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gU3Ez4fyvsvn5cMs-jwavvW1eoqf-FxxSCFkP8j19Do"
    }

    response = requests.get(url, headers=headers)
    response = response.json()

    with open('show_season.json', 'w') as f:
        json.dump(response, f, indent=1)

    with open('show_season.json', 'r') as f:
        tv_season = json.load(f)

    episodes = tv_season['episodes']
    episode_rating = {}

    for episode in range(len(episodes)):
        rating = episodes[episode]['vote_average']
        episode_rating[f'E{episode+1}'] = rating
    
    which_season = {}
    which_season[f'S{i+1}'] = episode_rating
    all_seasons.append(which_season)

show["seasons"] = all_seasons
with open('show_rating.json', 'w') as f:
    json.dump(show, f, indent=1)

print("check show_rating.json")
tot_seasons = len(all_seasons)


root = tk.Tk()
for i in range(tot_seasons):
    current_season = all_seasons[i][f'S{i+1}'].values()
    episode_ratings = list(current_season)
    for eRating in range( len(episode_ratings)):
        color = get_color(episode_ratings[eRating])
        label = tk.Label(root, text=f"{' '*5}S{i+1} E{eRating+1}: {episode_ratings[eRating]}{' '*5}", bg=color, padx=10)
        # label.pack()
        label.grid(row=eRating, column=i)
root.mainloop()
