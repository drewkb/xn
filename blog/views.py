from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Post, Category


class BaseMixin(generic.base.TemplateResponseMixin):

    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class IndexView(BaseMixin, generic.ListView):

    template_name = 'blog/list.html'
    context_object_name = 'latest_posts'
    paginate_by = 3
    
    def get_queryset(self):
        return Post.objects.order_by('-date')[:10]


class DetailView(BaseMixin, generic.DetailView):

    model = Post
    template_name = 'blog/detail.html'


class PostsByCategoryView(BaseMixin, generic.ListView):

    template_name = 'blog/category.html'
    context_object_name = 'category_posts'
    paginate_by = 1
    
    def get_queryset(self):
        self.categories = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Post.objects.filter(categories=self.categories)

    


