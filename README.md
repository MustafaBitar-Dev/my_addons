# HR Grade Pay Module

## Create The Module Directory

1. Create the folder (`hr_grade_pay`)  
   - Named similarly to other modules (`hr_job`, `hr_contract`, `hr_employee`).  
   - The name `grade_pay` is chosen instead of `grade` to avoid confusion with school grades.

2. Create important files: `__manifest__.py` and `__init__.py`.

3. Create the main model (`hr_grade`).

---

## hr_grade Model

### Conditions to have a grade
1. `hr.employee`: `employee_type` must be `"employee"`.
2. `hr.contract.type`: `code` should not be `"Seasonal"` or `"Interim"`.

### Main Field:
- **Grade number**  
  *(Will be inherited in the `hr_employee` model)*

### Rate Fields:
- **Disability rate**  
  *(Depends on new field in `hr.employee`: `has_disability`)*  
- **Female rate**  
  *(Depends on `hr.employee`: `gender`)*  
- **Day hours**  
  *(Depends on `resource.calendar`: `hour_per_day`)*  

### Allowance Fields:
- **Medical Allowance**  
  *(Multiplied by `disability_rate`)*  
- **Education Allowance**  
  *(Depends on `hr.employee`: `certificate`, multiplied by `female_rate`)*  
- **Children Allowance**  
  *(Multiplied by `hr.employee`: `children`)*  
- **Transport Allowance**  
  *(For each km, depends on `hr.work.location`: `work_location_id`, multiplied by `hr.employee`: `km_home_work`)*  
- **Housing Allowance**  

### Special Fields:
- `is_retirement_eligible`
- `grade_level`

### Final Wage Calculation:
*(Where `day_hours` is the hours per day in the employee's contract.)*
```python
final wage = (wage + allowances)  * (1 / day_ hours)(hours per day in employee contract)
```

### Relationships:
- **Many2one:** `pay_scale_id`
- **Many2many:** `tax_type_ids`

---

## Tree View

1. Create a view file for the menu item and define a new menu item (Grade).
2. Create another view file for different view types.
3. Call these files in `__manifest__.py`.
4. Build the tree view, showing allowance fields while keeping other fields optional.
5. Add `pay_scale_id` as an optional field.

---

## Form View

1. The **Grade number** will be the title.
2. **Day Hours** will be displayed under the title.
3. Other fields will be separated into **three pages**:
   - **Allowances**
   - **Rates**
   - **Special**
4. Add `pay_scale_id` field.
5. Add `max_salary` and `min_salary` from the `pay_scale` model.

---

## Search View

1. Add custom search for **grade number** and **grade level**:
   - If the user types a number → search for **grade number**.
   - If the user types a text → search for **grade level**.
2. Filtering by **Ability to retire** field.
3. Grouping by **grade level** field.

---

## Security

1. Create `ir.model.access.csv`.
2. Grant access to all users.
3. Call the file in `__manifest__.py`.

---

## Chatter Box

1. Add `'mail'` to the `depends` list in `__manifest__.py`.
2. Inherit `'mail.thread'` and `'mail.activity.mixin'` in the `hr_grade` model.
3. Add Chatter fields inside the form view.
4. Set `tracking=True` for all fields in `hr_grade` model.

---

## Constraints

1. **Grade number** must be an **integer greater than 0** *(Python)*.
2. **Grade number** must be **unique** *(SQL)*.
3. All **fields must be positive numbers** *(Python)*.
4. **Day hours** must be between **0 - 12** *(Python)*.
5. All **allowances must be required** *(Presentation)*.

---

## CRUD Methods

- **Create Method** (`@api.model` or `@api.model_create_multi`)  
  - **Attributes:** `vals`
- **Search Method** (`@api.model`)  
  - **Attributes:** `domain`, `offset`, `limit`, `order`, `access_rights_uid`
- **Write Method**  
  - **Attributes:** `vals`
- **Unlink Method**  
  - **Attributes:** `vals`

---

## hr_pay_scale Model

### Main Fields:
- **Name**
- **max_salary**
- **min_salary**

### Relationships:
- **One2Many:** `grade_ids`

### Views:
- **Tree View:** Displays all fields.
- **Form View:** Displays all fields with related grades.

---

## tax_type Model

### Main Field:
- **Name**

### Views:
- **Tree View:** Displays `name` field.
- **Form View:** Displays `name` field.

---

## hr_employee Inherited Model

### New Field:

```python
grade_id = fields.Many2one('hr.grade')
```
### Customizing the Form View:
- **Display Grade number**.  
- **Add a new page** (Salary Information).  
- **Add a new field** (Wage).  
