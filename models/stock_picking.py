from odoo import models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    shipping_hold = fields.Boolean("Shipping Hold")