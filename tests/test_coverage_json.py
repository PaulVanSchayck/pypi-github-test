import json
import unittest
from pathlib import Path

from covjson_pydantic.coverage_json import CoverageJson
from hamcrest import assert_that
from hamcrest import is_


class TestDomain(unittest.TestCase):
    def test_coverage_json(self):
        file = Path(__file__).parent.resolve() / "test_data" / "coverage-json.json"
        # Put JSON in default unindented format
        with open(file, "r") as f:
            data = json.load(f)
        json_string = json.dumps(data, separators=(",", ":"))

        # Round-trip
        assert_that(
            CoverageJson.parse_raw(json_string).json(exclude_none=True),
            is_(json_string),
        )
