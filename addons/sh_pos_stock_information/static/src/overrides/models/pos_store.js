/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    get order_product_qty() {
        let orderProductQty = {};
        let order_list = this.get_order_list();
        for (let i = 0; i < order_list.length; i++) {
            const order = order_list[i];
            const orderlines = order.get_orderlines();
            for (let j = 0; j < orderlines.length; j++) {
                const orderLine = orderlines[j];
                if (orderLine.product) {
                    const productId = orderLine.product.id;
                    const quantity = orderLine.quantity;

                    if (!orderProductQty[productId]) {
                        orderProductQty[productId] = 0;
                    }
                    orderProductQty[productId] += quantity;
                }
            }
        }
        return orderProductQty;
    }
});
