from synchronizers.new_base.SyncInstanceUsingAnsible import SyncStep
from synchronizers.new_base.modelaccessor import SimpleProviderService

from xosconfig import Config
from multistructlog import create_logger

log = create_logger(Config().get('logging'))

class SyncSimpleProviderService(SyncStep):
    provides = [SimpleProviderService]

    observes = SimpleProviderService

    def sync_record(self, o):
        log.info("SimpleProviderService has been updated!")

    def delete_record(self, o):
        log.info("SimpleProviderService has been deleted!")
