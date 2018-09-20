from synchronizers.new_base.SyncInstanceUsingAnsible import SyncStep
from synchronizers.new_base.modelaccessor import HelloWorldService

from xosconfig import Config
from multistructlog import create_logger

log = create_logger(Config().get('logging'))

class SyncHelloWorldService(SyncStep):
    provides = [HelloWorldService]

    observes = HelloWorldService

    def sync_record(self, o):
        log.info("HelloWorldService has been updated!", object=str(o), hello_from=o.hello_from)

    def delete_record(self, o):
        log.info("HelloWorldService has been deleted!", object=str(o), hello_from=o.hello_from)
