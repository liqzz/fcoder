from unittest import TestCase
import os
from fcoder import CoderClient
from dotenv import load_dotenv

load_dotenv()

class TestCoderClient(TestCase):
    def test_code_interpreter(self):
        client = CoderClient(
            server_host=os.environ["CODER_SERVER_HOST"],
            server_port=int(os.environ["CODER_SERVER_PORT"]),
            auth_token=os.environ["AUTH_TOKEN"]
        )
        result = client.code_interpreter("print('hello')")
        self.assertIn(
            {'text/plain': 'hello\n'},
            result.output
        )

