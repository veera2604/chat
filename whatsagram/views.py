from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Chat1,Chat2
from .models import Video
from .forms import VideoForm

def Home(request):
    return render(request,"home.html")
def chat(request,methods=['POST','GET']):
    if request.method=="POST":
        msg1=request.POST.get('chat1')
        msg2=request.POST.get('chat2')
        Chat1.objects.create(msg=msg1)
        data=Chat1.objects.all()
        return render(request,'chat.html',{"Msg":msg1,"Msg2":msg2})
    return render(request,'chat.html')

def vid(request):
    form=VideoForm()
    return render(request,"vid.html",{"Form":form})

def video_detail(request, video_id):
    video = Video.objects.get(pk=video_id)
    return render(request, 'reels.html', {'video': video})
    
