import django
from django.conf import settings
from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from django.urls import get_resolver, reverse
from django_extensions.management.commands.show_urls import Command

from zds.member.tests.factories import ProfileFactory


class ForumMemberTests(TestCase):
    def setUp(self):
        self.user = ProfileFactory().user
        self.client.force_login(self.user)

        self.patterns = Command().extract_views_from_urlpatterns(get_resolver().url_patterns)

    def test_forum_urls(self):
        for _, url_pattern, url_name in self.patterns:
            if not url_name or not "forum:" in url_name:
                continue

            with self.subTest(url=url_pattern):
                try:
                    with CaptureQueriesContext(connection) as ctx:
                        self.client.get(reverse(url_name))
                    query_count = len(ctx.captured_queries)
                    print(url_pattern, url_name, query_count)
                except django.template.exceptions.TemplateSyntaxError:
                    continue
                except django.urls.exceptions.NoReverseMatch:
                    continue
                except Exception as erreur:
                    print(type(erreur), erreur)
