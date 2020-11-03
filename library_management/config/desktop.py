from frappe import _

def get_data():
	return \
		[
			# Library Management
			{
				"module_name": "Library Management",
				"category": "Modules",
				"label": _("Library Management"),
				"color": "#589494",
				"reverse": 1,
				"icon": "octicon octicon-book",
				"type": "module",
				"description": "Todos, notes, calendar and newsletter."
			},
		]