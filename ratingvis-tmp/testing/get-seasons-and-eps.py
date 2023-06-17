import json

with open('./tv-series-details.json') as f:
    data = json.load(f)

no_of_seasons = data['number_of_seasons']
show = []
for season in range(1, no_of_seasons+1):
    current_season = {}
    no_of_eps = data['seasons'][season-1]['episode_count']
    strr = f'season_{season}'
    current_season[strr] = no_of_eps
    show.append(current_season)

print(show)
