# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 RERO.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""rero21 ils data module."""

from __future__ import absolute_import, print_function

from flask_babelex import gettext as _
from invenio_indexer.signals import before_record_index

from . import config
from .receivers import patron_receiver


class REROILSPATRON(object):
    """REROILS-PATRON extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        # TODO: This is an example of translation string with comment. Please
        # remove it.
        # NOTE: This is a note to a translator.
        _('A translation string')
        if app:
            self.init_app(app)
            self.register_signals(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['reroils-patron'] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith('REROILS_PATRON_'):
                app.config.setdefault(k, getattr(config, k))

    @staticmethod
    def register_signals(app):
        """Register Invenio indexer signals."""
        before_record_index.connect(patron_receiver, weak=False)
