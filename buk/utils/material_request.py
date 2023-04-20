import frappe
from frappe.utils.data import nowdate

@frappe.whitelist()
def create_mr_from_quotation(quotation):
    quotation_doc = frappe.get_doc("Quotation", quotation)
    items = []
    for item in quotation_doc.items:
        items.append({
            'item_code': item.item_code,
            'item_name': item.item_name,
            'description': item.description,
            'item_group': item.item_group,
            'qty': item.qty,
            'uom': item.uom,
            'schedule_date': nowdate(),
            'rate': item.rate,
            'quotation': quotation
        })
    mr = frappe.get_doc({
        'doctype': 'Material Request',
        'material_request_type': 'Purchase',
        'schedule_date': nowdate(),
        'items': items
    }).insert()
    return mr.name
