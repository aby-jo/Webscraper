from webscraper import check_url,connect,write_to_file
import pytest,os
def test_check_url():
    with pytest.raises(SystemExit):
        assert(check_url("cat"))
def test_connect():
    with pytest.raises(SystemExit):
        assert(connect("https://goooogle/.com"))
def test_write_to_file(monkeypatch):
    if os.path.exists("scraper_data.txt"):
        monkeypatch.setattr("builtins.input",lambda _:"cat")
        with pytest.raises(SystemExit):
            assert write_to_file("hello")
        