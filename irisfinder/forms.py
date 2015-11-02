from django import forms


class UserIrisData(forms.Form):
    sepal_length = forms.FloatField(label="Sepal length")
    sepal_width = forms.FloatField(label="Sepal width")
    petal_length = forms.FloatField(label="Petal length")
    petal_width = forms.FloatField(label="Petal width")
