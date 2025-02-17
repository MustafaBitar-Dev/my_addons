from odoo import models, fields

class TaxType(models.Model):
    _name = 'tax.type'
    _description = 'Tax Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    # Main field
    name = fields.Char(required=True, tracking=True, size=20)
    
    # Database level constrains
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'Tag Type Should Be Unique')
    ]  