# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from django.utils.translation import get_language
from cms.models import Title

class CMSSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        titles = Title.objects.public().filter(page__login_required=False, \
                    language=get_language())
        return titles

    def lastmod(self, title):
        return title.page.publication_date or title.page.creation_date

    def location(self, title):
        return title.page.get_absolute_url()
