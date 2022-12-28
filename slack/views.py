from django.shortcuts import render
import os
from slack_sdk import WebClient
token = "xoxb-4596187176272-4572503955826-Vfdm8ccOAIvOdyMw2za9rQCQ"
client = WebClient(token=token)


# Create your views here.
def slack_msg(request):
    if request.method == "POST":
        client.chat_postMessage(channel="C04GUKZ1AKC", text=request.POST['email'], attachments=[{"text":"Who wins the lifetime supply of chocolate?","fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.","color":"#3AA3E3","attachment_type":"default","callback_id":"select_simple_1234","actions":[{"name":"winners_list","text":"Who should win?","type":"select","data_source":"users"}]}])
    return render(request, 'slack.html')
