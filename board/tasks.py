from celery import shared_task
from django.contrib.auth.models import User
from .models import Post, Response
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone


@shared_task
def task_mail_week(): # выслать посты за неделю
    week_back = datetime.today() - timedelta(days=7) # определить время неделю
    postsweek = list(Post.objects.filter(dateCreation__gte=week_back)) # фильтруем все посты за неделю
    if postsweek:
        for user in User.objects.filter():
            print(user) # отображение пользователя
            posts_s = ''
            for post in postsweek:
                posts_s += f'\n{post.title}\nhttp://127.0.0.1:8000/post/{post.id}'
            send_mail(
                subject=f'Notice Board: объявления за прошедшую неделю.',
                body=f'Привет, {user.username}, просмотрите новые объявления,за последнюю неделю: \n{posts_s}',
                from_email='notice.board.Factory@gmail.com',
                recipient_list=[user.email, ], # дергаем с базы электронную почту пользователя
            )

@shared_task
def respond_accept_email(res_id): # высылаем подтверждение принятия отклика
    respond = Response.objects.get(id=res_id)
    
    # print(respond.post.author.email)
    send_mail(
        subject=f'Notice Board оповещение - отклик на ваше объявление',
        body=f'Привет, Автор {respond.post.author}, принял Ваш отклик на объявление {respond.post.title}.\n'
                f'Чтобы просмотреть принятые отклики, можно перейти по ссылке \nhttp://127.0.0.1:8000/responses',
        from_email='notice.board.Factory@gmail.com',
        recipient_list=[respond.post.author.email, ], # дергаем с базы электронную почту автора
    )


@shared_task
def respond_email(res_id):
    respond = Response.objects.get(id=res_id)
    send_mail(
        subject=f'Notice Board оповещение - отклик на ваше объявление',
        body=f'Привет, {respond.post.author}, есть новый отклик на ваше объявление.\n'
                f'Чтобы прочитать отклик, можно перейти по ссылке \nhttp://127.0.0.1:8000/responses/{respond.post.id}',
        from_email='notice.board.Factory@gmail.com',
        recipient_list=[respond.post.author.email, ], # дергаем с базы электронную почту автора
    )