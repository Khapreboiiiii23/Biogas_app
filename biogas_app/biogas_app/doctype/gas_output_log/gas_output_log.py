# Copyright (c) 2025, Aradhya_khapre and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Gasoutputlog(Document):
	def validate (self):
			if self.methane_ <0 or self.methane_ > 100:
				frappe.throw("Methane(%) must be between 0 and 100.") 
