from core.models import Category


def add_variable_to_context(request):
    return {
        "cats": Category.objects.all()
    }
