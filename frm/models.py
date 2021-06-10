from django.db import models
from django.contrib import admin
from django.db.models.fields import DateTimeField
from django.utils.translation import ugettext_lazy as _

class Hereglegch(models.Model):
    name=models.CharField(max_length=30, verbose_name=_("Хэрэглэгчийн нэр"))
    code=models.CharField(max_length=30, verbose_name=_("Хэрэглэгчийн код"))

    class Meta:
        verbose_name = _("Хэрэглэгч")
        verbose_name_plural = _("Хэрэглэгч")

    def __str__(self):
        return self.name











# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.question_text


# # class Question(models.Model):
# #     question_text = models.CharField(max_length=200)
# #     pub_date = models.DateTimeField('date published')

# #     def __str__(self):
# #         return self.question_text
#     # ...
#     # @admin.display(
#     #     boolean=True,
#     #     ordering='pub_date',
#     #     description='Published recently?',
#     # )
#     # def was_published_recently(self):
#     #     # now = timezone.now()
#     #     return now - DateTimeField.timedelta(days=1) <= self.pub_date <= now


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text