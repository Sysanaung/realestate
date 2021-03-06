# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

class RealEstateSettings(Document):
	def validate(self):
		if self.enable_real_estate == 1:
			# setup_custom_fields()
			pass

@frappe.whitelist()
def setup_custom_fields():
	custom_fields = {
		"Project": [
			dict(
				fieldname='realestate_project_details',
				label='RealEstate Project Details ',
				fieldtype='Section Break',
				insert_after='sales_order'
			),
			dict(
				fieldname='realestate_project',
				label='RealEstate Project',
				fieldtype='Link',
				options='RealEstate Project',
				insert_after='realestate_project_details',
			),		
		],
		"Purchase Invoice": [
			dict(
				fieldname='project_reference',
				label='Project Reference',
				fieldtype='Link',
				options='Project',
				insert_after='supplier_name'
			),
		],
		"Journal Entry": [
			dict(
				fieldname='realestate_payment_entry',
				label='RealEstate Payment Entry',
				fieldtype='Link',
				options='RealEstate Payment Entry',
				insert_after='reference'
			),
		]
	}

	create_custom_fields(custom_fields)
	frappe.msgprint("Custome Field update done.")