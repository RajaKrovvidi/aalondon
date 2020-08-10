from django.test import TestCase

class TestURLSuccess(TestCase):
    """
    Just test that each api endpoint returns 200
    """
    def test_visit_api_root(self):
        expected_content = b'{"meetings":"http://testserver/api/meetings/"}'
        response = self.client.get('/api/')
        response.render()
        assert response.status_code == 200
        assert response.content == expected_content

    def test_visit_meetings(self):
        expected_content = b'{"count":0,"next":null,"previous":null,"results":[]}'
        response = self.client.get('/api/meetings/')
        response.render()
        assert response.status_code == 200
        assert response.content == expected_content

    def test_visit_meetingsearch(self):
        expected_content = b'{"count":0,"next":null,"previous":null,"results":[]}'
        response = self.client.get('/api/meetingsearch/')
        response.render()
        assert response.status_code == 200
        assert response.content == expected_content

    def test_visit_onlinemeetingsearch(self):
        expected_content = b'{"count":0,"next":null,"previous":null,"results":[]}'
        response = self.client.get('/api/onlinemeetingsearch/')
        response.render()
        assert response.status_code == 200
        assert response.content == expected_content
