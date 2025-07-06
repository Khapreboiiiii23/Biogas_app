from __future__ import unicode_literals
import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Plant", "fieldname": "plant", "fieldtype": "Link", "options": "Plant", "width": 180},
        {"label": "Gas Output", "fieldname": "gas_output", "fieldtype": "Float", "width": 120},
    ]

    data = frappe.db.get_all(
        "Gas Output Log",
        filters={
            "plant": filters.get("plant"),
            "date": ["between", [filters.get("from_date"), filters.get("to_date")]]
        },
        fields=["date", "plant", "gas_output"]
    )

    return columns, data
