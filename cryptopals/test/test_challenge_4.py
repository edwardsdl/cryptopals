import codecs
import unittest

import pkg_resources

import cryptopals.challenge_4 as challenge


class Tests(unittest.TestCase):
    def test(self):
        encrypted_messages = pkg_resources.resource_string('cryptopals.resources', '4.txt')
        encrypted_messages = codecs.decode(encrypted_messages, 'utf').split('\n')
        expected_output = 'Now that the party is jumping'
        actual_output = challenge.find_xor_encrypted_message(encrypted_messages)

        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
