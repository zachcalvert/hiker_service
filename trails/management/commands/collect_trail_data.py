import requests
from bs4 import BeautifulSoup
from decimal import Decimal

from django.core.management.base import BaseCommand

from trails.models import Trail

class Command(BaseCommand):
    """
    Retrieve trail data for NW Oregon / SW Washington
    """
    def handle(self, *args, **options):
        prefixes = (237, 257, 288)

        for prefix in prefixes:

            count = 1
            while count:
                url = 'http://www.trails.com/tcatalog_trail.aspx?trailid=HGW{0}-{1:03d}'.format(prefix, count)
                print('requesting: {}'.format(url))
                r = requests.get(url)
                soup = BeautifulSoup(r.text)

                for hit in soup.find_all('h1', class_='GlobalTitle'):
                    title = hit.contents[0].strip()

                if title == 'An unexpected error occured':
                    break

                trail, created = Trail.objects.get_or_create(name=title, url=url)

                table = soup.find(attrs={'id':'TrailInformationContainer'})
                rows = table.find('tbody').find_all('tr')
                d = {}
                i = 0
                for row in rows:
                    cells = row.find_all('td')
                    j = 0
                    for cell in cells:
                        d[i] = {}
                        text = cell.get_text()
                        if j == 0:
                            tmp = text
                        d[i][tmp] = text
                        j += 1
                    i += 1

                trail.city = d.get(2).get('Nearby City:')
                trail.distance = Decimal(d.get(3).get('Length:').strip('miles').replace('total',''))
                trail.elevation_gain = d.get(4).get('Elevation Gain:')
                trail.trail_type = d.get(5).get('Trail Type:')
                trail.difficulty = d.get(6).get('Skill Level:')
                trail.time_required = d.get(7).get('Duration:')
                if d.get(9).get('Top Elevation:'):
                    trail.peak_elevation = d.get(9).get('Top Elevation:')
                else:
                    trail.other = d.get(9).get('Other Uses:')
                try:
                    trail.save()
                    print('saved {0}'.format(trail.id))
                except Exception, e:
                    print('failed to save {0} due to {1}'.format(trail, e))
                    continue
                count += 1
