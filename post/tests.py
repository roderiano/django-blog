from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Tag, Post
from django.utils import timezone

class PostModelTest(TestCase):
    def setUp(self):
        # Create a sample user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a sample tag for testing
        self.tag = Tag.objects.create(name='Test Tag')

        # Create a sample post for testing
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            pub_date=timezone.now(),
            tag=self.tag,
            author=self.user
        )

    def test_post_title(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_content(self):
        self.assertEqual(self.post.content, 'This is a test post content.')

    def test_post_pub_date(self):
        # Ensure pub_date is within a reasonable timeframe
        self.assertLess(self.post.pub_date, timezone.now())

    def test_post_tag(self):
        self.assertEqual(self.post.tag, self.tag)

    def test_post_author(self):
        self.assertEqual(self.post.author, self.user)

    def test_post_str_representation(self):
        expected_str = f'{self.post.title}'
        self.assertEqual(str(self.post), expected_str)