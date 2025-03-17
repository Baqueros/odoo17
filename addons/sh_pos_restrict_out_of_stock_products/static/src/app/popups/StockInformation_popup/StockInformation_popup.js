/** @odoo-module */

import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { _t } from "@web/core/l10n/translation";

export class StockInformationPopup extends AbstractAwaitablePopup {
    static template = "sh_pos_restrict_out_of_stock_products.StockInformationPopup";

    setup() {
        super.setup()
    }  
}
