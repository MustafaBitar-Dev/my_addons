{
  'name': 'Grade Pay',
  'author': 'CNC',
  'category': 'Human Resources/Employees',
  'version': '17.0.0.1.0',
  'depends': ['base', 'mail'],
  'application': True,
  'data': [
    'security/ir.model.access.csv',
    'views/base_menu.xml',
    'views/hr_grade_view.xml'
  ]
}