{
  'name': 'Grade Pay',
  'author': 'CNC',
  'category': 'Human Resources/Employees',
  'version': '17.0.0.1.0',
  'depends': ['base', 'mail', 'hr'],
  'application': True,
  'data': [
    'security/ir.model.access.csv',
    'data/sequence.xml',
    'views/base_menu.xml',
    'views/hr_grade_view.xml',
    'views/hr_pay_scale_view.xml',
    'views/tax_type_view.xml',
    'views/hr_employee_view.xml',
    'wizard/change_visa_status_view.xml'
    # 'reports/hr_grade_report.xml'
  ],
  'assets': {
    'web.assets_backend': ['hr_grade_pay/static/src/css/hr_employee.css']
  } 
}