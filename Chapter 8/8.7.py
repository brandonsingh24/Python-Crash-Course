##Album

def make_album(artist_name, album_name, track_number=None):
    """Dictionary contain album details"""
    album = {'artist_name' : artist_name, 'album_name' : album_name}
    if track_number:
        album['track number'] = track_number
    return album

#album = {'artist' : artist_name, 'album' : album_name}
#return album
album_info = make_album('the beatles', 'abbey road', '11')
#album_info = make_album('artist', 'album')
print(f"The follow is album info: {album_info}")