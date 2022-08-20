{
    'name': 'Employee Portal',
    'version': '15.0.1.0.0',
    'author': 'Gokul Prasath',
    'website': 'http://www.appcomp.com',
    'category': 'Employe',
    'complexity': 'easy',
    'Summary': 'A Module For Employee Management',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/menu.xml',
        'views/template.xml',
        'views/descripition_tem.xml',
        'views/snippets.xml',
        'views/weather.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'employes/static/src/add.js',
            'employes/static/src/Weather.js',
            'employes/static/src/student.js',
            'employes/static/src/scss/add.scss',

        ],
    },
    'demo': [],
    'installable': True,
    'application': True
}
