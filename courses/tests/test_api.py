from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from courses.models import Course, Lesson


class CourseAndMaterialAPITests(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(
            username='teacher1',
            password='password123',
            role=User.Role.TEACHER
        )
        self.client.force_authenticate(user=self.teacher)

    def test_create_course_and_lesson_with_file(self):
        course_data = {
            'title': 'Python Advanced',
            'description': 'Deep dive into Django and DRF'
        }
        response = self.client.post('/api/courses/', course_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        course_id = response.data['id']

        test_file = SimpleUploadedFile(
            name='material.pdf',
            content=b'%PDF-1.4 test material content',
            content_type='application/pdf'
        )

        lesson_data = {
            'course': course_id,
            'title': 'DRF File Upload',
            'content': 'Learn how to upload files securely.',
            'material_file': test_file
        }
        
        response_lesson = self.client.post('/api/lessons/', lesson_data, format='multipart')
        
        self.assertEqual(response_lesson.status_code, status.HTTP_201_CREATED)
        self.assertIn('material_file', response_lesson.data)

    def test_get_courses_list(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)