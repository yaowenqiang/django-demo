from django import forms

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
