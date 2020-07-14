from pytube import YouTube
YouTube("Link").streams.first().download()
