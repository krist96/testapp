from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import Contactt
from .forms import ContactForm

class ContactView(ListView):
    model = Contactt
    template_name = 'contact/contact_list.html'

class ContactDeleteView(DeleteView):
    model = Contactt
    success_url = reverse_lazy('contact_list')
    template_name = 'contact/contact_confirm_delete.html'
class ContactUpdateView(UpdateView):
    model = Contactt
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact_list')

class ContactCreateView(CreateView):
    model = Contactt
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact_list')