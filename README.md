# HR Grade Pay Module

## Create The Module Directory

1. Create the folder (`hr_grade_pay`)
   - Named similarly to other HR modules (`hr_job`, `hr_contract`, `hr_employee`).
   - The name `grade_pay` is used instead of `grade` to avoid confusion with school grades.
2. Create important files: `__manifest__.py` and `__init__.py`
3. Create the main model (`hr.grade`)

## `hr.grade` Model

### Conditions to Have a Grade
- `hr.employee`: `employee_type` must be "employee".
- `hr.contract.type`: `code` must not be "Seasonal" or "Interim".

### Main Field
- **Grade number** (Inherited in `hr.employee` model)

### Rate Fields
- **Disability rate** (Depends on new field in `hr.employee`: `has_disability`)
- **Female rate** (Depends on `hr.employee`: `gender`)
- **Day hours** (Depends on `resource.calendar`: `hours_per_day`)

### Allowance Fields
- **Medical allowance** (Depends on `hr_employee: has_disability`, multiplied by `disability_rate`)
- **Education allowance** (Depends on `hr.employee: certificate` (not Master or Doctor), multiplied by `female_rate`)
- **Children allowance** (Multiplied by `hr.employee: children`)
- **Transport allowance** (Per km, depends on `hr.work.location: work_location_id`, multiplied by `hr.employee: km_home_work`)
- **Housing allowance**

### Special Fields
- `is_retirement_eligible`
- `grade_level`

### Final Wage Calculation
```
final_wage = wage + allowances * (1 / day_hours) (hours per day in employee contract)
```
Final wage will be ensured in the pay scale.

### Relations
- **One2Many**: `line_ids = fields.One2many('hr.employee', 'grade_id')`
- **Many2one**: `pay_scale_id`
- **Many2many**: `tax_type_ids`

## Views

### Tree View
1. Create a view file for the menu item and define a new menu item (`Grade`).
2. Create another view file for different view types.
3. Call these files in `__manifest__.py`.
4. Build the tree view, showing allowance fields while making other fields optional.
5. Add `pay_scale_id` as an optional field.

### Form View
1. The **grade number** will be the title.
2. **Day Hours** displayed under the title.
3. Other fields will be separated into three pages:
   - Allowances
   - Rates
   - Special
4. Add `pay_scale_id` field.
5. Add `max_salary` and `min_salary` from `pay_scale` model.

### Search View
1. Custom search for `grade number` and `grade level`:
   - If user types a number → search by `grade number`.
   - If user types text → search by `grade level`.
2. Filtering by **ability to retire** field.
3. Grouping by **grade level** field.

## Security
1. Create `ir.model.access.csv`.
2. Grant access to all users.
3. Call the file in `__manifest__.py`.

## Chatter Box
1. Add `'mail'` to `depends` list in `__manifest__.py`.
2. Inherit `mail.thread` and `mail.activity.mixin` in `hr_grade` model.
3. Add Chatter Box fields inside the form view.
4. Set the attribute `tracking=True` on all fields in `hr_grade` model.

## Constraints
1. **Grade number** should be an integer greater than 0 (Python).
2. **Grade number** should be unique (SQL).
3. **All fields** should be positive numbers (Python).
4. **Day hours** must be between 0 - 12 (Python).
5. **All allowances** should be required (Presentation).

## CRUD Methods
1. **Create Method** (`@api.model` or `@api.model_create_multi`)
   - Attributes: `vals`
2. **Search Method** (`@api.model`)
   - Attributes: `domain`, `offset`, `limit`, `order`, `access_rights_uid`
3. **Write Method**
   - Attributes: `vals`
4. **Unlink Method**
   - Attributes: `vals`

## `hr.pay_scale` Model

### Main Fields
- **Name**
- **Max salary**
- **Min salary**

### Relations
- **One2Many**: `grade_ids`

### Views
- **Tree View**: Display all fields.
- **Form View**: Display all fields with related grades.

## `tax_type` Model

### Main Field
- **Name**

### Views
- **Tree View**: Display name field.
- **Form View**: Display name field.

## `hr.employee` Inherited Model

### New Fields
- `grade_id = fields.Many2one('hr.grade')`

### Customizing the Form View
1. Display **grade number**.
2. Add new page (**Salary Information**).
3. Add new field (**Wage**).
4. Add **Visa Status Bar**.
5. Add **Visa Expired Button**.
6. Add **Valid Visa Server Action**.

## Cron Job
1. Apply cron job for visa expiration.

## Sequence
- Add employee sequence.

## Blockers
1. Custom style for visa status.
2. PDF Report.
