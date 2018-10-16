from synchronizers.new_base.SyncInstanceUsingAnsible import SyncStep
from synchronizers.new_base.modelaccessor import IperfClientService

from xosconfig import Config
from multistructlog import create_logger

log = create_logger(Config().get('logging'))

class SyncHelloWorldService(SyncStep):
    provides = [IperfClientService]

    observes = IperfClientService

    def sync_record(self, o):
	pass
    def delete_record(self, o):
	pass
