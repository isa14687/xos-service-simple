# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import jinja2
import json
from synchronizers.new_base.modelaccessor import *
from synchronizers.new_base.policy import Policy

from xosconfig import Config
from multistructlog import create_logger

log = create_logger(Config().get('logging'))

class SimpleSubscriberServiceInstancePolicy(Policy):
    model_name = "SimpleSubscriberServiceInstance"

    def handle_create(self, service_instance):
        log.info("handle_create SimpleSubscriberServiceInstance", object=str(service_instance))
	return self.handle_update(service_instance)

    def handle_update(self, service_instance):
	log.info("handle_update SimpleSubscriberServiceInstance", object=str(service_instance))
        compute_service = KubernetesService.objects.first()
        compute_service_instance_class = Service.objects.get(id=compute_service.id).get_service_instance_class()
        slice = Slice.objects.filter(name="myslice")[0]
        image = Image.objects.filter(name="nginx")[0]
        name="simplesubscriberserviceinstance-%s" % service_instance.id
        instance = compute_service_instance_class(slice=slice, owner=compute_service, image=image, name=name, no_sync=False)
        instance.save()


    def handle_delete(self, service_instance):
        log.info("handle_delete SimpleSubscriberServiceInstance", object=str(service_instance))
	compute_service = KubernetesService.objects.first()
        compute_service_instance_class = Service.objects.get(id=compute_service.id).get_service_instance_class()
	name = "simplesubscriberserviceinstance-%s" % service_instance.id
	compute_service_instance_class.objects.get(name=name).delete()
