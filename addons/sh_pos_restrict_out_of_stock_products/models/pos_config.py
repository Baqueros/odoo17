# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    restrict_product_out_of_stock = fields.Boolean(
        string='Restrict Product Out of Stock?')
