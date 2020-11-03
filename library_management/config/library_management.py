from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Library Management"),
			"icon": "octicon octicon-book",
			"items": [
				{
					"type": "doctype",
					"name": "Article",
					"label": _("Article"),
					"description": _("Manage Books"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Member",
					"label": _("Library Member"),
					"description": _("Manage Members"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Membership",
					"label": _("Library Membership"),
					"description": _("Manage Membersship"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Transaction",
					"label": _("Library Transaction"),
					"description": _("Manage Members Transaction"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Settings",
					"label": _("Library Settings"),
					"description": _("Manage Library Settings"),
					"onboard": 0,
				},
			]
        },
    ]