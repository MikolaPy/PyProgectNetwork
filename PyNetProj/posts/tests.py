from django.test import TestCase,Client 
from .models import Post , User

class ProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(
            username='Tailor',password='roll1243')
        self.post = Post.objects.create(text='Iam skyinet , machins wins , people lost',author=self.user)
    def test_profile(self):
        response = self.client.get("/butcher/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.context['posts'],1))
