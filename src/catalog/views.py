from django.shortcuts import render, redirect

from django.views import generic

from catalog.forms import GoodCreateForm
from catalog.models import CategoryModel, GoodModel, ImageModel


class CategoryListView(generic.ListView):
    model = CategoryModel
    template_name = 'catalog/category_list.html'


class GoodsByCategoryView(generic.ListView):
    context_object_name = 'goods'
    template_name = 'catalog/goods_list.html'

    def get_queryset(self):
        self.category = CategoryModel.objects.get(pk=self.kwargs['pk'])
        queryset = GoodModel.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.category
        return context


class GoodCreateView(generic.CreateView):
    model = GoodModel

    def get(self, request, *args, **kwargs):
        form = GoodCreateForm()
        return render(request, 'catalog/good_form.html',
                      context={'form': form})

    def post(self, request, *args, **kwargs):
        form = GoodCreateForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.pop('images')
            new_good = GoodModel.objects.create(
                category=form.cleaned_data['category'],
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price']
            )
            ImageModel.objects.bulk_create([ImageModel(
                good=new_good, img=img, short_description=form.cleaned_data['short_description']) for img in images])
            return redirect('/catalog/categories')
        return render(request, 'catalog/good_form.html',
                      context={'form': form})
