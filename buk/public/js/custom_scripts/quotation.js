frappe.ui.form.on("Quotation", {
    refresh: function(frm) {
        if (!(__("Material Request") in cur_frm.custom_buttons)) {
            setTimeout(create_custom_btn(frm), 1000);
        }
    }
});

function create_custom_btn(frm) {
    frm.add_custom_button(__("Material Request"),  function() {make_material_request(frm);}, __("Create"));
}

function make_material_request(frm) {
    frappe.call({
        "method": "buk.utils.material_request.create_mr_from_quotation",
        "args": {
            "quotation": cur_frm.doc.name
        },
        "callback": function(response) {
            frappe.set_route("Form", "Material Request", response.message);
        }
    });
}
