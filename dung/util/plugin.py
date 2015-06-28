from pkgutil import walk_packages

def find_modules_in(package):
    for (module_loader, name, ispkg) in walk_packages(path=package.__path__):
        if not ispkg:
            yield name

def entrypoints_for_plugins(look_in):
    return ["{plugin} = {into}.{plugin}".format(into=look_in.__name__, **locals()) for plugin in find_modules_in(look_in)]
