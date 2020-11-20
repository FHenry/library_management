# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document

class ArticleType(Document):
	def build_icon_type(self, data):
		# if icon type do not exits then create it in doctype
		if data:
			icons = json.loads(data)
			for icon_class in icons:
				if not frappe.db.exists(
						dt='Article Type Icon',
						dn={
							"css_class": icon_class,
						}):
					icon = frappe.new_doc('Article Type Icon')
					icon.css_class = icon_class
					icon.insert()
