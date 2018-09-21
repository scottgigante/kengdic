import kengdic


def test_kengdic():
    d = kengdic.Kengdic()
    result = d.search(english="do")
    assert len(result) == 3
    assert str(result[0]) == ('Korean: 매만져  가지런히하다\nEnglish: do\nSynonym: None'
                              '\nPart of Speech: 1.0 (1)\nSubmitted: engdic '
                              '(2006-01-16 00:52:46)')
    assert result[0].word_id == 53245
    assert result[0].word_id2 == 53245
    assert result[0].word_size == 29.0
    assert result[0].extra_data == 't'
    reverse_result = d.search(korean=result[0].korean)
    assert reverse_result[0] == result[0]
    assert len(d.search_glob(english="do?")) == len(
        d.search_regex(english="^do.$"))
    assert len(d.search_like(english="do_")) == len(
        d.search_regex(english="^[d|D][o|O].$"))
    assert len(d.search_regex(english=" do ")) == 108