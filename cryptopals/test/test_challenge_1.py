from cryptopals.challenge_1 import hex_to_base64
from unittest import TestCase, main


class Tests(TestCase):
    def testHexConversion(self):
        rows = [
            ('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d', 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'),
            ('e983e546c8379cdad607dc713d60c1562ea680f7b35f0b131a38d43cd05cb6daaac3a8553770a0e026ed96fe0afa3b12', '6YPlRsg3nNrWB9xxPWDBVi6mgPezXwsTGjjUPNBcttqqw6hVN3Cg4Cbtlv4K+jsS'),
            ('1885ef65b963665b6c2a81e3bb2c02537e02f28e40a531979af603fc1abb837f539de5b7412733f8e01a8d5b79dfd8bf', 'GIXvZbljZltsKoHjuywCU34C8o5ApTGXmvYD/Bq7g39TneW3QScz+OAajVt539i/'),
            ('f77adf3ff079b2a00b1d914b7b1ffe6df42da6e21a7a28e5a6b85b33c418cdaad23791117518379d596d1198284458ff', '93rfP/B5sqALHZFLex/+bfQtpuIaeijlprhbM8QYzarSN5ERdRg3nVltEZgoRFj/'),
            ('2ad703d6d6fe3b766aae10f92fdd79c8553fa52515548ac9c32cbc5ba8566933c16848efde5232680b0626a15bc2eee1', 'KtcD1tb+O3ZqrhD5L915yFU/pSUVVIrJwyy8W6hWaTPBaEjv3lIyaAsGJqFbwu7h')
        ]

        for row in rows:
            base64_string = hex_to_base64(row[0])
            self.assertEqual(base64_string, row[1])


if __name__ == '__main__':
    main()
