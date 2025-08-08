rom django.db import models
class edback(models.Model):
    comment = model.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
  from django import forms
  from .models importFeedback
  class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        Fields = ['comment'] 
 from django.shortcuts import render,redirect
 from. forms import FeedbackForm
 def feedback_view(request):
    if request.method == 'POST'
    form  =FeedbackForm(request.POST)
    if form.is_valid():
        form.save() 
        return redirect('success')
        else:
            form = FeedbackForm()
            return render(request, 'feedback.html', {'form': form})    





