{
    'name' : 'is_employee field',
    'version' : '1.0.0',
    'author' : 'Matiar Rahman',
    'category' : 'Sale',
    'website' : 'http://matiarrahman.com/',
    'description': """
Adds is_employee to res.users and res.partner

Shows "Related employees" in res.users 

Shows "Related employee" in res.partner 

Tested on 8.0 ab7b5d7732a7c222a0aea45bd173742acd47242d
    """,
    'depends' : ['hr'],
    'data':['views.xml'],
    'installable': True
}
