# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. SeeLICENSE

from __future__ import print_function, unicode_literals

import frappe
from frappe import _

def after_install():
	# create Librarian Default role
	frappe.get_doc({'doctype': "Role", "role_name": "Librarian"}).insert()
	frappe.db.commit()

