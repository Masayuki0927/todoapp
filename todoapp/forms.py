from django import forms
from .models import TodoModel
from django.contrib.admin.widgets import AdminDateWidget

class TodoForm(forms.ModelForm):

    class Meta:
        model = TodoModel
        fields = ('title', 'memo','priority', 'status', 'duedate',)
        widgets = {
            'duedate': forms.SelectDateWidget,    #インポートしたウィジェットを使う指示
        }



# class ChoiceForm(forms.Form):
#     choice1 = forms.fields.ChoiceField(
#         choices = (
#             ('status', 'ステータス'),
#             ('priority', '優先度'),
#             ('duedate', '期限'),
#         ),
#         required=True,
#         widget=forms.widgets.Select
#     )