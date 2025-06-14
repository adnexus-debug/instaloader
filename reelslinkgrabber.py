import instaloader

L = instaloader.Instaloader()
L.load_session_from_file('adnexuss', 'session-adnexuss')

profile = instaloader.Profile.from_username(L.context, 'xhamasters_')

print(f"Profile loaded: {profile.username}, {profile.mediacount} posts")
