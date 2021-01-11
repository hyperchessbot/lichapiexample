import requests
import json

username = "thibault"

r = requests.get(f"https://lichess.org/api/games/user/{username}?max=10", headers={'Accept': 'application/x-ndjson'})

games = r.text.split("\n")[:-1]

gamesJson = [json.loads(game) for game in games]

print(json.dumps(gamesJson, indent=2))
