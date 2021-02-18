from django.shortcuts import render
# Create your views here.


posts = [
    {
        'Name': "Manish Kumar Panday",
        'Address': "Siwan Bihar",
        'Email': "manishcs036@gmail.com",
        'Mobile_number': 7781823530,
        'Birthday': "14/10/1997",
    },
    {
    
        'Name': "Ashutosh Mishra",
        'Address': "Lar Road Deoria",
        'Email': "1516510042@kit.ac.in",
        'Mobile_number': 8381858530,
        'Birthday': "17/02/1996",
    }
    ]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
