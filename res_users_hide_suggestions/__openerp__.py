{
    'name' : 'Hide suggestions',
    'version' : '1.0.0',
    'author' : 'Matiar Rahman',
    'category' : 'Sale',
    'website' : 'http://matiarrahman.com/',
    'description': """
Set False as default value for display_employees_suggestions and display_groups_suggestions.

Also, delete these ticks from all current users

Tested on Odoo 8.0 ab7b5d7732a7c222a0aea45bd173742acd47242d
    """,
    'depends' : ['hr', 'mail'],
    'data':[
        'pre_install.yml'
        ],
    'installable': True
}
