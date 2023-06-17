import requests
import json

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
    show.update(which_season)


with open('show_rating.json', 'w') as f:
    json.dump(show, f, indent=1)

print("check show_rating.json")
