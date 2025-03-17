# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pw_hide_invoice = fields.Boolean('Hide Invoice')

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pw_hide_invoice = fields.Boolean(related='pos_config_id.pw_hide_invoice', readonly=False)
