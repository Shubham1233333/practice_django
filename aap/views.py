from django.shortcuts import render


from django.contrib.auth.models import Contact

def contact(request):
    if request.method=='post':
        name=request.post.get('name')
        email=request.post.get('email')
        phone=request.post.get('phone')
        contact=Contact(name=name,email=email,phone=phone)
        contact.save()
        return render(request,'a.html')
    return render(request,'index.html')