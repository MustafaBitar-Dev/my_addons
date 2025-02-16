# HR Grade Pay module

## Create The Module Directory
1. Create the folder (`hr_grade_pay`)
   - Named similarly to other modules (`hr_job`, `hr_contract`, `hr_employee`).
   - The name `grade_pay` is chosen instead of `grade` to avoid confusion with school grades.
2. Create important files: manifest and `__init__`.
3. Create the main model (`hr_grade`).

## hr_grade Model

### Conditions to have a grade:
1. `hr.employee`: `employee_type` is "employee".
2. `hr.contract.type`: `code` is not "Seasonal" or "Interim".

### Main field:
- **Grade number** (Will be inherited in `hr_employee` model).

### Rate fields:
- **Disability rate** (Depends on `hr.employee: has_disability`).
- **Female rate** (Depends on `hr.employee: gender`).
- **Day hours** (Depends on `resource.calendar: hour_per_day`).

### Allowance fields:
- **Medical allowance** (Multiplied by `disability_rate`).
- **Education allowance** (Depends on `hr.employee: certificate`, multiplied by `female_rate`).
- **Children allowance** (Multiplied by `hr.employee: children`).
- **Transport allowance** (Per km, depends on `hr.work.location: work_location_id`, multiplied by `hr.employee: km_home_work`).
- **Housing allowance**.

### Special fields:
- `is_retirement_eligible`
- `grade_level`

### Final Wage Calculation:
```plaintext
final_wage = (wage + allowances) * (1 / day_hours) (hours per day in employee contract)
```

## Views

### Tree View
1. Create view file for `menuitem` and define new menu item (**Grade Pay**).
2. Create another view file for different view types.
3. Call these files in `manifest`.
4. Build the tree view:
   - Allowance fields will be shown.
   - Other fields are optional.

### Form View
1. The **Grade number** will be the title.
2. **Day Hours** will be placed under the title.
3. Other fields will be separated into 3 pages:
   - **Allowances**
   - **Rates**
   - **Special**

### Search View
1. Add custom search for `grade number` and `grade level`:
   - If the user types a number, it will search for `grade number`.
   - If the user types text, it will search for `grade level`.
2. Filtering by `Ability to retire` field.
3. Grouping by `grade level` field.

## Security
1. Create `ir.model.access.csv`.
2. Grant access to all users.
3. Call the file in `manifest`.

## Chatter Box
1. Add `mail` to the `depends` list in `manifest`.
2. Inherit `mail.thread` and `mail.activity.mixin` in `hr_grade` model.
3. Define chatter box fields inside the form view.
4. Set `tracking=True` on all fields in `hr_grade` model.

## Constraints

1. **Grade number should be an integer bigger than 0**  
   *(Python)*
2. **Grade number should be unique**  
   *(SQL)*
3. **All fields should be a positive number**  
   *(Python)*
4. **Day hours must be between 0 - 12**  
   *(Python)*
5. **All allowances should be required**  
   *(Presentation)*

## CRUD Methods

1. **Create method** (`@api.model` or `@api.model_create_multi`)
   - Attributes: `vals`
2. **Search method** (`@api.model`)
   - Attributes: `domain`, `offset`, `limit`, `order`, `access_rights_uid`
3. **Write method**
   - Attributes: `vals`
4. **Unlink method**
   - Attributes: `vals`

## Notes

- Manually grades
- `hr.contract`: `state == [running, draft]`
- Tree view in the documentation
- Other models type
- Readonly property
- Active reserved field
- State property
- `<separator/>` in search view
- `size` attribute
- `create = "1"`
- `edit = "1"`
- `delete = "1"`
- `multi_edit = "1"`


