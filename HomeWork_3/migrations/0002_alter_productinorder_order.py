from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_in_order', to='homework3.order'),
        ),
    ]