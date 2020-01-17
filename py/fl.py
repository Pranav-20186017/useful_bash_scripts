# import urllib3
import requests
import math
import boto3
# http = urllib3.PoolManager()

# r = http.request("GET", "https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg")

# r = http.request("GET", "https://ftp.hp.com/pub/softlib/software13/printers/COL71130/LJM129-M134_UWWL_4-1_U_3_1_Full_WebPack_44.3.2667.exe")

# r = http.request("GET", "https://download.virtualbox.org/virtualbox/6.1.0/virtualbox-6.1_6.1.0-135406~Ubuntu~bionic_amd64.deb")

# r = http.request("GET", "http://s1.naasongs.download/tepn51lhc9dvla/Ilavelupu%20-%20%281956%29/[iSongs.info]%2002%20-%20Challani%20Raja.mp3")

#r = requests.get("https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64")

r = requests.get("https://images-na.ssl-images-amazon.com/images/I/71ncRs6HzyL._SX679_.jpg")


file_size = float(r.headers['Content-Length'])

print("file size in bytes: {}".format(file_size))
print("file size in kilo bytes: {} KB".format(file_size / 1024))
print("file size in mega bytes: {} MB".format(math.ceil(file_size / 1024 / 1024)))


