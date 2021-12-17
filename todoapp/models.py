from django.db import models

CHOICE = (('high','high'),('normal','normal'),('low','low'))
status_CHOICE = (('done','done'),('WIP','WIP'),('Not started','Not started'))
 
class TodoModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="タスク名")
    memo = models.TextField(verbose_name="タスクの概要", blank=True, null=True)
    priority = models.CharField(
        max_length= 50,
        choices= CHOICE,
        verbose_name="優先度"
    )
    status = models.CharField(
        max_length= 50,
        choices= status_CHOICE,
        verbose_name="ステータス"
    )
    duedate = models.DateTimeField(verbose_name="期限")
    user_id = models.CharField(max_length=50, null=True) 

    def __str__(self):
        return self.title


