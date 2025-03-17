/** @odoo-module */
import { Order, Orderline } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";
import { StockInformationPopup } from "@sh_pos_restrict_out_of_stock_products/app/popups/StockInformation_popup/StockInformation_popup"
patch(Order.prototype, {
    add_orderline(line) {
        line.skip_qty_check = false
        if (!line.refunded_orderline_id) {
            line._checkStockQty(false)
        }
        super.add_orderline(...arguments)
    }
});

patch(Orderline.prototype, {
    async setup(obj, options) {
        await super.setup(obj, options)
    },
    async set_quantity(quantity, keep_price) {
        console.log("qt y==> ",quantity);
        let curr_qty = this.quantity === undefined ? false : this.quantity
        if (quantity && this.order && this.order.orderlines && this.order.orderlines.includes(this)) {
            this._checkStockQty(curr_qty)
        }
        return super.set_quantity(...arguments);
    },
    async _checkStockQty(curr_qty) {
        let self = this
        console.log("1 ==>", self.pos.config.restrict_product_out_of_stock);
        console.log("2 ==>",self.pos.order_product_qty, self.pos.order_product_qty[self.product.id]);
        console.log("3 ==>", self.product.qty_available  , self.pos.order_product_qty[self.product.id] , self.product.qty_available - self.pos.order_product_qty[self.product.id] );
        console.log("4 ==>", this.product.type);
        console.log("5 ==>", this.skip_qty_check);
        if (self.pos.config.restrict_product_out_of_stock && 
            (self.product.qty_available - (self.pos.order_product_qty[self.product.id] || 0)-curr_qty) <= 0 && 
            this.product.type == "product" && 
            !this.skip_qty_check){
            const add_order = await self.pos.env.services.popup.add(StockInformationPopup, {
                product: self.product
            })
            console.log("confirmed", add_order);
            if (!add_order.confirmed) {
                self._setRestrictedStockQty(curr_qty)
                
            }

        } else {
            this.skip_qty_check = false
        }
    },
    _setRestrictedStockQty(qty) {
        this.skip_qty_check = true
        console.log("qty ===>", qty);
        if (!qty) {
            this.set_quantity(0)
            this.order.removeOrderline(this)
        } else {
            this.set_quantity(qty)
        }
    }

});
