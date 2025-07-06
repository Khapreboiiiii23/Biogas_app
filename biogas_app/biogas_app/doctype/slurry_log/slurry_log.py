# Copyright (c) 2025, Aradhya_khapre and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Slurrylog(Document):
	def validate(self):
		if self.moisture < 0 or self.moisture > 100:
			frappe.throw("Moisture (%) must be between 0 and 100.")

