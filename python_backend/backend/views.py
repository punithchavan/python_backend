from django.shortcuts import render
from.models import ChaiVarity, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.
def home(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'backend/index.html', {'chais': chais})

def desc(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'backend/description.html', {'chai': chai})

def prices(request, chai_id):
    price = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'backend/prices.html', {'price': price})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST) 
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarityForm()            
    return render(request, 'backend/chai_stores.html', {'stores': stores, 'form': form})