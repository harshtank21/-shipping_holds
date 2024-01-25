from odoo import models, fields
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    shipping_hold = fields.Boolean("Shipping Hold")

    def button_validate(self):
        if self.shipping_hold == True:
            raise ValidationError(
                f"This stock movement is currently on Shipping Hold. Its associated Sales Order {self.origin} must be taken off hold before it can be validated")

        return super().button_validate()
