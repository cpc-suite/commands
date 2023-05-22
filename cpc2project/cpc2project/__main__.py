import json
import subprocess
import click
import shutil
import os
import sys
from jinja2 import Template

@click.command()
@click.option('-c', '--cpc', required=True, type=click.Choice(['6128', '464', '664']), default='0', help='CPC Machines')
@click.option('-d', '--dsk', required=True, help='Name a DSK file')
@click.option('-r', '--run', required=True, help='Command to execute')

def main(cpc, dsk,run):
    context = {
        'cpc': cpc,
        'dsk': dsk,
        'run': run
    }

    CPCSUITE = os.environ.get('CPCSUITE')
    with open(CPCSUITE +"/src/cpc.j2", 'r') as file:
        template_string = file.read()
    template = Template(template_string)
    rendered_template = template.render(context)
    with open("cpc.htm", 'w') as file:
        file.write(rendered_template)

    print("--> Create Template HTML CPC Machine Retrovirtual Machine")
if __name__ == '__main__':
    main()
