# Generated by Django 4.1 on 2023-05-21 02:52

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_blogpage_body_alter_postpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('h1', wagtail.blocks.CharBlock()), ('h2', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('testimonials', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(required=False)), ('name', wagtail.blocks.RichTextBlock(required=False))]))), ('image_text', wagtail.blocks.StructBlock([('reverse', wagtail.blocks.BooleanBlock(required=False)), ('title', wagtail.blocks.RichTextBlock(required=False)), ('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('image_carousel', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('thumbnail_gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='postpage',
            name='body',
            field=wagtail.fields.StreamField([('h1', wagtail.blocks.CharBlock()), ('h2', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('testimonials', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(required=False)), ('name', wagtail.blocks.RichTextBlock(required=False))]))), ('image_text', wagtail.blocks.StructBlock([('reverse', wagtail.blocks.BooleanBlock(required=False)), ('title', wagtail.blocks.RichTextBlock(required=False)), ('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('image_carousel', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('thumbnail_gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], blank=True, use_json_field=True),
        ),
    ]
