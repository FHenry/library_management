# Copyright (c) 2013, Frappe
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class LibraryTransaction(Document):
	#def before_save(self):
	#	self.title = f'{self.member_full_name} {self.article_name} {self.transaction_date}'

	def before_submit(self):
		if self.type == "Issue":
			self.validate_issue()
			self.validate_maximum_limit()
			# set the article status to be Issued
			article = frappe.get_doc("Article", self.article)
			article.status = "Issued"
			article.save()

		elif self.type == "Return":
			self.validate_return()
			# set the article status to be Available
			article = frappe.get_doc("Article", self.article)
			article.status = "Available"
			article.save()

	def validate_issue(self):
		self.validate_membership()
		article = frappe.get_doc("Article", self.article)
		# article cannot be issued if it is already issued
		if article.status == "Issued":
			frappe.throw("Article is already issued by another member")

	def validate_return(self):
		article = frappe.get_doc("Article", self.article)
		# article cannot be returned if it is not issued first
		if article.status == "Available":
			frappe.throw("Article cannot be returned without being issued first")

	def validate_maximum_limit(self):
		max_articles = frappe.db.get_single_value("Library Settings", "max_number_per_period")
		period_max = frappe.db.get_single_value("Library Settings", "max_period")

		if period_max == 'Week':
			to_date = frappe.utils.add_days(frappe.utils.today(), 7)
			from_date = frappe.utils.add_days(frappe.utils.today(), -7)

		elif period_max == 'Month':
			to_date = frappe.utils.add_months(frappe.utils.today(), 1)
			from_date = frappe.utils.add_months(frappe.utils.today(), -1)

		elif period_max == 'Month':
			to_date = frappe.utils.add_years(frappe.utils.today(), 1)
			from_date = frappe.utils.add_years(frappe.utils.today(), -1)

		count = frappe.db.count(
			"Library Transaction",
			{"library_member": self.library_member,
			 "type": "Issue",
			 "docstatus": 1,
			 "date": ("<=", to_date),
			 "date": (">", from_date)},
		)
		if count >= max_articles:
			frappe.throw("Maximum limit(",count,")reached for issuing articles for period ", period_max)

	def validate_membership(self):
		# check if a valid membership exist for this library member
		valid_membership = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": 1,
				"from_date": ("<=", self.date),
				"to_date": (">", self.date),
			},
		)

		if not valid_membership:
			frappe.throw("The member does not have a valid membership")