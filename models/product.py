from openerp import api, fields, models

class Product(models.Model):
	nombre = fields.Char('Nombre', required=True)
	state = fields.Boolean('State', default=True)
	notes = fields.Char('Notes')
	