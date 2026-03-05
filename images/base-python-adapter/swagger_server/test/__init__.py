#  Copyright 2022 VMware, Inc.
#  SPDX-License-Identifier: Apache-2.0
import logging

import connexion
from flask_testing import TestCase
from swagger_server.encoder import JSONProvider


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.FlaskApp(__name__, specification_dir="../swagger/")
        app.app.json_provider_class = JSONProvider
        app.app.json = JSONProvider(app.app)
        app.add_api("swagger.yaml")
        return app.app
