#!/usr/bin/env python3
#  Copyright 2022 VMware, Inc.
#  SPDX-License-Identifier: Apache-2.0
import os

import connexion
from swagger_server import server_logging
from swagger_server.encoder import JSONProvider


def main() -> None:
    server_logging.setup_logging("server.log")
    logger = server_logging.getLogger("main")

    app = connexion.FlaskApp(__name__, specification_dir="swagger/")
    app.app.json_provider_class = JSONProvider
    app.app.json = JSONProvider(app.app)
    app.add_api(
        "swagger.yaml",
        arguments={"title": "Adapter API"},
        pythonic_params=True,
    )

    ssl_cert = "/etc/ssl/certs/dockerized.crt"
    ssl_key = "/etc/ssl/certs/dockerized.key"
    port = 8080
    ssl_args = {}
    if os.path.exists(ssl_cert) and os.path.exists(ssl_key):
        port = 443
        ssl_args = {"ssl_certfile": ssl_cert, "ssl_keyfile": ssl_key}

    logger.info(f"Port: {port}")
    app.run(host="0.0.0.0", port=port, **ssl_args)


if __name__ == "__main__":
    main()
