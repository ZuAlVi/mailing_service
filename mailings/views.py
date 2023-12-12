from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.forms import inlineformset_factory

from mailings.models import Client, MailingSettings, Message, Log
from mailings.forms import ClientForm, MailingSettingsForm, MessageForm


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView, ClientForm):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailings:clients_list')


class ClientUpdateView(UpdateView, ClientForm):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailings:clients')


class MailingSettingsDetailView(DetailView):
    model = MailingSettings


class MailingSettingsListView(ListView):
    model = MailingSettings

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['all'] = context_data['object_list'].count()
        context_data['active'] = context_data['object_list'].filter(status=MailingSettings.STARTED).count()

        mailing_list = context_data['object_list'].prefetch_related('clients')
        clients = set()
        [[clients.add(client.email) for client in mailing.clients.all()] for mailing in mailing_list]
        context_data['clients_count'] = len(clients)
        return context_data


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingSettings, Message, extra=1, form=MessageForm)

        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST)
        else:
            context_data['formset'] = MessageFormset()

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailings:distribution_list')


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings

    def get_success_url(self):
        return reverse('mailings:distribution_list')


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingSettings, Message, extra=1, form=MessageForm)

        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MessageFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailings:distribution_detail', args=[self.object.pk])


class LogListView(ListView):
    model = Log

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['all'] = context_data['object_list'].count()
        context_data['success'] = context_data['object_list'].filter(status=True).count()
        context_data['error'] = context_data['object_list'].filter(status=False).count()

        return context_data
