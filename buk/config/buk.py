from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": _("Service Arbeiten"),
            "icon": "fa fa-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Service Arbeiten",
                    "description": _("Service Arbeiten")
                },
                {
                    "type": "report",
                    "name": "Uebersicht der Service Arbeiten",
                    "label": _("Übersicht der Service Arbeiten"),
                    "description": _("Übersicht der Service Arbeiten"),
                    "doctype": "Service Arbeiten",
                    "is_query_report": True
                }
            ]
        }
    ]
