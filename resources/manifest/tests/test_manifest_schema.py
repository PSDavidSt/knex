import os
import unittest

from jsonschema import ValidationError

from resources.manifest.validator.manifest_validator import ManifestValidator

DIR = os.path.dirname(os.path.abspath(__file__))
JSON_DIR = os.path.abspath(os.path.join(DIR, os.pardir))


class TestManifestSchema(unittest.TestCase):
    def setUp(self):
        path = os.path.join(JSON_DIR, "schema/manifest_schema.json")
        with open(path) as schema:
            self.validator = ManifestValidator(schema)

    def test_schema_ok(self):
        with open(os.path.join(os.path.dirname(__file__), "manifest.json5")) as manifest:
            self.assertEqual(None, self.validator.validate_manifest(manifest))

    def test_schema2_ok(self):
        with open(os.path.join(os.path.dirname(__file__), "json1.json5")) as manifest:
            self.assertEqual(None, self.validator.validate_manifest(manifest))

    def test_schema_empty(self):
        with open(os.path.join(os.path.dirname(__file__), "manifest2.json5")) as manifest:
            self.assertRaises(ValidationError, self.validator.validate_manifest(manifest))

    def test_schema_invalidDate(self):
        with open(os.path.join(os.path.dirname(__file__), "manifest3.json5")) as manifest:
            self.assertRaises(ValidationError, self.validator.validate_manifest(manifest))

    def test_schema_invalidURL(self):
        with open(os.path.join(os.path.dirname(__file__), "manifest4.json5")) as manifest:
            self.assertRaises(ValidationError, self.validator.validate_manifest(manifest))

    def test_schema_invalidEmail(self):
        with open(os.path.join(os.path.dirname(__file__), "manifest5.json5")) as manifest:
            self.assertRaises(ValidationError, self.validator.validate_manifest(manifest))

    def test_schema_invalidJSON(self):
        with open(os.path.join(os.path.dirname(__file__),"manifest6.json5")) as manifest:
            self.assertRaises(ValidationError, self.validator.validate_manifest(manifest))



if __name__ == '__main__':
    unittest.main()
