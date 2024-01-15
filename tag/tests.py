from django.test import TestCase
from .models import Tag

class TagModelTest(TestCase):
    def setUp(self):
        # Create sample tags for testing
        Tag.objects.create(name='Tag1')
        Tag.objects.create(name='Tag2')

    def test_tag_name(self):
        tag1 = Tag.objects.get(name='Tag1')
        tag2 = Tag.objects.get(name='Tag2')
        self.assertEqual(str(tag1), 'Tag1')
        self.assertEqual(str(tag2), 'Tag2')

    def test_tag_count(self):
        tags_count = Tag.objects.count()
        self.assertEqual(tags_count, 2)