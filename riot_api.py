import os
from dotenv import load_dotenv
import requests
load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")
account_v1_url = "https://americas.api.riotgames.com/riot/account/v1/"
match_v5_url = "https://americas.api.riotgames.com/lol/match/v5/matches/"

def get_account_info_by_riot_id(gameName, tagLine):
    api_path = f"{account_v1_url}accounts/by-riot-id/"

    url = f"{api_path}{gameName}/{tagLine}?api_key={API_KEY}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        account_info = response.json()
        return(account_info)
    else:
        print(f"Failed to retrieve data {response.status_code}")

def get_account_info_by_puuid(puuid):
    api_path = f"{account_v1_url}accounts/by-puuid/"

    url = f"{api_path}{puuid}/?api_key={API_KEY}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        account_info = response.json()
        return(account_info)
    else:
        print(f"Failed to retrieve data {response.status_code}")

def get_recent_matches_by_puuid(puuid):
    api_path = f"{match_v5_url}by-puuid/"

    url = f"{api_path}{puuid}/ids?start=0&count=20&api_key={API_KEY}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        match_ids = response.json()
        return(match_ids)
    else:
        print(f"Failed to retrieve data {response.status_code}")

account_info = get_account_info_by_puuid("7lWXd76TB3lwlSy76XGwUj-fDBoJPqLHryvlq3JVIOk-kbhknMf5RaK57AEF5OPIYd6X2G6i8p9dyA")

if account_info:
    print(f"{account_info['puuid']}")
    print(f"{account_info['gameName']}")
    print(f"{account_info['tagLine']}")

print(get_recent_matches_by_puuid("7lWXd76TB3lwlSy76XGwUj-fDBoJPqLHryvlq3JVIOk-kbhknMf5RaK57AEF5OPIYd6X2G6i8p9dyA"))