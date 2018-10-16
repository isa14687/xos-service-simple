from synchronizers.new_base.SyncInstanceUsingAnsible import SyncStep
from synchronizers.new_base.modelaccessor import SimpleSubscriberService

from xosconfig import Config
from multistructlog import create_logger

log = create_logger(Config().get('logging'))

class SyncHelloWorldService(SyncStep):
    provides = [SimpleProviderService]

    observes = SimpleProviderService

    def sync_record(self, o):
        log.info("SimpleSubscriberService has been updated!", object=str(o), hello_from=o.subscriber_data)

    def delete_record(self, o):
        log.info("SimpleSubscriberService has been deleted!", object=str(o), hello_from=o.subscriber_data)
