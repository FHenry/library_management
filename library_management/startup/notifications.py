# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

def get_notification_config():
	# When click on badge of open Library Transaction into member dashboard show list of transaction filtered with docstatus=0
	# check library_management/hook.py
    return {
		"for_doctype":
		{
			"Library Transaction": {"docstatus": 0}
		}
	}