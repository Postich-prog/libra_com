from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Текст комментария',
        }
        help_texts = {
            'text': 'Добавьте Ваш комментарий',
        }

    def __str__(self):
        return self.text
