from django.db import models # type: ignore
from django.utils import timezone # type: ignore

# Create your models here.

class ScrapedData(models.Model):
    url = models.URLField(blank=True, null = True)
    data = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField( default=timezone.now)

















#html code for database
'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scraped Data</title>
</head>
<body>
    <h1>Scraped Data</h1>
    <table>
        <thead>
            <tr>
                <th>URL</th>
                <th>Data</th>
            </tr>
        </thead>
        <tbody>
            {% for item in data %}
            <tr>
                <td>{{ item.url }}</td>
                <td>{{ item.data }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
'''
