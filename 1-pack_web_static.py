#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function
do_pack."""

from fabric.api import local
from os import path
from datetime import datetime


def do_pack():
    """_summary_

    Returns:
        _type_: _description_
    """
    local('mkdir -p versions')
    name = 'web_static_{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
    ruta = 'versions/{}'.format(name)
    local('tar czfv versions/{}.tgz web_static'.format(name))

    if path.isfile(ruta):
        return ruta
    else:
        return None
