#  Copyright 2022 VMware, Inc.
#  SPDX-License-Identifier: Apache-2.0
from flask.json.provider import DefaultJSONProvider
from swagger_server.models.base_model_ import Model


class JSONProvider(DefaultJSONProvider):
    def default(self, o):
        if isinstance(o, Model):
            return {
                o.attribute_map[attr]: getattr(o, attr)
                for attr in o.swagger_types
                if getattr(o, attr) is not None
            }
        return super().default(o)
