from odoo import models, fields, api
from datetime import timedelta


class HREmployee(models.Model):
    _inherit = 'hr.employee'
    
    # Relationship with hr_grade model
    grade_id = fields.Many2one('hr.grade')
    
    visa_status = fields.Selection([
        ('valid', 'Valid'),
        ('soon', 'Expired Soon'),
        ('expired', 'Expired'),
    ], default="valid", tracking=True)
    
    # From chat gpt
    _inherits = {'hr.grade': 'grade_id'}

    # New fields
    salary = fields.Float(compute= '_compute_salary')
    
    allowances_sum = fields.Float(compute= '_compute_salary')
    
    has_disability = fields.Boolean()
    
    hours_per_day = fields.Float(related='contract_id.resource_calendar_id.hours_per_day')
    
    contract_type_id = fields.Many2one(related='contract_id.contract_type_id')
    contract_code = fields.Char(related='contract_type_id.code')
    
    work_location_name = fields.Char(related='work_location_id.name')
    
    wage = fields.Monetary(related='contract_id.wage')
    
    @api.depends(
        'salary', 'has_disability', 'hours_per_day', 'contract_code', 'employee_type',
        'allowances_sum', 'wage', 'education_allowance', 'transport_allowance', 'medical_allowance', 
        'children_allowance', 'children', 'pay_scale_max_salary', 'pay_scale_min_salary',
        'certificate', 'gender', 'female_rate', 'disability_rate', 'work_location_name',
        'km_home_work', 'housing_allowance', 'day_hours')
    def _compute_salary (self):
        for rec in self:
            
            if rec.employee_type == 'employee' and rec.contract_code not in ['Seasonal', 'Interim']:
                # Aplly housing allowance
                allowances =  rec.housing_allowance 
 
                # education_allowance will applied if the certificate not too high 
                # Also it will be increased for female employee
                if rec.certificate in ['master', 'doctor']:
                    rec.education_allowance = 0
                elif rec.gender == 'female':
                    allowances += rec.education_allowance * rec.female_rate
                else:
                    allowances += rec.education_allowance
                    
                # medical_allowance will be increased if the employee has disability
                if rec.has_disability:                  
                    allowances += rec.medical_allowance * rec.disability_rate
                else:
                    allowances += rec.medical_allowance

                # The employee have transport_allowance only if not working from Home
                # This allowance will be increased based on the distance
                if rec.work_location_name != 'Home':
                    allowances += rec.transport_allowance * rec.km_home_work
                    
                # Apply children allowance based on their count
                allowances += rec.children_allowance * rec.children
                
                # If the employee work hours in his contract less than the grade required 
                # hours, then this will decrease the allowances.
                if rec.day_hours and rec.hours_per_day and rec.hours_per_day < rec.day_hours: 
                    hour_rate = rec.hours_per_day / rec.day_hours                           
                else:
                    hour_rate = 1           
                allowances *= hour_rate                   

                # Check pay scale
                if allowances > rec.pay_scale_max_salary:
                    allowances = rec.pay_scale_max_salary
                if allowances < rec.pay_scale_min_salary:
                    allowances = rec.pay_scale_min_salary
                
                
                # Total allowances
                rec.allowances_sum = allowances
                
                # Final result
                rec.salary = rec.wage + allowances
            else:
                rec.salary = 0
                
    def action_expired(self):
        for rec in self:
            rec.write(
                {'visa_status': 'expired'}
            )
            
    def action_valid(self):
        for rec in self:
            rec.write(
                {'visa_status': 'valid'}
            )

    def check_visa_expiration(self):
        employee_ids = self.search([])  
        for rec in employee_ids:           
            if rec.visa_expire:
                if rec.visa_expire < fields.date.today():
                    rec.visa_status = 'expired'              
                elif rec.visa_expire - timedelta(30) < fields.date.today():
                    rec.visa_status = 'soon'
                else:
                    rec.visa_status = 'valid'    
        