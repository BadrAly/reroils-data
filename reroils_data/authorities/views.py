# -*- coding: utf-8 -*-
#
# This file is part of organisations.
# Copyright (C) 2018 RERO.
#

"""Blueprint used for loading templates.

The sole purpose of this blueprint is to ensure that Invenio can find the
templates and static files located in the folders of the same names next to
this file.
"""

from __future__ import absolute_import, print_function

from urllib.request import urlopen

import six
from dojson.contrib.marc21.utils import create_record, split_stream
from flask import Blueprint, abort, current_app, jsonify
from flask_babelex import gettext as _
from reroils_record_editor.permissions import record_edit_permission

from .dojson.contrib.unimarctojson import unimarctojson

blueprint = Blueprint(
    'reroils_data_authorities',
    __name__,
    template_folder='templates',
    static_folder='static',
)
