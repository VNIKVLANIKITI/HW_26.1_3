from rest_framework.test import APITestCase
from rest_framework import status


class lessonTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        """ Тест создания урока """
        data = {
            "name": "Тестовый урок",
            "description": "тестовое описание урока https://www.youtube.com/watch?v=1qMB4YeKuuU",
        }
        response = self.client.post(
            '/lesson/create',
            data=data,
            )
        
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        
        self.assertEqual(
            response.json(),
                {
                   "name": "Тестовый урок",
                    "description": "тестовое описание урока https://www.youtube.com/watch?v=1qMB4YeKuuU"
                }
        )
