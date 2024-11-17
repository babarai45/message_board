from django.test import TestCase
from .models import post_model

# Create your tests here.

class posttest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post_model = post_model.objects.create(title='test', body='test body')

        def test_model_content(self):
            post = post_model.objects.get(id=1)
            expected_title = post.title
            expected_body = post.body
            self.assertEqual(expected_title, 'test')
            self.assertEqual(expected_body, 'test body')
