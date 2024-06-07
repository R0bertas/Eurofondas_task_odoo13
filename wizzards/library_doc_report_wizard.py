from odoo import models, fields

class LibraryDocReportWizard(models.TransientModel):
    _name = 'library.doc.report.wizard'
    _description = 'Library Document Report Wizard'

    date_from = fields.Date('Date From')
    date_to = fields.Date('Date To')
    employee_id = fields.Many2one('hr.employee', 'Employee')

    def action_print_report(self):
        docs = self.env['library.doc'].search([
            ('create_date', '>=', self.date_from),
            ('create_date', '<=', self.date_to),
            '|',
            ('assigned_emp_ids', '=', self.employee_id.id),
            ('assigned_emp_ids', '=', False)
        ])
        # Čia galite atspausdinti arba sukurti ataskaitą pagal `docs` rezultatus
        print(docs)