# -*- coding: utf-8 -*-
{
    'name': 'POS Invoice Auto Check | POS Default Invoicing',
    'version': '1.0',
    'author': 'Preway IT Solutions',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'summary': 'This apps helps you select invoice button automatically on every order on pos payment screen | POS Auto Invoice',
    'description': """
- POS Default invoice button is selected
- POS Auto invoicing
- POS Invoice automatically 
    """,
    'data': [
        'views/pos_config_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pw_pos_auto_invoicing/static/src/js/payment_screen.js',
        ],
    },
    'price': 8.0,
    'currency': "EUR",
    'application': True,
    'installable': True,
    "license": "LGPL-3",
    "images":["static/description/Banner.png"],
}
