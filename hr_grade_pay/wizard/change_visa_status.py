from odoo import models, fields

class ChangeVisaStatus(models.TransientModel):
    _name = 'change.visa.status'
    
    employee_id = fields.Many2one('hr.employee')
    visa_status = fields.Selection([
        ('valid', 'Valid'),
        ('soon', 'Expired Soon'),
        ('expired', 'Expired')
    ])  
    reason = fields.Char()
    
    def action_confirm(self):
        if self.employee_id.visa_status == 'canceled':
            self.employee_id.visa_status = self.visa_status