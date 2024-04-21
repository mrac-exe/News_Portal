# 1)   Создать двух пользователей (с помощью метода User.objects.create_user('username')).
#
# from news.models import *
#
# u1 = User.objects.create_user('Василий')
# u2 = User.objects.create_user('Иван')
#
#
#
# 2)   Создать два объекта модели Author, связанные с пользователями.
#
# a1 = Author.objects.create(user=u1)
# a2 = Author.objects.create(user=u2)
#
#
# 3. Добавить 4 категории в модель Category.
# cat1 = Category.objects.create(name='Спорт')
# cat2 = Category.objects.create(name='Экология')
# cat3 = Category.objects.create(name='Gemes')
# cat4 = Category.objects.create(name='Политика')
#
#4. Добавить 2 статьи и 1 новость.
# p1 = Post.objects.create(title='The Day Before уже успела стать одной из самых низкорейтинговых игр в Steam', text='The Day Before пронизана множеством багов, а также проблемами с оптимизацией, серверами и всем остальным.', author=a2)
#
# p2 = Post.objects.create(title='Интересные факты о Байкале: нефть, ветра с именами и обитаемый остров', text='Самое глубокое озеро планеты. Первый и самый известный «титул» Байкала.', author=a1)
#
# p3 = Post.objects.create(title='Team Spirit сыграет с Virtus.pro в финале BetBoom Dacha', text='Team Spirit прошла в финал соревнования. Начало решающего противостояния 10 декабря, 13:55 мск.', author=a2)

# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# PostCategory.objects.create(post=p1, category=cat3)

# PostCategory.objects.create(post=p2, category=cat2)
#
# PostCategory.objects.create(post=p3, category=cat3)
#
# PostCategory.objects.create(post=p3, category=cat1)
#
# 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
# c1 = Comment.objects.create(text='Ой, да как вы вообще в эту гадость играете?', post=p1, user=User(id=2))
#
# c2 = Comment.objects.create(text='А вы бы хотели увидеть Байкал?', post=p2, user=User(id=2))
#
# c3 = Comment.objects.create(text='А свой собственный текст прочесть перед публикацией не судьба?', post=p3, user=User(id=2))
#
# c4 = Comment.objects.create(text='Извините, не заметил, что название пропущено. Поправим. Спасибо за замечание!', post=p3, user=User(id=2))
#
#
#
# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
# p1.like() - 2 раза
#
# p2.like() - 3 раза
#
# p3.like() - 1 раз
#
# p3.dislike() - 2 раза
#
# c1.dislike() - 2 раза
#
# c2.like() - 4 раза
#
# c3.like() - 3 раза
#
# c3.dislike() - 1 раз
#
# c4.like() - 3 раза
#
#
# 8. Обновить рейтинги пользователей.
# a1.update_rating()
# a2.update_rating()
#
#
# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# Author.objects.all().order_by('-rating').values('user__username', 'rating').first()
#
# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
# Post_best = Post.objects.all().order_by('-rating').first()
# Post_best.date_time
# Post_best.author.user.username
# Post_best.rating
# Post_best.title
# Post_best.preview()
#
# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье
# Comment.objects.filter(post=Post_best).values('date_time', 'user__username', 'rating', 'text')