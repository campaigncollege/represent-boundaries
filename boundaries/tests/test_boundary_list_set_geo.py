# coding: utf-8
from __future__ import unicode_literals

from datetime import date

from django.contrib.gis.geos import GEOSGeometry

from boundaries.models import BoundarySet, Boundary
from boundaries.tests import ViewTestCase, ViewsTests, GeoListTests, GeoTests


class BoundaryListSetGeoTestCase(ViewTestCase, ViewsTests, GeoListTests, GeoTests):

    """
    Compare to BoundaryListGeoTestCase (/boundaries/shape)
    """

    maxDiff = None

    url = '/boundaries/inc/shape'
    json = {
        'objects': [
            {
                'name': '',
                'shape': {
                    'type': 'MultiPolygon',
                    'coordinates': [[[[0.0, 0.0], [0.0, 5.0], [5.0, 5.0], [0.0, 0.0]]]],
                },
            },
        ],
    }

    def setUp(self):
        BoundarySet.objects.create(slug='inc', last_updated=date(2000, 1, 1))

        geom = GEOSGeometry('MULTIPOLYGON(((0 0,0 5,5 5,0 0)))')
        Boundary.objects.create(slug='foo', set_id='inc', shape=geom, simple_shape=geom)
