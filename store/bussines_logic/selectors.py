from store.models.product import Item

def get_all_products():
    return Item.objects.all()