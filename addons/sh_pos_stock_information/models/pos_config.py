# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    sh_enable_on_hand_qty = fields.Boolean(string='Display Stock Information')
    sh_manage_stock = fields.Selection([('on_hand_qty', 'Display On Hand Qty'), (
        'available_qty', 'Display Virtual Quantity'), ('both', 'Both')], string='Stock Information', default='on_hand_qty')
