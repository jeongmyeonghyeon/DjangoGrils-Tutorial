from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    return render(request, 'bolg/post_list.html')