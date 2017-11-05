from django.shortcuts import render

from django.views.generic import ListView

from .models import Goods
from django.db.models import Q

class GoodsListView(ListView):
    template_name = 'index.html'
    model = Goods
    ordering = ['-create_time']
    paginate_by = 2

    def get_queryset(self):
        q = str(self.request.GET.get('q', '')).strip()
        queryset = super().get_queryset()
        queryset = queryset.filter(status=0)
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(desc__icontains=q) | Q(category__name__icontains=q))

        return queryset