# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

{
    "name": "Point Of Sale Stock Information",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Point of Sale",
    "license": "OPL-1",
    "summary": "POS Stock Information,POS Inventory Information,Point Of Sale Inventory Information,POS On Hand Quantity,POS On-hand Quantity,POS On hand QTY, Point Of Sale On Hand Qty,Point Of Sale Forecasted Quantity,Forecasted qty,Virtual Quantity Odoo Display POS Stock Quantity Display POS Stock Quantity on POS Screen Stock in POS Inventory Management POS Product Qty POS Product Quantity POS Warehouse Quantity POS Inventory POS on Hand Quantity Stock Quantity Display Stock Quanity POS Available Quantity Show Product Quanity in POS Show Stock POS Display Point of Sale Stock Quantity on Point of Sale Screen Stock in Point of Sale Inventory Management Point of Sale Product Qty Point of Sale Product Quantity Point of Sale Warehouse Quantity Point of Sale Inventory Point of Sale on Hand Quantity Stock Quantity Display Stock Quanity Point of Sale Available Quantity Show Product Quanity in Point of Sale Show Stock Point of Sale Available Quantity Available Stock Available Item",
    "description": """Do you want to show the quantity of product stock in the POS products? This module allows you to displays product stock quantities at the point of sale. You can choose whether On-hand Quantity, Forecasted Quantity, or both will be displayed on the product screen. Stock information helps you to provide better customer services.""",
    "version": "0.0.1",
    "depends": ["point_of_sale"],
    "application": True,
    "data": [
        'views/res_config_settings.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'sh_pos_stock_information/static/src/overrides/**/*',
        ],
    },
    "images": ["static/description/background.png", ],
    "auto_install": False,
    "installable": True,
    "price": 15,
    "currency": "EUR"
}
