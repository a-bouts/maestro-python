import compose
import logging

log = logging.getLogger(__name__)

def up(w, service):
    log.info('up ' + service['name'])
    project = compose.cli.command.get_project(w + '/services/' + service['name'])
    project.up(silent=True)

def down(w, service, include_volumes):
    log.info('down ' + service['name'])
    project = compose.cli.command.get_project(w + '/services/' + service['name'])
    project.down(remove_image_type=True, include_volumes=include_volumes)

def pull(w, service):
    log.info('pull ' + service['name'])
    project = compose.cli.command.get_project(w + '/services/' + service['name'])
    project.pull(silent=True)

def checkImage(w, service):
    project = compose.cli.command.get_project(w + '/services/' + service['name'])

    uptodate = True

    services = project.get_services()
    for s in services:
        containers = s.containers()
        if len(containers) > 0:
            c = s.containers()[0]

            if(s.image()['Id'] != c.image_config['Id']):
                log.info('New version available for service %s', service['name'])
                uptodate = False

    return not uptodate