from django import forms
from .models import Book

class Reviewform(forms.Form):
    """
        Form for reviewing a book
    """
    is_favourite = forms.BooleanField(
        label="Favourite?",
        help_text="In to your top 100 books of all time?",
        required=False
    )
    review = forms.CharField(
        widget= forms.Textarea,
        min_length=300,
        help_text="In to your top 100 books of all time?",
        required=False,
        error_messages={
            'required': 'Please enter your review!',
            'min_length': 'Please write at least 3000 characters,(you have written %(show_value)s%)  '
        }
    )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','authors']

    def clean(self):
        super(BookForm,self).clean()
        try:
            title = self.cleaned_data.get('title')
            authors = self.cleaned_data.get('authors')
            book = Book.objects.get(title=title,authors=authors)
            raise forms.ValidationError(
                'The book {} by {} already exists'.format(title,book.list_authors()),
                code='bookexists'
            )
        except Book.DoesNotExist:
            return self.cleaned_data

