from src.utils import mask_card_num, final_mask, mask_account_num, get_date, filter_and_sorted

def test_filter_and_sorted():
    new = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]
    assert filter_and_sorted(new) == new

def test_get_date():
        assert get_date('2019-01-05T00:52:30.108534') == '05.01.2019'
#
#
def test_mask_account_num():
    assert mask_account_num('12345678912345678912') == '****************8912'
    assert mask_account_num('Count12345678912345678912') == '****************8912'
    assert mask_account_num('-12345678912345678912') == '****************8912'

#
def test_mask_card_num():
    assert mask_card_num('123456789123') == ' ******6789****'
    assert mask_card_num('Visa123456789123') == 'Visa ******6789****'
    assert mask_card_num('Visa Classik123456789123') == 'VisaClassik ******6789****'
    assert mask_card_num('-V-isa Classik123456789123') == 'VisaClassik ******6789****'

#
def test_final_mask():
    assert final_mask('123456789123') == ' ******6789****'
assert final_mask('Счет12345678912345678912') == 'Счет ****************8912'