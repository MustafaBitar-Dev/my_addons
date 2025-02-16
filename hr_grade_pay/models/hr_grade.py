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
    
    # Database level constrains
    _sql_constraints = [
        ('unique_grade_number', 'unique("grade_number")', 'Grade Number Should Be Unique')
    ]   
  
    # Logic level constrains
    @api.constrains('grade_number')
    def _check_greater_than_zero(self):
        for rec in self:
            if rec.grade_number <= 0:               
                raise ValidationError('Grade Number Should Be A Positive Integer')
            
    @api.constrains(
        'disability_rate', 'female_rate', 'day_hours', 'housing_allowance',
        'education_allowance', 'transport_allowance', 'medical_allowance',
        'children_allowance' )
    def _check_positive(self):
        field_names = [
            'disability_rate', 'female_rate', 'day_hours', 'housing_allowance',
            'education_allowance', 'transport_allowance', 'medical_allowance',
            'children_allowance'
        ]
        for rec in self:
            for field_name in field_names:
                if rec[field_name] < 0:
                    raise ValidationError( field_name.replace('_', ' ').title() + " Can't Be A Nigative Number")
       
    # CRUD Methods 
    @api.model_create_multi # or @api.model      
    def create(self, vals):
        res = super(HrGrade, self).create(vals)
        # Another way: res = super().create(self, vals)
        return res
    
    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        res = super(HrGrade, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
        return res

    def write(self, vals):
       res = super(HrGrade, self).write(vals)
       return res
   
    def unlink(self):
        res = super(HrGrade, self).unlink()
        return res
   