from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrPayScale(models.Model):
    _name = 'hr.pay.scale'
    _description = 'Pay Scale'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(required=True, tracking=True)
    max_salary = fields.Float(required=True, tracking=True)
    min_salary = fields.Float(required=True, tracking=True)
    
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'Name Should Be Unique')
    ]  
    
    @api.constrains('max_salary', 'min_salary')
    def _check_max_salary(self):
        for rec in self:
            if rec.max_salary < rec.min_salary:               
                raise ValidationError('Max Salary Should Be Bigger Than Min Salary')
    