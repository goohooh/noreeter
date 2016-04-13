from django import forms

from datetimewidget.widgets import DateTimeWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from activities.models import Activity


class ActivityRegistForm(forms.ModelForm):

    dateTimeOptions = {
        'format': 'yyyy-mm-dd hh:ii',
        'autoclose': True,
        'showMeridian': False,
    }

    due_datetime = forms.DateTimeField(
        widget=DateTimeWidget(options=dateTimeOptions),
    )

    class Meta:
        model = Activity
        exclude = [
            'host',
            'town',
            'participant_set',
            'is_full',
        ]

    def __init__(self, *args, **kwargs):
        super(ActivityRegistForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['title'].label = '제목'
        self.fields['content'].label = '본문'
        self.fields['category_set'].label = '카테고리'
        self.fields['image'].label = '이미지'
        self.fields['due_datetime'].label = '모임 시간'
        self.fields['max_num_of_participant'].label = '최대 모집인원'
        self.helper.layout = Layout(
            'title',
            'content',
            'category_set',
            'image',
            'due_datetime',
            'max_num_of_participant',
        )
