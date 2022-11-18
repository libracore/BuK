// Copyright (c) 2022, libracore and contributors
// For license information, please see license.txt

frappe.listview_settings['Service Arbeiten'] = {
    add_fields: ["status"],
    get_indicator: function(doc) {
        if (doc.status == "Aktiv") {
            return [__("Aktiv"), "green", "status,=," + "Aktiv"]
        }
        
        if (doc.status == "Inaktiv") {
            return [__("Inaktiv"), "red", "status,=," + "Inaktiv"]
        }
    }
};
