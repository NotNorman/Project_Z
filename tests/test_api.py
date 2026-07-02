from riot_api import get_account_info_by_puuid, get_account_info_by_riot_id

def test_get_account_info_by_puuid():
    puuid = "7lWXd76TB3lwlSy76XGwUj-fDBoJPqLHryvlq3JVIOk-kbhknMf5RaK57AEF5OPIYd6X2G6i8p9dyA"
    account_info = get_account_info_by_puuid(puuid)
    assert account_info is not None
    assert account_info['puuid'] == puuid

def test_get_account_info_by_riot_id():
    gameName = "Zeeshan Ahmad"
    tagLine = "Bkini"
    account_info = get_account_info_by_riot_id(gameName, tagLine)
    assert account_info is not None
    assert account_info['gameName'] == gameName
    assert account_info['tagLine'] == tagLine
    