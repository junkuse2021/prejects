import requests
import tkinter as tk
import json
from keys import API_KEY


all_seasons_ep_ratings = []

def save_episode_rating(all_seasons_ep_ratings, show):
    show["seasons"] = all_seasons_ep_ratings
    with open('episode_rating.json', 'w') as f:
        json.dump(show, f, indent=1)


def get_show_info(series_id):
    url = f"https://api.themoviedb.org/3/tv/{series_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": API_KEY
    }
    
    response = requests.get(url, headers=headers)
    response = response.json()
    return response



def get_episode_ratings(no_of_seasons, series_id):
    for i in range(no_of_seasons):
        url = f"https://api.themoviedb.org/3/tv/{series_id}/season/{i+1}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": API_KEY
        }

        response = requests.get(url, headers=headers)
        response = response.json()

        episodes = response['episodes']
        episode_rating = {}

        for episode in range(len(episodes)):
            rating = episodes[episode]['vote_average']
            episode_rating[f'E{episode+1}'] = rating
        
        which_season = {}
        which_season[f'S{i+1}'] = episode_rating
        all_seasons_ep_ratings.append(which_season)


    print("check episode_rating.json")

    tot_seasons = len(all_seasons_ep_ratings)
    return tot_seasons

def get_color(rating_val):
    red = int((10-rating_val) * 25.5)
    green = int(rating_val * 25.5)
    blue = 0
    return f"#{red:02x}{green:02x}{blue:02x}"


def display_data(no_of_seasons, series_id):
    root = tk.Tk()
    tot_seasons = get_episode_ratings(no_of_seasons, series_id)
    for i in range(tot_seasons):
        current_season = all_seasons_ep_ratings[i][f'S{i+1}'].values()
        episode_ratings = list(current_season)
        for eRating in range( len(episode_ratings)):
            color = get_color(episode_ratings[eRating])
            label = tk.Label(root, text=f"{' '*5}S{i+1} E{eRating+1}: {episode_ratings[eRating]}{' '*5}", bg=color, padx=10)
            label.grid(row=eRating, column=i)
    root.mainloop()


def main():
    default = 71712
    series_id = input("Enter the series id [default: good doctor]: ") or default
    series_id = int(series_id)
    show = {}

    show_details = get_show_info(series_id)
    no_of_seasons = show_details['number_of_seasons']
    show['number_of_seasons'] = no_of_seasons
    display_data(no_of_seasons, series_id)
    save_episode_rating(all_seasons_ep_ratings, show)


main()
