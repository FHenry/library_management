// Copyright (c) 2020, Frappe and contributors
// For license information, please see LICENSE

frappe.ui.form.on('Library Transaction', {
    setup: function(frm) {
        if (frm.is_new()) {
            frm.set_query("library_member", function () {
                return {
                    query: "library_management.library_management.doctype.library_member.library_member.get_valid_members"
                }
            })
        }
    },
    onload: function(frm) {
       if (frm.is_new()) {
           frm.trigger("set_query_article_and_member");
       }
    },
    type: function(frm) {
        frm.trigger("set_query_article_and_member");
    },
	set_query_article_and_member: function(frm) {
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
        }
	}
});
