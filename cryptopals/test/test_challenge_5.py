import unittest

import cryptopals.challenge_5 as challenge


class Tests(unittest.TestCase):
    def test(self):
        message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        expected_output = ('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272'
                           'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
        actual_output = challenge.xor_with_repeating_key('ICE', message)

        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
