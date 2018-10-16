from synchronizers.new_base.SyncInstanceUsingAnsible import SyncStep
from synchronizers.new_base.modelaccessor import IperfServerService

from xosconfig import Config
from multistructlog import create_logger

log = create_logger(Config().get('logging'))

class SyncHelloWorldService(SyncStep):
    provides = [IperfServerService]

    observes = IperfServerService

    def sync_record(self, o):
	pass

    def delete_record(self, o):
	pass
