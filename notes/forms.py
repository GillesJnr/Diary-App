from django import forms
from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'body', 'status', 'date')
        labels = {
            'title': 'Note Title',
            'body': 'Message'
        }

    def __int__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Select status"
