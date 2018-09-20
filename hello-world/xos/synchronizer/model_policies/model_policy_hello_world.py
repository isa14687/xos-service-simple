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

class SimpleExampleServiceInstancePolicy(Policy):
    model_name = "HelloWorldServiceInstance"

    def handle_create(self, service_instance):
        log.info("handle_create HelloWorldServiceInstance", object=str(service_instance))
        # TODO: Break dependency
        compute_service = KubernetesService.objects.first()
        compute_service_instance_class = Service.objects.get(id=compute_service.id).get_service_instance_class()

        exampleservice = service_instance.owner.leaf_model

        # TODO: What if there is the wrong number of slices?
#        slice = Slice.objects.filter(name="myslice")[0]
        slice = exampleservice.slices.first()
	log.info("handle_update slice", object=str(slice))

        # Tlice = exampleservice.slices.first()
        image = slice.default_image

        name="simpleexampleserviceinstance-%s" % service_instance.id
#	compute_service_instance = KubernetesServiceInstance.objects.new()
#        compute_service_instance.slice = slice
#        compute_service_instance.owner = compute_service
#        compute_service_instance.image = image
#        compute_service_instance.name = name
#	compute_service_instance.no_sync = True
        compute_service_instance = compute_service_instance_class(slice=slice, owner=compute_service, image=image, name=name, no_sync=False, xos_managed=True)
        compute_service_instance.save()


    def handle_update(self, service_instance):
	log.info("handle_update HelloWorldServiceInstance", object=str(service_instance))

    def handle_delete(self, service_instance):
        log.info("handle_delete HelloWorldService", object=str(service_instance))
