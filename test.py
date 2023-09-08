from pytube import Playlist

url = input("Enter The Url List===> ")
p = Playlist(url)
print(f'Downloading: {p.title}')

for video in p.videos:
    video.streams.get_highest_resolution().download(output_path=f"D:\CcnaCourses\{p.title}")

print(f'Download Donne!')





