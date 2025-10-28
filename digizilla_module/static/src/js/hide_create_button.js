/** @odoo-module **/

import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";

patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
    },

    get className() {
        const className = super.className;
        // Check if we're in the digizilla.digizilla model
        if (this.props.resModel === "digizilla.digizilla") {
            return `${className} o_digizilla_form`;
        }
        return className;
    }
});

// CSS to hide the create button for digizilla forms
const style = document.createElement('style');
style.textContent = `
    .o_digizilla_form .o_form_button_create {
        display: none !important;
    }
    .o_digizilla_form .o_control_panel_main_buttons .o_form_button_create {
        display: none !important;
    }
`;
document.head.appendChild(style);