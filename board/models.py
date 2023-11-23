from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# from django.contrib.contenttypes.fields import GenericRelation
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
# from django.conf import settings


# Verbose_name - удобночитаемое имя поля
class Post(models.Model): # пост
    author = models.ForeignKey(User, on_delete=models.CASCADE) # автор
    # віды категорий по тех заданию
    CATEGORY_SP = (('tanks', 'Танки'),
           ('hils', 'Хилы'),
           ('dd', 'ДД'),
           ('torgov', 'Торговцы'),
           ('gildmasters', 'Гилдмастеры'),
           ('questgivers', 'Квестгиверы'),
           ('kuznec', 'Кузнецы'),
           ('kogevnik', 'Кожевники'),
           ('zelevari', 'Зельевары'),
           ('masterszak', 'Мастера заклинаний'))
    category = models.CharField(max_length=15, choices=CATEGORY_SP, verbose_name='Категория')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    dateCreation = models.DateTimeField(auto_now_add=True) # дата создания
    text = RichTextField() # поле хранения текста поста с ссылками

class Response(models.Model): # ответ
    author = models.ForeignKey(User, on_delete=models.CASCADE) # автор ответа
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # на какой пост
    text = models.TextField(verbose_name='Текст')
    accept = models.BooleanField(default=False) # принятие ответа автором поста
    dateCreation = models.DateTimeField(auto_now_add=True) # дата создания

# # ЛАЙКИ ! Like через GenericRelation
# class Like(models.Model): # лайки, лайкать ответы, в django лайк ставиться на объект
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')  # автор лайка,
#     # related_name='likes' явно зададим имя лайка при связи
#     response = models.ForeignKey(Response, on_delete=models.CASCADE)  # на какой ответ
##    Модель Like основана на встроенном в Django фреймворке ContentType
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
## Фреймворк ContentType предоставляет отношение GenericForeignKey,
## которое создает обобщенные (generic) отношениямежду моделями.
## ForeignKey создает отношение только с какой-то конкретной моделью.
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')

## Создаем модель Tweet и связываем ее с моделью Like через GenericRelation
# class Tweet(models.Model):
#     body = models.CharField(max_length=140)
#     likes = GenericRelation(Like)
#     def __str__(self):
#         return self.body
#     @property
#     def total_likes(self):
#         return self.likes.count()