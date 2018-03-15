# Generated by Django 2.0.1 on 2018-03-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0014_auto_20180315_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon_id',
            field=models.CharField(choices=[('airplane', 'icon-airplane'), ('android', 'icon-android'), ('card', 'icon-card'), ('babymilk', 'icon-babymilk'), ('bag', 'icon-bag'), ('balloon', 'icon-balloon'), ('bandage', 'icon-bandage'), ('bikini', 'icon-bikini'), ('birthday-cake', 'icon-birthday-cake'), ('bread', 'icon-bread'), ('call', 'icon-call'), ('can-water', 'icon-can-water'), ('car', 'icon-car'), ('chair', 'icon-chair'), ('chart', 'icon-chart'), ('christmas', 'icon-christmas'), ('cocktail', 'icon-cocktail'), ('control-pad', 'icon-control-pad'), ('muffin', 'icon-muffin'), ('tool', 'icon-tool'), ('faucet', 'icon-faucet'), ('first-aid', 'icon-first-aid'), ('shoe', 'icon-shoe'), ('ice', 'icon-ice'), ('pool', 'icon-pool'), ('light-bulb', 'icon-light-bulb'), ('mask', 'icon-mask'), ('mobile', 'icon-mobile'), ('music', 'icon-music'), ('piggy-bank', 'icon-piggy-bank'), ('pizza', 'icon-pizza'), ('sewing-machine', 'icon-sewing-machine'), ('sign-board', 'icon-sign-board'), ('smartphone', 'icon-smartphone'), ('sock', 'icon-sock'), ('spoon-fork', 'icon-spoon-fork'), ('store', 'icon-store'), ('transport', 'icon-transport'), ('tooth', 'icon-tooth'), ('train', 'icon-train'), ('cart', 'icon-cart'), ('repair', 'icon-repair'), ('default', 'icon-simple-budget')], default='icon-simple-budget', max_length=30),
        ),
    ]
