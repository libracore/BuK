frappe.ui.form.on("Material Request", {
    refresh: function(frm) {
		frm.add_custom_button(__("Create Excel File"),  function(frm){
			create_excel_file(frm);
        });
    }
});

function create_excel_file(frm) {
    frappe.call({
        "method": "buk.utils.material_request.create_mr_excel_export",
        "args": {
            "material_request": cur_frm.doc.name
        },
        "callback": function (response) {
			console.log(response)
			//~ if (!response.exc) {
				//~ // Verwenden Sie frappe.download mit dem Dateipfad
				//~ frappe.download(response.message);
			//~ } else {
				//~ frappe.msgprint('Fehler beim Exportieren der Daten: ' + response.exc);
			//~ }
        }
    });
}
