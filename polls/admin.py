from django.contrib import admin
from nested_admin.nested import (
    NestedTabularInline,
    NestedStackedInline,
    NestedModelAdmin
)

from polls.models import Poll, Question, Answer, UserPollResult


class AnswerInline(NestedTabularInline):
    model = Answer
    fields = ('text', 'correct_answer')
    extra = 0
    min_num = 1
    max_num = 4


class QuestionInline(NestedStackedInline):
    model = Question
    inlines = (AnswerInline, )
    fields = ('text', )
    inline_classes = ('grp-collapse grp-open',)
    min_num = 1
    extra = 0


@admin.register(Poll)
class PollAdmin(NestedModelAdmin):
    fields = ('title', 'description', 'image')
    list_display = ('title', 'description', 'pub_date')
    inlines = (QuestionInline, )


@admin.register(UserPollResult)
class ResultAdmin(admin.ModelAdmin):
    fields = ('user', 'poll', 'done', 'correct')
    list_display = ('user', 'poll', 'done', 'correct')

