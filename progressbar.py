from tqdm import tqdm
from time import sleep
# for i in tqdm([1,2,3,4,5]):
#     time.sleep(0.2)
####################################
while(True):   
    with tqdm(total=100) as pbar:
        for i in range(10):
            sleep(0.1)
            pbar.update(10)
        print(" \'\3\'"*40)
#####################################
# from alive_progress import alive_bar
# with alive_bar(100, bar='bubbles', spinner='arrows') as bar:
#     for i in range(100):
#         sleep(0.03)
#         bar()
######################################
# import alive_progress
# from alive_progress import show_bars 

# print(show_bars)


