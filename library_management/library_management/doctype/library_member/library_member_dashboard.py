from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on transactions against this Members. See timeline below for details'),
		'fieldname': 'library_member',
		'method':'library_management.library_management.doctype.library_member.library_member.get_count_and_timeline_operation',
		'transactions': [
			{
				'label': _('Transaction'),
				'items': ['Library Transaction']
			},
			{
				'label': _('Membership'),
				'items': ['Library Membership']
			}
		]
	}
