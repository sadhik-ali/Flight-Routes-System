from django import forms

from .models import Airport, Route


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ["code"]


class RouteForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        queryset=Airport.objects.all(), empty_label="Select Parent Airport"
    )
    child = forms.ModelChoiceField(
        queryset=Airport.objects.all(), empty_label="Select Child Airport"
    )

    class Meta:
        model = Route
        fields = ["parent", "child", "position", "duration"]


class SearchNodeForm(forms.Form):
    start_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(), empty_label="Select Airport"
    )
    direction = forms.ChoiceField(choices=[("left", "Left"), ("right", "Right")])
    n = forms.IntegerField()


class ShortestPathForm(forms.Form):
    source = forms.ModelChoiceField(
        queryset=Airport.objects.all(), empty_label="Select Source Airport"
    )
    destination = forms.ModelChoiceField(
        queryset=Airport.objects.all(), empty_label="Select Destination Airport"
    )
