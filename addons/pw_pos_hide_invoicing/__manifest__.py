# -*- coding: utf-8 -*-
{
    'name': 'POS Hide Invoice | POS Restrict Invoice',
    'version': '1.0',
    'author': 'Preway IT Solutions',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'summary': 'This apps helps you to hide invoice button on pos screen for specific shops | POS Hide Invoice Button',
    'description': """
- POS Hide Invoice
    """,
    'data': [
        'views/pos_config_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pw_pos_hide_invoicing/static/src/xml/payment_screen.xml',
        ],
    },
    'price': 5.0,
    'currency': "EUR",
    'application': True,
    'installable': True,
    "license": "LGPL-3",
    "images":["static/description/Banner.png"],
}
