from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator

from .models import Conversion

from .forms import ConversionForm


def conversion_list(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)

        if form.is_valid():
            conversion = form.save(commit=False)
            conversion.convertion = bin2dec(conversion.num)
            conversion.save()
            return redirect('/')
    else:
        conversions_list = Conversion.objects.all().order_by('-created_at')
        form = ConversionForm()

        paginator = Paginator(conversions_list, 10)

        page = request.GET.get('page')

        conversions = paginator.get_page(page)

        return render(request, 'conversion/list.html', {'conversions': conversions, 'form': form})

def conversion_delete(request, id):
    conversion = get_object_or_404(Conversion, pk=id)
    conversion.delete()
    return redirect('/')


def bin2dec(num):
    total = 0

    for i in range(len(num)):
        total += int(num[-1]) * 2**i
        num = num[:-1]
    return total
