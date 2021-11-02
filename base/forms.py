from django.forms import ModelForm

from base.models import Participant


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email']
