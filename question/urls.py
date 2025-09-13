from django.urls import path

from question.views import add_question_page, user_add_question

urlpatterns = [
    path('add', add_question_page, name="add-question-page"),
    path('user-add-question', user_add_question, name='user-add-question'),

]