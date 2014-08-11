#!/usr/bin/env python
# vi: set ft=python ts=4 sta et sts=4 sw=4 si ai tw=79:

from app import app
import redis
import os
import unittest
import json

class CloudTestCase(unittest.TestCase):
    
    def setUp(self):
        app.redis.rpush('clouds', 'Altoc')
        app.redis.rpush('clouds', 'Altos')
        app.redis.rpush('clouds', 'Cumul')
        app.redis.rpush('clouds', 'Nimbo')

    def tearDown(self):
        app.redis.flushdb()

    def test_clouds(self):
        tester = app.test_client(self)

        response = tester.get('/clouds.json', content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, json.dumps(['Altoc', 'Altos', 'Cumul',
            'Nimbo']))

if __name__ == '__main__':
    unittest.main()
