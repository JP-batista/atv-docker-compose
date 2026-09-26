from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Arquivo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=200)),
                ("arquivo", models.FileField(upload_to="uploads/%Y/%m/%d/")),
                ("enviado_em", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-enviado_em"],
            },
        ),
    ]
