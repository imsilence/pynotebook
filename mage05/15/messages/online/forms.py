#encoding: utf-8

from django import forms

class MessageForm(forms.Form):
    title = forms.CharField(label="标题", error_messages={'required' : '标题不能为空'})
    content = forms.CharField(widget=forms.Textarea, label="内容", error_messages={'required' : '内容不能为空'})

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if len(title) > 32 or len(title) == 0:
            raise forms.ValidationError('标题必须是1到32个字符')

        return title
