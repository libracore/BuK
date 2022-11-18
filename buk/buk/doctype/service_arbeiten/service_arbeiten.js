// Copyright (c) 2022, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Service Arbeiten', {
    intervall_neuberechnung: function(frm) {
        frappe.call({
            method: 'intervall_neuberechnung',
            doc: frm.doc,
            callback: function(response) {
               cur_frm.reload_doc();
            }
        });
    },
    refresh: function(frm) {
        cur_frm.fields_dict['contact'].get_query = function(doc) {
             return {
                 filters: {
                     "link_name": frm.doc.customer
                 }
             }
        }
        cur_frm.fields_dict['address'].get_query = function(doc) {
             return {
                 filters: {
                     "link_name": frm.doc.customer
                 }
             }
        }
    },
    customer: function(frm) {
        cur_frm.set_value("address", "");
        cur_frm.set_value("contact", "");
    }
});
