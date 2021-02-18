from django.shortcuts import render
# Create your views here.


posts = [
    {
        'author': "Manish Kumar Panday",
        'date_posted': "12/12/2035",
        'title': "Broken Angles",
        'content': "Drama",
        
    },
    {
    
        'author': "Ashutosh Mishra",
        'date_posted': "31/12/2030",
        'title': "How to free fall?",
        'content': "Adventure",
        
    }
    ]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
