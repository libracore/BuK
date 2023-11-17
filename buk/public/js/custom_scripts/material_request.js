frappe.ui.form.on("Material Request", {
    refresh: function(frm) {
		if (!frm.doc.__islocal) {
			frm.add_custom_button("Excel exportieren",  function(frm){
				create_excel_file(frm);
			});
		}
    }
});

function create_excel_file(frm) {
    frappe.call({
        "method": "buk.utils.material_request.create_mr_excel_export",
        "args": {
            "material_request": cur_frm.doc.name
        },
        "callback": function (response) {
				frappe.msgprint('Daten exportiert, File im Anhang');
				cur_frm.reload_doc();
        }
    });
}
