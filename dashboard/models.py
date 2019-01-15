from django.db import models

# Create your models here.
class MemberInfo(models.Model):
    age_member = (
        ('15','15'),('16','16'),('17','17'),
        ('20','20'),('21','21'),('22','22'),('23','23'),
        ('24','24'),('25','25'),('26','26'),('27','27'),
        ('28','28'),('29','29'),('30','30'),('31','31'),
        ('32','32'),('33','33'),('34','34'),('35','35'),
        ('36','36'),('37','37'),('38','38'),('39','39'),
        ('40','40'),('41','41'),('42','42'),('43','43'),
        ('44','44'),('45','45'),('46','46'),('47','47'),
        ('48','48'),('49','49'),('50','50'),('51','51'),
        ('52','52'),('53','53'),('54','54'),('55','55'),
        ('56','56'),('57','57'),('58','58'),('59','59'),
        ('60','60'),('61','61'),('62','62'),('63','63'),
        ('64','64'),('65','65'),('66','66'),('67','67'),
        ('68','68'),('69','69'),('70','70'),('71','71'),
        ('72','72'),('73','73'),('74','74'),('75','75'),
        ('76','76'),('77','77'),('78','78'),('79','79'),
        ('80','80'),('81','81'),('82','82'),('83','83'),
        ('84','84'),('85','85'),('86','86'),('87','87'),
        ('88','88'),('89','89'),('90','90'),('91','91'),
        ('92','92'),('93','93'),('94','94'),('95','95'),
        ('96','96'),('97','97'),('98','98'),('99','99'),('100','100')
    )
    # idadi_ya_mume = (
    #     ('one','one')
    # )
    married_choice = (
        ('Married','Married'),('Single','Single')
    )
    sex = (
        ('Male','Male'),('Female','Female')
    )
    mume = (
        ('0','0'),('1','1')
    )
    wake = (
        ('0','0'),('1','1'),('2','2'),('3','3'),('4','4')
    )
    year = (
        ('2018','2018'),('2019','2019'),('2020','2020'),('2021','2021'),('2022','2022'),
        ('2023','2023'),('2024','2024'),('2025','2025')
    )
    f_name = models.CharField(max_length = 50)
    m_name = models.CharField(max_length = 50)
    l_name = models.CharField(max_length = 50)
    image = models.ImageField()
    mwaka = models.CharField(max_length = 10, choices = year)
    age = models.CharField(max_length = 5, choices = age_member)
    address = models.CharField(max_length = 100)
    residence = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10, choices = sex)
    married = models.CharField(max_length = 10, choices = married_choice)
    mwanamke = models.CharField(max_length = 10, choices = wake)
    mwanaume = models.CharField(max_length = 10, choices = mume)
    phone_number = models.CharField(max_length = 20)
    member_id = models.CharField(max_length = 50)
    amount = models.PositiveIntegerField()
    class Meta:
        verbose_name_plural = "Members - Information"
    def __str__(self):
        return self.f_name + ' ' + self.l_name


class Dependant_info(models.Model):
    dependant_id = models.ForeignKey(MemberInfo, on_delete = models.CASCADE)
    wazazi = models.IntegerField()
    watoto_above = models.IntegerField()
    watoto_below = models.IntegerField()
    watoto_yatima = models.IntegerField()
    watoto_wakulea = models.IntegerField()
    class Meta:
        verbose_name_plural = "Dependant - Information"
    def __str__(self):
        return self.dependant_id.member_id
