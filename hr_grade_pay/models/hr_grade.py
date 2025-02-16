from odoo import models, fields

class HrGrade(models.Model):
    _name = 'hr.grade'
    _description = 'Geade'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    # Main field
    grade_number = fields.Integer('Grade', required=True, copy=False, tracking=True)
    
    # Rates fields
    female_rate = fields.Float(default=1, tracking=True)
    disability_rate = fields.Float(default=1, tracking=True)  
    day_hours = fields.Float(
        string='Required working hours per day', 
        default=8,
        help='This will affect the final pay based on the contract for each employee',
        tracking=True)
          
    # Allowances fields
    housing_allowance = fields.Float(tracking=True) 
    education_allowance = fields.Float(tracking=True) 
    transport_allowance = fields.Float(tracking=True)
    medical_allowance  = fields.Float(tracking=True) 
    children_allowance = fields.Float(tracking=True)
    
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