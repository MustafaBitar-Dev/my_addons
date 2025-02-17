from odoo import models, fields

class HREmployee(models.Model):
    _inherit = 'hr.employee'
    
    # Relationship with hr_grade model
    grade_id = fields.Many2one('hr.grade')
    
    # this is from chat gpt, if you reach this line please speak with me about it     
    _inherits = {'hr.grade': 'grade_id'}
    
    wage = fields.Float(store = False)