#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function
do_deploy:"""

from fabric.api import local, settings, abort, run, cd, env, put, get
from fabric.decorators import task, hosts, with_settings
from os import path
from datetime import datetime

env.hosts = ["54.226.167.87", "34.148.202.126"]
env.user = "ubuntu"


def do_pack():
    """_summary_

    Returns:
        _type_: _description_
    """
    local("mkdir -p versions")
    name = "web_static_{}".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    ruta = "versions/{}".format(name)
    local("tar czfv versions/{}.tgz web_static".format(name))

    if path.isfile(ruta):
        return ruta
    else:
        return None


def do_deploy(archive_path):
    """_summary_

    Args:
        archive_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    if path.isfile(archive_path):
        name_file = archive_path[9:]
        new_path = "/data/web_static/releases/"
        path_server_file = "/tmp/{}".format(name_file)
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_path))
        run("sudo tar -xzf {} -C {}/".format(path_server_file, new_path))
        run("sudo rm {}".format(path_server_file))
        run("sudo rm -rf {}".format("/data/web_static/current"))
        run(
            "sudo ln -s {} /data/web_static/current".format(
                "/data/web_static/releases/web_static"
            )
        )
        print("New version deployed!")
        return True

    return False
