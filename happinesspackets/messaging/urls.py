from __future__ import unicode_literals

from django.conf.urls import url

from .views import (StartView, MessageSearchView, MessageSendView, MessageSenderConfirmationSentView, MessageSenderConfirmationView,
                    MessageSenderConfirmedView, MessageRecipientMessageUpdate, FaqView, ArchiveView, InspirationView,
                    BlacklistEmailView, ReceivedMessagesView, SentMessagesView)

urlpatterns = [
    url(r'^$', StartView.as_view(), name='start'),
    url(r'^faq/$', FaqView.as_view(), name='faq'),
    url(r'^archive/$', ArchiveView.as_view(), name='archive'),
    url(r'^inspiration/$', InspirationView.as_view(), name='inspiration'),
    url(r'^received-messages/$', ReceivedMessagesView.as_view(), name='received_messages'),
    url(r'^sent-messages/$', SentMessagesView.as_view(), name='sent_messages'),
    url(r'^blacklist-email/(?P<email>[\w\.@\+-]+)/(?P<digest>\w+)/$', BlacklistEmailView.as_view(), name='blacklist_email'),
    url(r'^send/$', MessageSendView.as_view(), name='send'),
    url(r'^send/confirmation-sent/$', MessageSenderConfirmationSentView.as_view(), name='sender_confirmation_sent'),
    url(r'^send/confirmation/(?P<identifier>[\w-]+)/(?P<token>[\w-]+)/$', MessageSenderConfirmationView.as_view(), name='sender_confirm'),
    url(r'^send/confirmed/$', MessageSenderConfirmedView.as_view(), name='sender_confirmed'),
    url(r'^recipient/(?P<identifier>[\w-]+)/(?P<token>[\w-]+)/$', MessageRecipientMessageUpdate.as_view(), name='recipient_message_update'),
    url(r'^search/?$', MessageSearchView.as_view(), name='search'),
]
