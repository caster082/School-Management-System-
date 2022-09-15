{
    'name': 'School Management System',
    'version': '1.0',
    'summary': 'School Management System',
    'sequence': -100,
    'description': """School Management System""",
    'category': 'Tutorials',
    'author': 'Casta',
    'maintainer': 'Casta',
    'website': 'https://www.google.com',
    'license': 'AGPL-3',
    'depends': ['base', 'web', 'mail', 'report_xlsx', 'contacts', 'fleet', 'sale', 'board', ],
    'css': ['static/src/css/student.css'],
    'js': ['static/src/js/stu.js'],


    'data': [
        # 'reports/report.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'reports/student_detail.xml',
        'reports/sale_report_inherit.xml',
        'views/student_website.xml',
        'views/studentlist_website.xml',
        'views/student.xml',
        'views/book.xml',
        'views/sale.xml',
        'views/teacher.xml',
        'views/dashboard.xml',


    ],
    'images': ['static/description/banner.png'],

    'installable': True,
    'license': 'LGPL-3',
}
