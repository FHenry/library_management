# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ArticleTypeIcon(Document):
	def before_save(self):
		self.icon_picto = '<div class="octicon octicon-' + self.css_class + '"></div>'
		self.icon_picto_name = '<div class="octicon octicon-' + self.css_class + '">' + self.css_class + '</div>'

@frappe.whitelist()
def get_picto_list(doctype, txt, searchfield, start, page_len, filters):
	icons_list = []
	for i in frappe.db.get_all(doctype=doctype,order_by='name', filters ={'name':['like', '%'+txt+'%']}):
		icons_list.append((i.name,'<div class="octicon octicon-'+i.name+'">'+i.name+'</div>'))
	return icons_list