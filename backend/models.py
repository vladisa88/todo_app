from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=140, verbose_name='Название')
    completed = models.BooleanField(verbose_name='Выполнено', default=False, blank=True, null=True)
    start_date = models.DateTimeField(verbose_name='Дата начала', auto_now_add=True)

    def __str__(self):
        return self.title
