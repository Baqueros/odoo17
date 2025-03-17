# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PosConfig(models.Model):
    _inherit = 'pos.config'

    is_auto_invoice = fields.Boolean('Auto Invoicing')

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_auto_invoice = fields.Boolean(related='pos_config_id.is_auto_invoice',readonly=False)
