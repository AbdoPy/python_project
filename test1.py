from pytube import YouTube
# from tqdm import tqdm
# import time

link = input(" Enter The Vedio Link: ")

video = YouTube(link)
print(f'Downloading: {video.title}')

video.streams.get_highest_resolution().download(output_path=f"D:\My Courses Vedios\Divers Videos\{video.title}")
# for i in tqdm(range(video.length)):
#     time.sleep(0.01)
print('Download Donne!')