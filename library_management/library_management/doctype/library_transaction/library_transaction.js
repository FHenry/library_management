// Copyright (c) 2020, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
    onload_post_render: function(frm) {
        frm.refresh_field('type');
    },
	type: function(frm) {
	    if (frm.doc.type == 'Return') {
            frm.set_query("article", function () {
                return {
                    filters: {
                        status: "Issued",
                    }
                };
            });
        } else {
	        frm.set_query("article", function () {
                return {
                    filters: {
                        status: "Available",
                    }
                };
            });
	        frm.set_query("article", function () {
                return {
                    filters: {
                        status: "Available",
                    }
                };
            });
        }
	}
});
