{
  'name': 'Grade Pay',
  'author': 'CNC',
  'category': 'Human Resources/Employees',
  'version': '17.0.0.1.0',
  'depends': ['base', 'mail', 'hr'],
  'application': True,
  'data': [
    'security/ir.model.access.csv',
    'views/base_menu.xml',
    'views/hr_grade_view.xml',
    'views/hr_pay_scale_view.xml',
    'views/tax_view.xml',
    'views/hr_employee_view.xml'
  ]
}