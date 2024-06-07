from odoo import models, fields, api

class LibraryDoc(models.Model):
    _name = 'library.doc'
    _description = 'Library Document'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    company_id = fields.Char('Company')
    create_uid = fields.Char('Created By')
    assigned_emp_ids = fields.Many2many('hr.employee', 'library_doc_employee_rel', 'doc_id', 'emp_id', 'Assigned Employees')