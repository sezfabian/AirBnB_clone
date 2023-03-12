import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_class_instance(self):
        self.assertIsInstance(storage, FileStorage)

    def test_has_attributes(self):
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_save_and_reload(self):
        model = BaseModel()
        model.full_name = "TestModel"
        model.save()

        # Verify the model is saved
        self.assertTrue(os.path.exists(self.file_path))

        # Verify the model can be reloaded
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertTrue(key in all_objs)

        # Verify the reloaded model has the correct attributes
        reloaded_model = all_objs[key]
        self.assertEqual(model.full_name, reloaded_model.full_name)

    def test_save_update_and_reload(self):
        model = BaseModel()
        model.name = "First name"
        model.save()

        # Verify the model is saved
        self.assertTrue(os.path.exists(self.file_path))

        # Verify the model can be reloaded
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertTrue(key in all_objs)

        # Verify the model can be updated and reloaded
        model.name = "Second name"
        model.save()
        storage.reload()
        all_objs = storage.all()
        reloaded_model = all_objs[key]
        self.assertEqual(model.name, reloaded_model.name)

    def test_save_self(self):
        with self.assertRaises(TypeError):
            FileStorage.save(self, 100)

    def test_new_method(self):
        model = BaseModel()
        model.save()
        storage.save()
        with open(self.file_path) as f:
            obj_dict = json.load(f)

        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertTrue(key in obj_dict)

    def test_reload_no_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        storage.reload()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)

    def test_reload_empty_file(self):
        with open(self.file_path, 'w') as f:
            f.write("")

        storage.reload()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 0)


if __name__ == '__main__':
    unittest.main()
