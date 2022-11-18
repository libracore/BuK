// Copyright (c) 2016, libracore and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Uebersicht der Service Arbeiten"] = {
    "filters": [
        {
            'fieldname': "nur_aktive",
            'label': __("Zeige nur Aktive"),
            'fieldtype': "Check",
            'default': 1
        }
    ]
};
