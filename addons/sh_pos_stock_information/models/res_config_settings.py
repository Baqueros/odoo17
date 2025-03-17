# Part of Softhealer Technologies.

from odoo import models, fields, api

class ResConfigSettiongsInhert(models.TransientModel):
    _inherit = "res.config.settings"

    pos_sh_enable_on_hand_qty = fields.Boolean(
        related="pos_config_id.sh_enable_on_hand_qty", readonly=False)
    
    pos_sh_manage_stock = fields.Selection(
        related="pos_config_id.sh_manage_stock", readonly=False)