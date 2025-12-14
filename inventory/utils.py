from .models import Item

def get_all_categories():
    return (
        Item.objects
        .exclude(category__isnull=True)
        .exclude(category__exact='')
        .values_list('category', flat=True)
        .distinct()
        .order_by('category')
    )
