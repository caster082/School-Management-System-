from odoo import models


# Creating Excel Report
class StudentCardXLS(models.AbstractModel):
    _name = 'report.testingschool.student_data_pdf_template_excel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter', })
        sheet = workbook.add_worksheet('Students Card')
        sheet.write(0, 0, 'Name', format1)#student_name
        sheet.write(0, 1, 'Age', format1)#age
        sheet.write(0, 2, 'Gender', format1)#gender
        sheet.write(0, 3, 'Notes', format1)#notes
        sheet.write(0, 4, 'Email', format1)#email
        sheet.write(0, 5, 'Mobile', format1)#mobile
        # sheet.write(0, 6, 'Responsible', format1)  # responsible_id
        sheet.write(0, 7, 'Status', format1)  # state
        row = 1
        for line in lines:
            sheet.write(row, 0, line.student_name)
            sheet.write(row, 1, line.age)
            sheet.write(row, 2, line.gender)
            sheet.write(row, 3, line.notes)
            sheet.write(row, 4, line.email)
            sheet.write(row, 5, line.mobile)
            # sheet.write(row, 6, line.responsible_id)
            sheet.write(row, 7, line.state)


