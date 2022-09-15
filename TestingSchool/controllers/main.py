import base64

from odoo import http
from odoo.http import request


class Mit(http.Controller):
    # Student Page
    @http.route('/mit', website=True, auth='public')
    def mit_student(self):
        return request.render('TestingSchool.stu_data')

    # Demotest Student List
    @http.route(['/mitstulist'], type='http', auth='public', website=True)
    def demo_test(self, **kw):
        data = request.env['sch.record'].sudo().search([('x_status', '=', 1)])
        return http.request.render('TestingSchool.stu_list', {'res': data})

    @http.route(['/savestu'], type='http', auth='public', website=True, method=['POST'])
    def save_test(self, **post):
        id = post.get('id')
        student_name = post.get('student_name')
        birth_date = post.get('birth_date')
        age = post.get('age')
        notes = post.get('notes')
        email = post.get('email')
        mobile = post.get('mobile')
        gender = post.get('gender')
        books = post.get('books')
        image = post.get('image')
        fileData = image.read()
        image = base64.b64encode(fileData)
        attachment_name = post.get('attachment').filename
        attachment = post.get('attachment')
        attachfile = attachment.read()
        attachment = base64.b64encode(attachfile)

        demodata = http.request.env['sch.record']
        obj = {'student_name': student_name, 'birth_date': birth_date, 'age': age, 'x_status': 1, 'notes': notes,
               'email': email, 'mobile': mobile, 'gender': gender, 'books': books, 'image': image,
               'attachment_name': attachment_name, 'attachment': attachment}
        if id:
            demodata1 = demodata.sudo().search([('id', '=', id)])
            demodata1.sudo().write(obj)
        if not id:
            demodata.sudo().create(obj)

        data = request.env['sch.record'].sudo().search([('x_status', '=', 1)])
        return http.request.render('TestingSchool.stu_list', {'res': data})

    @http.route(['/readById'], type='http', auth='public', website=True)
    def read_by_id(self, **kw):
        id = kw.get('id')
        val = request.env['sch.record'].sudo().search([('id', '=', id)])
        return http.request.render('TestingSchool.stu_data', {'res': val})

    @http.route(['/deleteById'], type='http', auth='public', website=True)
    def deleteById(self, **kw):
        id = kw.get('id')
        demodata = request.env['sch.record'].sudo().search([('id', '=', id)])
        val = {'x_status': 4}
        val1 = demodata.sudo().write(val)
        data = request.env['sch.record'].sudo().search([('x_status', '=', 1)])
        return http.request.render('TestingSchool.stu_list', {'res': data})

    # Api testing
    # Sample Controller Created
    @http.route(['/getstudentlist'], type='json', auth='public')
    def get_studentlist(self):
        student_rec = request.env['sch.record'].sudo().search([])
        students = []
        for rec in student_rec:
            vals = {
                'id': rec.id,
                'name': rec.student_name,
                'gender': rec.gender,
                'notes': rec.notes,
                'email': rec.email,
                'mobile': rec.mobile,
            }
            students.append(vals)
        print("Student List    >", students)
        data = {'status': 200, 'response': students, 'message': 'Student List Success'}
        return data

    @http.route(['/createstudent'], type='json', auth='public')
    def create_student(self, **rec):
        if request.jsonrequest:
            print("rec", rec)
            if rec['name']:
                vals = {
                    'student_name': rec['name'],
                    'email': rec['email'],
                    'gender': rec['gender'],
                    'notes': rec['notes'],
                    'mobile': rec['mobile'],
                    'birth_date': rec['birth_date'],
                    'x_status': rec['x_status'],


                }
                new_student= request.env['sch.record'].sudo().create(vals)
                args = {'success': True, 'message': 'Success', 'ID': new_student.id}
        return args


    @http.route('/updatepatient', type='json', auth='public')
    def updatepatient(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                print("rec...", rec)
                student = request.env['sch.record'].sudo().search([('id', '=', rec['id'])])
                if student:
                    student.sudo().write(rec)
                args = {'success': True, 'message': 'student Updated'}
        return args

    @http.route('/deletepatient', type='json', auth='public')
    def deletepatient(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                print("rec...", rec)
                student = request.env['sch.record'].sudo().search([('id', '=', rec['id'])])
                if student:
                    student.sudo().write(rec)
                args = {'success': True, 'message': 'student Archived status change to  4'}
        return args
