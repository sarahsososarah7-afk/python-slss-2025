# Helper for searching through Spotify results

import csv


def songs_by_artist(file_path: str, artist: str) -> list[list[str]]:
    """Searches through given file and returns a list of songs from given artist."""
    artist_col = 2

    songs = []

    # open the file
    with open(file_path) as f:
        # get rid of the header row
        _ = f.readline()

        # create a reader object
        r = csv.reader(f)

        # go through reader line by line
        for info in r:
            # if the current artist is "Kendrick"
            if info[artist_col] == artist:
                songs.append(info)

    return songs


def track_search(file_path: str, word: str) -> list[list[str]]:
    """Searches through track names for a particular word."""
    trackname_col = 0

    songs = []

    # open the file
    with open(file_path) as f:
        # get rid of the header row
        _ = f.readline()

        # create a reader object
        r = csv.reader(f)

        # go through reader line by line
        for info in r:
            track_name = info[trackname_col]
            track_tokens = [
                token.lower().strip("[](),./?! ")
                for token in track_name.strip().split(" ")
            ]

            if word in track_tokens:
                songs.append(info)

    return songs


def string_to_num(s: str) -> int:
    """Converts a string number with commas in it to an integer. (e.g. "1,223,222" -> 1223222)"""
    return int(s.replace(",", "")) if s else 0
