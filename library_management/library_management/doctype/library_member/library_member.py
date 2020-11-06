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

	def is_valid_membership_populate(self):
		exists = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.name,
				"docstatus": 1,
				# check if the membership's end date is later than this membership's start date
				"to_date": (">", frappe.utils.today()),
			},
		)
		if exists:
			self.is_valid_membership_flag = 1
		else:
			self.is_valid_membership_flag = 0

	def is_valid_membership(self):
		self.is_valid_membership_populate()
		return self

@frappe.whitelist()
def get_valid_members(doctype, txt, searchfield, start, page_len, filters):
	valid_members=[]
	#Return a list of Tuple(name,title field) for (value, search data) of only members with valid subscription
	meta = frappe.get_meta(doctype)
	for member_record in frappe.db.get_all(doctype=doctype, as_list=True):
		member = frappe.get_doc(doctype, member_record[0])
		member.is_valid_membership_populate()
		if member.is_valid_membership_flag == 1:
			if meta.title_field:
				description = getattr(member, meta.title_field)
			else:
				description = ''
			valid_members.append((member.name, description))
	return valid_members

@frappe.whitelist()
def get_count_and_timeline_operation(doctype, name):
	timeline_data={}
	# time line
	for member_record in frappe.db.get_all(
			doctype="Library Membership",
			fields=['from_date'],
			filters={
				"library_member": name,
			},
	):
		timeline_data.update({frappe.utils.get_timestamp(member_record.from_date): 1})

	for member_record in frappe.db.get_all(
			doctype="Library Transaction",
			fields=['date'],
			filters={
				"library_member": name,
				"type": ('in', ("Borrow","Issue")),
			 	"docstatus": 1,
			},
	):
		timeline_data.update({frappe.utils.get_timestamp(member_record.date): 1})

	out={
		"timeline_data": timeline_data
	}

	count = []
	# count
	count.append({
		"name":"Library Membership",
		"open_count": frappe.db.count(
		"Library Membership",
		filters={
			"library_member": name,
			"docstatus": 1,
		}),
		"count": frappe.db.count(
		"Library Membership",
		filters={
			"library_member": name,
		})
	})
	count.append({
		"name":"Library Transaction",
		"open_count":frappe.db.count(
		"Library Transaction",
		filters={
			"library_member": name,
			"docstatus": 0,
		}),
		"count": frappe.db.count(
		"Library Transaction",
		filters={
			"library_member": name,
		})
	})
	out["count"]=count

	return out


