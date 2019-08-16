#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The arg spec for the iosxr_lacp_interfaces module
"""


from __future__ import absolute_import, division, print_function

__metaclass__ = type


class Lacp_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the iosxr_lacp_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "churn_logging": {
                    "choices": ["actor", "partner", "both"],
                    "type": "str",
                },
                "collector_max_delay": {"type": "int"},
                "name": {"type": "str"},
                "period": {"type": "int"},
                "switchover_suppress_flaps": {"type": "int"},
                "system": {
                    "options": {
                        "mac": {"type": "str"},
                        "priority": {"type": "int"},
                    },
                    "type": "dict",
                },
            },
            "type": "list",
        },
        "state": {
            "choices": ["merged", "replaced", "overridden", "deleted"],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
