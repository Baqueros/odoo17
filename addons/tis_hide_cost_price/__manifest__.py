# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd. - ©
# Technaureus Info Solutions Pvt. Ltd 2023. All rights reserved.

{
    'name': 'Hide Cost Price From User',
    'version': '17.0.0.0',
    'summary': 'Hiding cost price from sale user group',
    'sequence': 1,
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'description': 'Hiding cost price from sale user group',
    'category': 'sales',
    'website': 'http://www.technaureus.com',
    'price': 4.99,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'depends': [
        'sales_team', 'stock_account',
    ],
    'data': [
        'views/product_template_custom_form.xml'
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
