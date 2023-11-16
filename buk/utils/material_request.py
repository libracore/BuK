import frappe
from frappe.utils.data import nowdate
from frappe.utils.xlsxutils import make_xlsx
import six
from io import BytesIO
import openpyxl

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

@frappe.whitelist()
def create_mr_excel_export(material_request):
	
	#get data from Material Request
	data = frappe.db.sql("""
		SELECT `sinvitem`.`qty`,
			`sinvitem`.`uom`,
			`sinvitem`.`item_code`,
			`sinvitem`.`item_group`
		FROM `tabMaterial Request Item` AS `sinvitem`
		LEFT JOIN `tabMaterial Request` AS `sinv` ON `sinvitem`.`parent` = `sinv`.`name`
		WHERE `sinv`.`name` = '{mr}'
		""".format(mr=material_request), as_dict=True)
		
	wb = openpyxl.Workbook(write_only=True)
	ws = wb.create_sheet('MaterialRequest', 0)
		
	#create grid and add data to it
	# ~ columns = ["Menge", "Einheit", "Artikel-Code", "Artikelgruppe"]
	# ~ rows = []
	
	
	
	for entry in data:
		row = [entry.get('qty'), entry.get('uom'), entry.get('item_code'), entry.get('item_group')]
		ws.append(row)
	
	# ~ xlsx_data = [columns] + rows
	# ~ frappe.log_error(xlsx_data)
	
	# ~ xlsx_file = make_xlsx("material_request", xlsx_data)
	
	xlsx_file = BytesIO()
	wb.save(xlsx_file)
	# ~ xlsx_io.write(xlsx_file)

	# ~ filename = 'material_request.xlsx'
	
	# ~ file_path = "/tmp/material_request.xlsx"
	# ~ with open(file_path, "wb") as file:
		# ~ file.write(xlsx_file)

	# ~ frappe.download(xlsx_file.getvalue(), filename=filename, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
	frappe.log_error(xlsx_file)
	return xlsx_file
