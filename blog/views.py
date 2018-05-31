from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Post, Category, Page
from .forms import DateForm
from django.utils import timezone
from django.http import HttpResponseRedirect


class BaseMixin(generic.base.TemplateResponseMixin):

    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class IndexView(BaseMixin, generic.ListView):

    template_name = 'blog/list.html'
    context_object_name = 'latest_posts'
    paginate_by = 11
    
    def get_queryset(self):
        return Post.objects.order_by('-date')[:40]


class DetailView(BaseMixin, generic.DetailView):

    model = Post
    template_name = 'blog/detail.html'


class PostsByCategoryView(BaseMixin, generic.ListView):

    template_name = 'blog/category.html'
    context_object_name = 'category_posts'
    paginate_by = 4
    
    def get_queryset(self):
        self.categories = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Post.objects.filter(categories=self.categories)


class BestView(BaseMixin, generic.ListView):

    template_name = 'blog/best.html'
    context_object_name = 'best_posts'
    paginate_by = 11
    
    def get_queryset(self):
        return Post.objects.filter(best=True).order_by('-date')[:40]


class PageView(BaseMixin, generic.DetailView):

    template_name = 'blog/page.html'
    slug = None

    def get_object(self):
        return get_object_or_404(Page, slug=self.slug)


class DateView(BaseMixin, generic.ListView):

    template_name = 'blog/calendar.html'   
    context_object_name = 'post_by_date'
    date = timezone.now() 
    form = DateForm(initial={'asked_date':timezone.now}) 
    paginate_by = 11

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(DateView, self).get_context_data(**kwargs)
        if 'form' not in context:           
            context['form'] = self.form
        if self.form.is_valid():
            self.date = self.form.cleaned_data['asked_date']
        context['date'] = self.date
        return context

    def get_queryset(self):
        form = DateForm(self.request.POST)
        if form.is_valid():
            self.date = form.cleaned_data['asked_date']
            return Post.objects.filter(end__lte=self.date)
        else:
            return Post.objects.filter(end__lte=timezone.now())
   


