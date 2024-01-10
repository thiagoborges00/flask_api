from mistune import markdown
from flask import Flask

def configure(app:Flask):
    '''configura e disponibiliza plugins para uso na aplicacao'''

    app.add_template_global(markdown)
    
    #formatando a data
    app.add_template_filter(lambda date: date.strftime('%d/%m/%Y'), 'format_date')

