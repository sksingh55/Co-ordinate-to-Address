from django.shortcuts import render
from pygeocoder import Geocoder
from geopy.geocoders import GoogleV3


def index(request):
	return render(request, 'location/index.html')


def detail(request):
	if request.GET.get('done'):
		x=(request.GET.get('latitude'))
		y=(request.GET.get('longitude'))
		print(x)
		print(y)
		z='"'+x+','+y+'"'
		print(z)
		geolocator = GoogleV3("AIzaSyB5U6iCtTTkLHH576hV7Zbx-2hTAOq3tts")
		location = geolocator.reverse(z)
		if location :
			return render(request, 'location/detail.html', {'address': location[1]})
		else:
			return render(request, 'location/detail.html', {'address': "NOT VALID LOCATION"})
	else:
		print("fgbskb")
