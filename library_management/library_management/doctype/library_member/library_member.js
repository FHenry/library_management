// Copyright (c) 2020, Frappe and contributors
// For license information, please see LICENSE

frappe.ui.form.on('Library Member', {
	refresh: function(frm) {
	    frm.call('is_valid_membership').then(data => {
	        console.log(data.message.is_valid_membership_flag);
           if (data.message.is_valid_membership_flag==1) {
               frm.add_custom_button('Create Transaction', () => {
                    frappe.new_doc('Library Transaction', {
                        library_member: frm.doc.name
                    })
                })
           } else {
               frm.add_custom_button('Create Membership', () => {
                    frappe.new_doc('Library Membership', {
                        library_member: frm.doc.name
                    })
                })
           }
        })
    }
});
