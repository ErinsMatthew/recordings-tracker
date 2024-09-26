import django_tables2 as tables
from api.models import Show


class ShowTable(tables.Table):
    class Meta:
        model = Show
        template_name = "django_tables2/bootstrap5.html"
        exclude = ("id", "sequence",)
        # fields = ("name", )
