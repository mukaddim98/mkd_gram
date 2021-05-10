from django.test import TestCase, Client
from shopify_images.models import Image


class ImageClassTest(TestCase):
    def setUp(self):
        Image.objects.create(file_name="abc", privacy="Private", image="image.png")

    def test_filename(self):
        abc = Image.objects.get(file_name="abc")
        self.assertEqual(abc.file_name, "abc")
        self.assertNotEqual(abc.file_name, "abd")

    def test_privacy(self):
        abc = Image.objects.get(file_name="abc")
        self.assertEqual(abc.privacy, "Private")
        self.assertNotEqual(abc.privacy, "Public")
        self.assertNotEqual(abc.privacy, "abc")

    def test_image(self):
        abc = Image.objects.get(file_name="abc")
        self.assertEqual(abc.image, "image.png")
        self.assertNotEqual(abc.image, "123.png")

    def test_fileupload(self):
        c = Client()
        with open('media/uploads/image.png') as fp:
            c.post('uploads/', {'file_name': 'fred', 'privacy': 'Public'})
        self.assertEqual(fp.name, "media/uploads/image.png")

