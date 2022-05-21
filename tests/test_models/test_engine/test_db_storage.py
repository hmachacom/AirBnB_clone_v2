#!/usr/bin/python3
# """ Module for testing file storage"""
import unittest
import pep8
from models.base_model import BaseModel
from models import storage
import os
from models.engine.db_storage import DBStorage
db_storage = DBStorage()
class TestDBStorageDocs(unittest.TestCase):
		""" Class to test the documentation """
		def test_doc_module(self):
			""" Module documentation """
			self.assertTrue(len(storage.__doc__) > 0)
		def test_doc_class(self):
			""" Class documentation """
			self.assertTrue(len(BaseModel.__doc__) > 0)
		def test_doc_method(self):
			""" Method documentation """
			self.assertTrue(len(BaseModel.__init__.__doc__) > 0)
		def test_doc_method(self):
			""" Method documentation """
			self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
		def test_doc_method(self):
			""" Method documentation """
			self.assertTrue(len(BaseModel.save.__doc__) > 0)
		def test_doc_method(self):
			""" Method documentation """
			self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)
		def test_doc_method(self):
			""" Method documentation """
			self.assertTrue(len(BaseModel.from_json.__doc__) > 0)
		def test_doc_method(self):
			""" Method documentation """
			self.assertTrue(len(BaseModel.__class__.__doc__) > 0)
		def test_doc_method(self):
			""" Method documentation """
			self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
		def test_doc_method(self):
			""" Method documentation """
			self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
		def test_doc_method(self):
			""" Method documentation """
			self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
		def test_pep8_conformance_db_storage(self):
			""" Test that we conform to PEP8 """
			pep8_check = pep8.check_files(['models/engine/db_storage.py'])
			self.assertEqual(pep8_check.total_errors, 0,
							"Found code style errors (and warnings).")
		def test_pep8_conformance_test_db_storage(self):
			""" Test that we conform to PEP8 """
			pep8_check = pep8.check_files(['tests/test_models/test_engine/test_db_storage.py'])
			self.assertEqual(pep8_check.total_errors, 0,
							"Found code style errors (and warnings).")
		def test_db_storage_module_docstring(self):
			""" Test for the db_storage.py module docstring """
			self.assertIsNot(db_storage.__doc__, None)
		def test_db_storage_class_docstring(self):
			""" Test for the BaseModel class docstring """
			self.assertIsNot(BaseModel.__doc__, None)
		def test_dbs_func_docstrings(self):
			""" Test for the presence of docstrings in db_storage methods """
			for func in dir(db_storage):
				self.assertIsNot(func.__doc__, None)


