from odoo import models, fields

class HREmployee(models.Model):
    _inherit = 'hr.employee'
    
    # Relationship with hr_grade model
    grade_id = fields.Many2one('hr.grade')
   