from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    shipping_hold = fields.Boolean("Shipping Hold")

    def action_confirm(self):
        res= super().action_confirm()
        if self.shipping_hold:
            record=self.env["stock.picking"].search([("origin", "=", self.name)])
            print(record.state)
            if record.state != "done":
                record.shipping_hold = True
        return res
