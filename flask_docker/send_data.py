import requests

def send_data(url):
	file ={
		'file': open('flask_docker/assets/image/test_image.jpeg', 'rb')
	}
	res = requestss.post(url,files= files)
	return res.text

url = "http://102.168.xxx.xxx:5000/predict"
print(send_post(url))