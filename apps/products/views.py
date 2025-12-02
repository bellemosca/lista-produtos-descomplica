from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 5)  # 5 produtos por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"page_obj": page_obj})
