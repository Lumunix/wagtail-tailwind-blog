# Generated by Django 4.1 on 2023-05-13 01:30

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('h1', wagtail.blocks.CharBlock()), ('h2', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('testimonials', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock())), ('image_text', wagtail.blocks.StructBlock([('reverse', wagtail.blocks.BooleanBlock(required=False)), ('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('image_carousel', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('thumbnail_gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='postpage',
            name='body',
            field=wagtail.fields.StreamField([('h1', wagtail.blocks.CharBlock()), ('h2', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('testimonials', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock())), ('image_text', wagtail.blocks.StructBlock([('reverse', wagtail.blocks.BooleanBlock(required=False)), ('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('image_carousel', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('thumbnail_gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], blank=True, use_json_field=True),
        ),
    ]
