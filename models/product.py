from openerp import api, fields, models

class Product(models.Model):
    _inherit = 'product'

	state = fields.Boolean('State', default=True)
	notes = fields.Char('Notes')