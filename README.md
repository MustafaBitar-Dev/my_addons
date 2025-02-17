*(Where `day_hours` is the hours per day in the employee's contract.)*

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
