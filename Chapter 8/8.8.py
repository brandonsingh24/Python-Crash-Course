#User albums

def make_album(artist_name, album_name, track_number=None):
    """Dictionary contain album details"""
    album = {'artist_name' : artist_name, 'album_name' : album_name}
    if track_number:
        album['track number'] = track_number
    return album

while True:
    artist_name = input("\n please tell me the artist name or press q to quit:")
    
    if artist_name == 'q':
        break
    
    album_name = input("\nPlease tell me the album name:")
    album_info = make_album(artist_name, album_name)
    print(f"\nThis is your album info: {album_info}")                        
