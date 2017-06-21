import codecs

import pkg_resources

import cryptopals.challenge_1 as challenge_1
import cryptopals.challenge_2 as challenge_2
import cryptopals.challenge_3 as challenge_3
import cryptopals.challenge_4 as challenge_4
import cryptopals.challenge_5 as challenge_5


def test_challenge_1():
    message = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    actual_output = challenge_1.base64_from_hex(message)

    assert expected_output == actual_output


def test_challenge_2():
    key = '686974207468652062756c6c277320657965'
    encrypted_message = '1c0111001f010100061a024b53535009181c'
    expected_output = '746865206b696420646f6e277420706c6179'
    actual_output = challenge_2.decrypt_xor_encrypted_message(key, encrypted_message)

    assert expected_output == actual_output


def test_challenge_3():
    encrypted_message = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    expected_output = "Cooking MC's like a pound of bacon"
    actual_output = challenge_3.decrypt_xor_encrypted_message(encrypted_message)

    assert expected_output == actual_output


def test_challenge_4():
    encrypted_messages = pkg_resources.resource_string('cryptopals.resources', '4.txt')
    encrypted_messages = codecs.decode(encrypted_messages, 'utf').split('\n')
    expected_output = 'Now that the party is jumping'
    actual_output = challenge_4.find_xor_encrypted_message(encrypted_messages)

    assert expected_output == actual_output


def test_challenge_5():
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    expected_output = ('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272'
                       'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
    actual_output = challenge_5.xor_with_repeating_key('ICE', message)

    assert expected_output == actual_output
