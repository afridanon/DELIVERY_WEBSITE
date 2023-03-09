from django.shortcuts import render
import os
from django.http import HttpResponse
from twilio.rest import Client
def index(request):
	return render(request,'index.html')


def test(request):
	
	val1 = int(request.POST["NUMBER_FIELD"])
	print(val1)
	return render(request,"index.html")


def message():
	global message
	#link = "https://scmylsc.github.io/scmylsc"
	link = "https://rzp.io/l/mAsJjQ2ST"
	amount_id = "5000"
	order_id = "4000"
	message = "WELCOME TO SWEETCHOICE YOUR ORDER ID  : "+order_id+", AND YOUR AMOUNT : "+amount_id+", WANT TO MAKE PAYMENT IN ONLINE : "+ link

def twilio(request):
	main_number = int(request.POST["NUMBER_FIELD"])

	main_message = message
	account_sid = "ACdd79ce84a0c87af94f772a39e9d03f07"
	auth_token = "a9bbf89474da3742d24638de551b9fc9"
	client = Client(auth_token,account_sid)
	client.message.create(to = main_number,
		       from_ = "",
			   body = main_message)
	return render(request,"index.html")