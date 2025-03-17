# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

from odoo import models,fields

class PosSessionInherit(models.Model):
    _inherit = "pos.session"

    def _loader_params_product_product(self):
        result = super(PosSessionInherit,
                       self)._loader_params_product_product()
        result['search_params']['fields'].extend(["type","qty_available","virtual_available"])
        return result

    # def _pos_data_process(self, loaded_data):
    #     super()._pos_data_process(loaded_data)
        
    #     product_qty_data_dict = {}
    #     for product_data in loaded_data['product.product']:

    #         product_qty_data_dict.update({
    #             product_data['id'] : [product_data['qty_available'], product_data['virtual_available']]
    #         })
        
    #     loaded_data['product_qty_data_dict'] = product_qty_data_dict
        