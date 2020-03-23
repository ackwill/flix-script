import requests
import os

def search_movie():
    search_url = "https://yts.mx/api/v2/list_movies.json"

    print("Enter movie title: ")
    title = input("> ")

    search_params = {"query_term": title}

    response = requests.get(url = search_url, params = search_params)

    data = response.json()

    if data["status"] != "ok":
        return "Failed to connect"

    data = data["data"]
    movies = data["movies"]

    return movies


def get_torrent_url(movies):
    for count, movie in enumerate(movies):
        print(str(count+1) + ": " + movie["title_long"])

    print("\nEnter number for movie:")
    num = input("> ")

    try:
        num = int(num)
    except:
        print("Must enter numbers")
        return ""
    
    if num < 1 or num > len(movie):
        print("Number must correspond to movie")
        return ""
    
    movie = movies[num-1]

    valid = False

    while not valid:
        print("Select Torrent Quality:")

        for i, torrent in enumerate(movie["torrents"]):
            print(str(i+1) + ": Quality: " + torrent["quality"] + " Size: " + torrent["size"])

        print("Enter number for torrent")
        num = input("> ")

        try:
            num = int(num)
        except:
            print("Number must be an intger")
            next
        
        if num < 1 or num > len(movie["torrents"]):
            print("Select valid number")

        valid = True
    
    return movie["torrents"][num-1]["url"]


def start_peerflex(url):
    command = "peerflix " + url + " --vlc"
    os.system(command)



def start():
    movies = search_movie()

    if len(movies) < 1 or isinstance(movies, str):
        print("No results found")
        return

    

    torrent_url = ""

    while torrent_url == "":
        torrent_url = get_torrent_url(movies)

    print(torrent_url)

    start_peerflex(torrent_url)


if __name__ == "__main__":
    start()