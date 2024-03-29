{
    'name' : 'Updated char_domain widget',
    'version' : '1.0.0',
    'author' : 'Matiar Rahman',
    'category' : 'Sale',
    'website' : 'http://matiarrahman.com/',
    'description': """
Shows domain value at char_domain widget, e.g.

    7 records selected -> Change selection : [('groups_id', '=', 3)]

Tested on Odoo 8.0 ab7b5d7732a7c222a0aea45bd173742acd47242d
    """,
    'depends' : ['web'],
    'data':[
        'views.xml',
        ],
    'qweb' : [
        "static/src/xml/*.xml",
    ],
    'installable': True
}
