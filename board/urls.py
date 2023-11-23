from django.urls import path
from django.shortcuts import redirect

from .views import Index, CreatePost, PostView, EditPost, DeletePost, Responses, Respond, response_accept, \
  response_delete


urlpatterns = [
  path('index', Index.as_view(), name='index'),                   # главная страница
  path('post/<int:pk>', PostView.as_view()),                      # просмотр поста
  path('create_post', CreatePost.as_view(), name='create_post'),  # создание поста
  path('post/<int:pk>/edit', EditPost.as_view()),                 # правка поста
  path('post/<int:pk>/delete', DeletePost.as_view()),             # удаление поста

  path('responses', Responses.as_view(), name='responses'),       # просмотр ответов
  path('responses/<int:pk>', Responses.as_view(), name='responses'),  # просмотр одного ответа
  path('respond/<int:pk>', Respond.as_view(), name='respond'),        # создание ответа
  path('response/accept/<int:pk>', response_accept),                  # принятие ответа
  path('response/delete/<int:pk>', response_delete),                  # удаление ответа
  path('', lambda request: redirect('index', permanent=False)),       # если что-то не сработало, пересылаем на главную страницу
]
