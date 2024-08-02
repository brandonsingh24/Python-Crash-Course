# User albums

# This function creates a dictionary that represents an album.
def make_album(artist_name, album_name, track_number=None):
    """Create a dictionary containing album details."""
    # Initialize the album dictionary with artist name and album name.
    album = {'artist_name' : artist_name, 'album_name' : album_name}
    
    # If a track number is provided, add it to the album dictionary.
    if track_number:
        album['track number'] = track_number
    
    # Return the completed album dictionary.
    return album

# Start an infinite loop to continuously ask the user for album details.
while True:
    # Ask the user for the artist name or a command to quit.
    artist_name = input("\nPlease tell me the artist name or press 'q' to quit:")
    
    # If the user enters 'q', break the loop and end the program.
    if artist_name == 'q':
        break
    
    # Ask the user for the album name.
    album_name = input("\nPlease tell me the album name:")
    
    # Use the provided artist name and album name to create an album dictionary.
    album_info = make_album(artist_name, album_name)
    
    # Print the album information.
    print(f"\nThis is your album info: {album_info}")