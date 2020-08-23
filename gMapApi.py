import requests
import json

api_key = YOUR API KEY

if api_key:
	serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json'
	
while True:
	address = input('enter your location')
	if len(address)<1: break
	
	payload=dict()
	payload['address']=address
	if api_key : payload['key']=api_key
	
	r=requests.get(serviceurl,params=payload)
	print('Retrieved',r.url)
	data = r.text
	print('Retrieved',len(data), 'characters')
	
	try:
		js= json.loads(data)
	except:
		js = None
		
	if not js or 'status' not in js or js['status'] != 'OK':
		print('--- Failure to retrieve ----')
		print(data)
		continue
		
	print(json.dumps(js, indent =4))
	
	lat = js['results'][0]['geometry']['location']['lat']
	lng = js['results'][0]['geometry']['location']['lng']
	print('lat', lat, 'lng', lng)
	location = js['results'][0]['formatted_address']
	print(location)
	
	
	
