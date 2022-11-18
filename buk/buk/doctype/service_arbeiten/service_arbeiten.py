# -*- coding: utf-8 -*-
# Copyright (c) 2022, libracore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.data import add_to_date, today, formatdate

class ServiceArbeiten(Document):
    def validate(self):
        # setze initiales ausführungsdatum anhand intervall startdatum
        if not self.geplant_per:
            self.geplant_per = add_to_date(self.start_date, days=self.days, months=self.months, years=self.years)
        
        # setze ggf. nächstes ausführungsdatum anhand intervall und kundentermin
        if self.termin_vereinbart and self.status == 'Aktiv':
            self.set_new_date()
    
    def set_new_date(self):
        # berechne und setze nächstes ausführungsdatum anhand intervall und kundentermin
        if self.vereinbarter_termin < today():
            try:
                self.durchgefuehrte_termine += "{0}\n".format(frappe.utils.get_datetime(self.vereinbarter_termin).strftime('%d.%m.%Y'))
            except:
                self.durchgefuehrte_termine = "{0}\n".format(frappe.utils.get_datetime(self.vereinbarter_termin).strftime('%d.%m.%Y'))
            self.letztmals_durchgefuehrt = self.vereinbarter_termin
            self.geplant_per = add_to_date(self.vereinbarter_termin, days=self.days, months=self.months, years=self.years)
            self.vereinbarter_termin = None
            self.termin_vereinbart = None
    
    def intervall_neuberechnung(self):
        if self.letztmals_durchgefuehrt:
            self.geplant_per = add_to_date(self.letztmals_durchgefuehrt, days=self.days, months=self.months, years=self.years)
        else:
            self.geplant_per = add_to_date(self.start_date, days=self.days, months=self.months, years=self.years)
        self.save()
        return

def check_set_new_date():
    service_arbeiten = frappe.db.sql("""SELECT `name` FROM `tabService Arbeiten` WHERE `vereinbarter_termin` < CURDATE()""", as_dict=True)
    for serv_a in service_arbeiten:
        doc = frappe.get_doc("Service Arbeiten", serv_a.name)
        doc.save() # triggers self.set_new_date()
