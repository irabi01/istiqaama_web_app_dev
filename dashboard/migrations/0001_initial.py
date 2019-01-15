# Generated by Django 2.1 on 2018-12-14 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dependant_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wazazi', models.IntegerField()),
                ('watoto_above', models.IntegerField()),
                ('watoto_below', models.IntegerField()),
                ('watoto_yatima', models.IntegerField()),
                ('watoto_wakulea', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Dependant - Information',
            },
        ),
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('age', models.CharField(choices=[('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'), ('79', '79'), ('80', '80'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89'), ('90', '90'), ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'), ('97', '97'), ('98', '98'), ('99', '99'), ('100', '100')], max_length=5)),
                ('address', models.CharField(max_length=100)),
                ('residence', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('married', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], max_length=10)),
                ('mwanamke', models.CharField(max_length=10)),
                ('mwanaume', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('member_id', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Members - Information',
            },
        ),
        migrations.AddField(
            model_name='dependant_info',
            name='dependant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.MemberInfo'),
        ),
    ]
