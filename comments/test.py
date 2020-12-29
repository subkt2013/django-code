from django.test import TestCase
from django.urls import reverse
 
# Create your tests here.
 
class CommentIndexTests(TestCase):
    def test_comment_index(self):
        """
        Comment index のテスト
        """
        response = self.client.get(reverse('comments:index'))
        self.assertEqual(response.status_code, 200)
