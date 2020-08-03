import instaloader
L= instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context,'username')
print(profile.biography)
