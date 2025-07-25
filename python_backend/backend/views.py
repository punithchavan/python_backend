from django.shortcuts import render
from.models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'backend/index.html', {'chais': chais})

def desc(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'backend/description.html', {'chai': chai})