from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrPayScale(models.Model):
    _name = 'hr.pay.scale'
    _description = 'Pay Scale'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    # Main fields
    name = fields.Char(required=True, tracking=True, size=30)
    max_salary = fields.Float(required=True, tracking=True, digits=(0, 2))
    min_salary = fields.Float(required=True, tracking=True, digits=(0, 2))
    
    # Relationship with hr_grade model
    grade_ids = fields.One2many('hr.grade', 'pay_scale_id')
    
    # Database level constrains
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'Name Should Be Unique')
    ]  
    
    # Logic level constrains
    @api.constrains('max_salary', 'min_salary')
    def _check_max_salary(self):
        for rec in self:
            if rec.max_salary < rec.min_salary:               
                raise ValidationError('Max Salary Should Be Bigger Than Min Salary')
    