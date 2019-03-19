from django.shortcuts import render

# Create your views here.

def candidate(request):
    return render(request,'candidates/candidate.html')