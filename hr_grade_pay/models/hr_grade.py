from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrGrade(models.Model):
    _name = 'hr.grade'
    _description = 'Geade'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    # Main field
    grade_number = fields.Integer('Grade', required=True, copy=False, tracking=True)
    
    # Rates fields
    female_rate = fields.Float(default=1, tracking=True, digits=(0,2))
    disability_rate = fields.Float(default=1, tracking=True, digits=(0,2))  
    day_hours = fields.Float(
        string='Required working hours per day', 
        default=8,
        help='This will affect the final pay based on the contract for each employee',
        tracking=True, 
        digits=(0,2))
          
    # Allowances fields
    housing_allowance = fields.Float(tracking=True, digits=(0,2)) 
    education_allowance = fields.Float(tracking=True, digits=(0,2)) 
    transport_allowance = fields.Float(tracking=True, digits=(0,2))
    medical_allowance  = fields.Float(tracking=True, digits=(0,2)) 
    children_allowance = fields.Float(tracking=True, digits=(0,2))
    
    # Special fileds
    is_retirement_eligible = fields.Boolean(string='Ability to retire', tracking=True)
    grade_level = fields.Selection([
        ('entry', 'Entry Level'),
        ('junior', 'Junior'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior'),
        ('lead', 'Lead/Expert'),
        ('executive', 'Executive')], 
        tracking=True)
    
    # Logic level constrains
    @api.constrains('grade_number')
    def _check_positive(self):
        for rec in self:
            if rec.grade_number < 1:               
                raise ValidationError('Grade Number Should Be A Positive Integer')