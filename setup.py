#!/usr/bin/env python3
import logging
import os

import setuptools

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

# Package meta-data.
NAME = "covjson-pydantic"

# TODO: See what we need to do about branches
env_suffix = os.environ.get("ENVIRONMENT_SUFFIX", "")
logger.debug(f"Environment suffix: {env_suffix}")

if env_suffix:
    NAME += f"-{env_suffix}"
logger.debug(f"Package name: {NAME}")


if __name__ == "__main__":
    setuptools.setup()
