#User albums

def make_album(artist_name, album_name, track_number=None):
    """Dictionary contain album details"""
    album = {'artist_name' : artist_name, 'album_name' : album_name}
    if track_number:
        album['track number'] = track_number
    return album

while True:
    print("\n please tell me the artist name:")
    print("\n please tell me the album name:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("artist")
    if artist_name == 'q':
        break

    album_info = make_album(artist_name, album_name)
    print(f\"nThis is your album info: {album_info}")                        
#album = {'artist' : artist_name, 'album' : album_name}
#return album
album_info = make_album('the beatles', 'abbey road', '11')
#album_info = make_album('artist', 'album')
print(f"The follow is album info: {album_info}")