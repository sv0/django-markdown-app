from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_markdown.models.MarkdownField()),
                ('description', django_markdown.models.MarkdownField()),
            ],
        ),
    ]
