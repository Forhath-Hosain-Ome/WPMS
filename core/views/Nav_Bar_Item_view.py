from core.models import NavItemModel, NavGroupModel

def navbar_items(request):
    standalone_items = NavItemModel.objects.filter(is_active=True, group__isnull=True).order_by('order')
    grouped_items = NavGroupModel.objects.prefetch_related(
        'items'
    ).order_by('order')
    
    return {
        'standalone_items': standalone_items,
        'nav_groups': grouped_items,
    }