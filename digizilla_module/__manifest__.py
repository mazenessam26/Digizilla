{
    'name': 'Digizilla Module',
    'version': '17.0.1.0.0',
    'category': 'Custom',
    'summary': 'Manage Digizilla records with logging, tabs, and restricted form actions',
    'description': """
        Digizilla Module
        ================
        * Manage Digizilla records
        * Track field changes with chatter
        * Organized form view with tabs
        * Restricted form actions
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'views/digizilla_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla_module/static/src/js/hide_create_button.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}