It is fork for https://github.com/coddingtonbear/django-mailbox

.. image:: https://travis-ci.org/morz/django-mailbox.svg?branch=master
   :target: https://travis-ci.org/morz/django-mailbox

What's new?
=============

* Add function ``record_draft_message`` for creating draft of messages `04eafae <https://github.com/morz/django-mailbox/commit/04eafae747a3e40d4756a6f1322ce6b320efda2e>`_.
* added searching parameter for imap connection. `b814d66 <https://github.com/morz/django-mailbox/commit/b814d66c6dc865b46cca500ba8f079a17c42bf17#diff-61b7ed68b4a7074b1ee53c624772fa90>`_.

TODO:
=============
# sync only not getted mails from acoount

Easily ingest messages from POP3, IMAP, or local mailboxes into your Django application.

This app allows you to either ingest e-mail content from common e-mail services (as long as the service provides POP3 or IMAP support),
or directly receive e-mail messages from ``stdin`` (for locally processing messages from Postfix or Exim4).

These ingested messages will be stored in the database in Django models and you can process their content at will,
or -- if you're in a hurry -- by using a signal receiver.

- Documentation for django-mailbox is available on
  `ReadTheDocs <http://django-mailbox.readthedocs.org/>`_.
- Please post issues on
  `Github <http://github.com/coddingtonbear/django-mailbox/issues>`_.
- Test status available on
  `Travis-CI <https://travis-ci.org/coddingtonbear/django-mailbox>`_.


.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/coddingtonbear/django-mailbox
   :target: https://gitter.im/coddingtonbear/django-mailbox?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
