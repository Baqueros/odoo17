# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

from odoo import models, fields

class ResConfigSettiongsInhert(models.TransientModel):
    _inherit = "res.config.settings"

    pos_restrict_product_out_of_stock = fields.Boolean(
        related="pos_config_id.restrict_product_out_of_stock", readonly=False)
    