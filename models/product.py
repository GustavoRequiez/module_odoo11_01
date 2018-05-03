from openerp import api, fields, models

class Product(models.Model):
    _inherit = 'product.template'

	state =fields.Boolean("State", default=True)
	notes = fields.Char("Notes", required=True)
	
    