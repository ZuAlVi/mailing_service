from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import ClientListView, ClientCreateView, ClientUpdateView, MailingSettingsListView, \
    MailingSettingsCreateView, MailingSettingsUpdateView, MailingSettingsDetailView, MailingSettingsDeleteView, \
    LogListView

app_name = MailingsConfig.name

urlpatterns = [
    path('', MailingSettingsListView.as_view(), name='distribution_list'),
    path('create', MailingSettingsCreateView.as_view(), name='create_distribution'),
    path('edit/<int:pk>', MailingSettingsUpdateView.as_view(), name='distribution_edit'),
    path('distribution/<int:pk>', MailingSettingsDetailView.as_view(), name='distribution_detail'),
    path('delete/<int:pk>', MailingSettingsDeleteView.as_view(), name='distribution_delete'),
    path('clients', ClientListView.as_view(), name='clients_list'),
    path('clients/create', ClientCreateView.as_view(), name='create_client'),
    path('clients/update/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('log', LogListView.as_view(), name='log_list'),

]
