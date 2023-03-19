from django.db import models


class Poll(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=256,
        verbose_name='Описание'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    image = models.ImageField(
        blank=True,
        upload_to='img',
        verbose_name='Изображение',
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    @property
    def first_question(self):
        return Question.objects.filter(poll=self).order_by('id').first()


class Question(models.Model):
    text = models.CharField(max_length=256, verbose_name='Текст вопроса')
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        verbose_name='Тест'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text

    def get_answers_list(self):
        return [(answer.id, answer.text) for answer in (
            Answer.objects.filter(question=self))]

    @property
    def next(self):
        return Question.objects.filter(
            id__gt=self.id, poll=self.poll).order_by('id').first()


class Answer(models.Model):
    text = models.CharField(max_length=256, verbose_name='Текст')
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    correct_answer = models.BooleanField(verbose_name='Правильный',
                                         default=False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответ'

    def __str__(self):
        return self.text


class UserPollResult(models.Model):
    # avoid circle import
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        verbose_name='Опрос'
    )
    done = models.IntegerField(
        default=0,
        verbose_name='Всего ответов'
    )
    correct = models.IntegerField(
        default=0,
        verbose_name='Правильных ответов'
    )

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f'{self.user}: тест №{self.poll.id}'
