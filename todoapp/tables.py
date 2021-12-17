import django_tables2 as tables
from .models import TodoModel

class TodoTable(tables.Table):
    class Meta:
        model = TodoModel
        template_name = "django_tables2/bootstrap.html"
        fields = ('title', 'memo','priority', 'duedate',)