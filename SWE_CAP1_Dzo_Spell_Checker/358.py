# learned from previous code and little bit knowldge from youtube
import requests

url="https://csf101-server-cap1.onrender.com/get/input/358"
txtfile="358.txt"

with open(txtfile, 'wb') as f:
    f.write(requests.get(url).content)

print("file converted")