# # import time
# # import concurrent.futures
# #
# #
# # def do_something(seconds):
# #     print(f"Sleeping {seconds} seconds(s)...")
# #     time.sleep(seconds)
# #     return "Done Sleeping..."
# #
# # start = time.perf_counter()
# #
# # with concurrent.futures.ThreadPoolExecutor() as executor:
# #     # f1 = executor.submit(do_something, 1)
# #     # f2 = executor.submit(do_something, 1)
# #    secs = [5,4,3,2,1]
# #    results = executor.map(do_something, secs)
# #
# #    for result in results:
# #        print(result)
# #
# # stop = time.perf_counter()
# # print(stop-start)
# #     # print(f1.result())
# #     # print(f2.result())
#
#
import time
import concurrent.futures
import requests
import random

img_urls = [
"https://media.istockphoto.com/id/1343663503/photo/parking-garage-floor-with-lighting.jpg?s=1024x1024&w=is&k=20&c=4s3EDDtDygaRO7iMWk2DcTTUhGgJush6QgK6XgU-7Nc=",
    "https://i.pinimg.com/564x/29/d5/d7/29d5d7e37787fdaee33db5ef1cecea08.jpg",
    "https://i.pinimg.com/564x/7c/05/f1/7c05f1cbc93581978b40e09af94dd31d.jpg",
    "https://i.pinimg.com/564x/97/bf/96/97bf96cdeec452a096706299aa4ef4d9.jpg0",
    "https://i.pinimg.com/564x/59/87/da/5987da21a34542de3c70175ef307bfb1.jpg",
    "https://i.pinimg.com/564x/b9/2d/ed/b92ded3ca9725f07d81e39668c569069.jpg"



]
t1 = time.perf_counter()

def download_img(img_url):
    data = requests.get(img_url).content
    with open(f'{random.randint(1,100)}.jpg', 'wb') as img_file:
        img_file.write(data)
        print(f"{random.randint(1, 100)} was downloaded...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_img, img_urls)

t2 = time.perf_counter()

print(f"Finished in {t2-t1} second(s)...")


