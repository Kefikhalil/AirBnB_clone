'''TestBaseModels module'''
import unittest
from models.base_model import BaseModel


class TestBaseModels(unittest.TestCase):
    '''
    Test BAse Models class
    '''
    def test_save(self):
        base1 = BaseModel()
        beforeCreatedAt = base1.created_at
        beforeUpdatedAt = base1.updated_at
        base1.save()
        afterCreatedAt = base1.created_at
        afterUpdatedAt = base1.updated_at
        self.assertEqual(beforeCreatedAt, afterCreatedAt)
        self.assertNotEqual(afterCreatedAt, afterUpdatedAt)
    pass
