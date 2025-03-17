/** @odoo-module */
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";

patch(PaymentScreen.prototype, {
    async afterOrderValidation(suggestToSync = true) {
        const orderlines = this.currentOrder.get_orderlines();
        for (let j = 0; j < orderlines.length; j++) {
            const orderLine = orderlines[j];
            if (orderLine.product) {
                orderLine.product.qty_available -= orderLine.quantity
                orderLine.product.virtual_available -= orderLine.quantity
            }
        }
        return await super.afterOrderValidation(...arguments);
    },
});
