{
    'name' : 'Special delivery',
    'version' : '1.0.0',
    'author' : 'Matiar Rahman',
    'category' : 'Sale',
    'website' : 'http://matiarrahman.com/',
    'description': """
Add field "Special delivery" to product and new condition at delivery grid definition. For example, "if Special Delivery > 0, delivery price is 0".

Currently, works only with sale order (not with picking)

Tested on Odoo 8.0 f8d5a6727d3e8d428d9bef93da7ba6b11f344284.
    """,
    'depends' : ['delivery'],
    'data':['views.xml'],
    'installable': True
}
