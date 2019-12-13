from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import FeedbackForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import QRC


class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = 'qrservice/qr.html'
    success_url = reverse_lazy('qrservice:ok')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class QRListView(ListView):
    model = QRCode
