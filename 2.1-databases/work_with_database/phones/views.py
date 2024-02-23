from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort", "")
    if sort:
        order_key = {
            "name": "name",
            "min_price": "price",
            "max_price": "-price"
        }
        phones = Phone.objects.order_by(order_key[sort])
    else:
        phones = Phone.objects.all()

    context = {
        "phones": phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        "phone": Phone.objects.filter(slug=slug)[0]
    }
    return render(request, template, context)
