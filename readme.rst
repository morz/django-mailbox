It is fork for https://github.com/coddingtonbear/django-mailbox

.. image:: https://travis-ci.org/morz/django-mailbox.svg?branch=master
   :target: https://travis-ci.org/morz/django-mailbox

Differences from the original
=============

* Add function ``record_draft_message`` for creating draft of messages `04eafae <https://github.com/morz/django-mailbox/commit/04eafae747a3e40d4756a6f1322ce6b320efda2e>`_.
* Add searching parameter for imap connection. `b814d66 <https://github.com/morz/django-mailbox/commit/b814d66c6dc865b46cca500ba8f079a17c42bf17#diff-61b7ed68b4a7074b1ee53c624772fa90>`_.
* Add function ``save_message`` in imap connection protocol. This function append message on imap server and return UID. `53e6000 <https://github.com/morz/django-mailbox/commit/53e6000f7d6572b2ff06d30b6e9f4b918b3d0190>`_.
* Download only un-downloaded messages from the mailbox

TODO:
=============
*
