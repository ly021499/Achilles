# @Time   : 2022/11/2 19:05
# @Author : LOUIE
# @Desc   : 随机数据生成类
from faker import Faker


fake = Faker()


def random_phone_number() -> str:
    """随机手机号"""
    return fake.phone_number()


def random_country() -> str:
    """随机国家"""
    return fake.country()


def random_city() -> str:
    """随机城市"""
    return fake.city()


def random_city_suffix() -> str:
    """随机县"""
    return fake.city_suffix()


def random_address() -> str:
    """随机地址"""
    return fake.address()


def random_street_address() -> str:
    """街道"""
    return fake.street_address()


def random_street_name() -> str:
    """街道名"""
    return fake.street_name()


def random_name() -> str:
    """随机姓名"""
    return fake.name()


def random_name_female() -> str:
    """女性姓名"""
    return fake.name_female()


def random_ean8():
    """8位条码"""
    return fake.ean8()


def random_ean13():
    """13位条码"""
    return fake.ean13()


def random_ean():
    """自定义位数条码,只能选8或者13"""
    return fake.ean(length=8)


def random_company() -> str:
    """公司名"""
    return fake.company()


def random_credit_card_number():
    """卡号"""
    return fake.credit_card_number(card_type=None)


def random_credit_card_full():
    """完整卡信息"""
    return fake.credit_card_full(card_type=None)


def random_date_time():
    """随机日期时间"""
    return fake.date_time(tzinfo=None)


def random_date_time_between():
    """两个时间间的一个随机时间"""
    return fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)


def random_day_of_month():
    """随机月中某一天"""
    return fake.day_of_month()


def random_unix_time() -> int:
    """随机unix时间（时间戳"""
    return fake.unix_time()


def random_date() -> str:
    """随机日期（可自定义格式"""
    return fake.date(pattern="%Y-%m-%d")


def random_job() -> str:
    """工作职位"""
    return fake.job()


def random_text() -> str:
    """随机生成一篇文章"""
    return fake.text(max_nb_chars=200)


def random_word() -> str:
    """随机单词"""
    return fake.word()


def random_sentence() -> str:
    """随机生成一个句子"""
    return fake.sentence(nb_words=6, variable_nb_words=True)


def random_paragraph() -> str:
    """随机生成一段文字(字符串)"""
    return fake.paragraph(nb_sentences=3, variable_nb_sentences=True)


def random_password() -> str:
    """随机密码（可指定密码策略)"""
    return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)


def random_uuid4() -> str:
    """随机uuid"""
    return fake.uuid4()


def random_pyint() -> int:
    """随机int"""
    return fake.pyint()


def random_pystr() -> str:
    """随机字符串（可指定长度）"""
    return fake.pystr(min_chars=None, max_chars=20)


def random_num(length=1) -> int:
    """随机数字"""
    return fake.random_number(length)


def random_email() -> str:
    """随机email"""
    return fake.email()


def random_ipv4() -> str:
    """随机IPV4地址"""
    return fake.ipv4()


if __name__ == '__main__':
    v = random_name()
    print(v)
    print(type(v))
