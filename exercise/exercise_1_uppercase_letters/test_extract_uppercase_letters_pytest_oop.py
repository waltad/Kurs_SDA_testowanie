from exercise.exercise_1_uppercase_letters.extract_uppercase_letters import extract_uppercase_letters


class TestExtractUppercaseLetters:
    def test_no_uppercase_letters(self):
        sentence = 'ala ma kota'
        expected = ''

        actual = extract_uppercase_letters(sentence)

        assert actual == expected


    def test_empty_string(self):
        sentence = ''
        expected = ''

        actual = extract_uppercase_letters(sentence)

        assert actual == expected


    def test_sentence_with_uppercase_letters(self):
        sentence = 'Ala Ma Kota'
        expected = 'AMK'

        actual = extract_uppercase_letters(sentence)

        assert actual == expected