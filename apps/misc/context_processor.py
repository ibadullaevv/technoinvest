from .models import Category


def category_renderer(request):
    return {
        'category_list': Category.objects.all(),
    }
