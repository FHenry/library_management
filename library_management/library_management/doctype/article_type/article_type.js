// Copyright (c) 2020, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article Type', {
    setup: function(frm) {
        // Setup default icon type
        let data = JSON.stringify(GetAppliedCssRules());
        frm.call('build_icon_type',{data: data}).then(
            frm.set_query("picto", function () {
                return {
                    query: "library_management.library_management.doctype.article_type_icon.article_type_icon.get_picto_list",
                }
            })
        )
    },
});

// return an array with all "octicon" CSS class available
function GetAppliedCssRules() {
    let appliedOcticon = [];
    let rules = [] ;
    for (let x = 0; x < document.styleSheets.length; x++) {
        try {
            rules = document.styleSheets[x].cssRules;
        } catch(e) {
            if (e instanceof DOMException) {
                console.log (document.styleSheets[x]);
            }
        } finally {
            for (let i = 0; i < rules.length; i++) {
                let txt = rules[i].selectorText;
                if (typeof txt !== 'undefined' && txt.indexOf('octicon-') > -1 && txt.indexOf('::before') > -1) {
                    let style_detail = txt.split("-");
                    if (style_detail.length > 0) {
                        let icon_name = style_detail[1].split('::before');
                        if (icon_name.length > 0 && !appliedOcticon.includes(icon_name[0])) {
                            appliedOcticon.push(icon_name[0]);
                        }
                    }
                }
            }
        }
    }
    return appliedOcticon;
}