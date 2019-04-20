from .models import Category, Code


def create_code(**kwargs):
    category = Category(
        code=kwargs.pop('category_code'),
        title=kwargs.pop('category_title')
    ).save()
    return Code(category_id=category.id, **kwargs).save()
