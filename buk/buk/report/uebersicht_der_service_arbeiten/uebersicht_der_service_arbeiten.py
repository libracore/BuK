# Copyright (c) 2013, libracore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return[
        {"label": _("Titel"), "fieldname": "titel", "fieldtype": "Data"},
        {"label": _("Dokument"), "fieldname": "name", "fieldtype": "Link", "options": "Service Arbeiten", "width": 105},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data"},
        {"label": _("Typ"), "fieldname": "typ", "fieldtype": "Data"},
        {"label": _("Projekt"), "fieldname": "project", "fieldtype": "Link", "options": "Project"},
        {"label": _("Kunde"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer"},
        {"label": _("Kundenname"), "fieldname": "customer_name", "fieldtype": "Data", "width": 190},
        {"label": _("Geplant"), "fieldname": "geplant_per", "fieldtype": "Date"},
        {"label": _("Strasse"), "fieldname": "strasse", "fieldtype": "Data"},
        {"label": _("PLZ"), "fieldname": "plz", "fieldtype": "Data"},
        {"label": _("Ort"), "fieldname": "ort", "fieldtype": "Data"},
        {"label": _("Festnetz"), "fieldname": "festnetz", "fieldtype": "Data"},
        {"label": _("Mobile"), "fieldname": "mobile", "fieldtype": "Data"},
        {"label": _("Vereinbart"), "fieldname": "termin_vereinbart", "fieldtype": "Check"},
        {"label": _("Vereinbart"), "fieldname": "vereinbarter_termin", "fieldtype": "Date"},
        {"label": _("Durchgeführt"), "fieldname": "letztmals_durchgefuehrt", "fieldtype": "Date"}
    ]

def get_data(filters):
    aktive_filter = ''
    if filters.nur_aktive:
        aktive_filter = """WHERE `status` = 'Aktiv'"""
    return frappe.db.sql("""SELECT
                                `titel`,
                                `name`,
                                `status`,
                                `customer`,
                                `geplant_per`,
                                `termin_vereinbart`,
                                `letztmals_durchgefuehrt`,
                                `customer_name`,
                                `vereinbarter_termin`,
                                `typ`,
                                `project`,
                                `strasse`,
                                `plz`,
                                `ort`,
                                `festnetz`,
                                `mobile`
                            FROM `tabService Arbeiten`
                            {aktive_filter}""".format(aktive_filter=aktive_filter), as_dict=True)
