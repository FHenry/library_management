# Copyright (c) 2013, Frappe
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address

class LibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
		if self.email_id:
			validate_email_address(self.email_id, True)

	def is_valid_membership(self):
		exists = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.name,
				# check for submitted documents
				"docstatus": 1,
				# check if the membership's end date is later than this membership's start date
				"to_date": (">", frappe.utils.today()),
				#"to_date": ("OR", "IS NULL"),
			},
		)
		#frappe.throw(exists)
		if exists:
			self.is_valid_membership_flag = 1
		else:
			self.is_valid_membership_flag = 0

		return self



