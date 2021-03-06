# This file is part of Merlin/Arthur.
# Merlin/Arthur is the Copyright (C)2009,2010 of Elliot Rosemarine.

# Individual portions may be copyright by individual contributors, and
# are included in this collective work with permission of the copyright
# owners.

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
 
from django.conf.urls.defaults import include, patterns, url
from Arthur.rankings import planets, galaxies, alliances, ialliances

urlpatterns = patterns('Arthur.rankings',
    url(r'^planets/$', 'planets.planets', name="planet_ranks"),
    url(r'^planets/(?P<page>\d+)/$', 'planets.planets'),
    url(r'^planets/(?P<sort>\w+)/$', 'planets.planets'),
    url(r'^planets/(?P<sort>\w+)/(?P<page>\d+)/$', 'planets.planets'),
    url(r'^planets/(?P<race>\w+)/(?P<sort>\w+)/$', 'planets.planets'),
    url(r'^planets/(?P<race>\w+)/(?P<sort>\w+)/(?P<page>\d+)/$', 'planets.planets', name="planets"),
    url(r'^planet/(?P<x>\d+)[. :\-](?P<y>\d+)[. :\-](?P<z>\d+)/(?P<fleets>fleets/)?$', 'planet.planet', name="planet"),
    url(r'^galaxy/(?P<x>\d+)[. :\-](?P<y>\d+)/$', 'galaxy.galaxy', name="galaxy"),
    url(r'^galaxies/$', 'galaxies.galaxies', name="galaxy_ranks"),
    url(r'^galaxies/(?P<page>\d+)/$', 'galaxies.galaxies'),
    url(r'^galaxies/(?P<sort>\w+)/$', 'galaxies.galaxies'),
    url(r'^galaxies/(?P<sort>\w+)/(?P<page>\d+)/$', 'galaxies.galaxies', name="galaxies"),
    url(r'^alliance/(?P<name>[^/]+)/$', 'alliance.alliance', name="alliance_members"),
    url(r'^alliance/(?P<name>[^/]+)/history/$', 'ialliancehistory.ialliancehistory', name="alliance_history"),
    url(r'^alliance/(?P<name>[^/]+)/(?P<page>\d+)/$', 'alliance.alliance'),
    url(r'^alliance/(?P<name>[^/]+)/(?P<sort>\w+)/$', 'alliance.alliance'),
    url(r'^alliance/(?P<name>[^/]+)/(?P<sort>\w+)/(?P<page>\d+)/$', 'alliance.alliance'),
    url(r'^alliance/(?P<name>[^/]+)/(?P<race>\w+)/(?P<sort>\w+)/$', 'alliance.alliance'),
    url(r'^alliance/(?P<name>[^/]+)/(?P<race>\w+)/(?P<sort>\w+)/(?P<page>\d+)/$', 'alliance.alliance', name="alliance"),
    url(r'^alliances/$', 'alliances.alliances', name="alliance_ranks"),
    url(r'^alliances/(?P<page>\d+)/$', 'alliances.alliances'),
    url(r'^alliances/(?P<sort>\w+)/$', 'alliances.alliances'),
    url(r'^alliances/(?P<sort>\w+)/(?P<page>\d+)/$', 'alliances.alliances', name="alliances"),
    url(r'^ialliances/$', 'ialliances.ialliances'),
    url(r'^ialliances/(?P<page>\d+)/$', 'ialliances.ialliances'),
    url(r'^ialliances/(?P<sort>\w+)/$', 'ialliances.ialliances'),
    url(r'^ialliances/(?P<sort>\w+)/(?P<page>\d+)/$', 'ialliances.ialliances', name="ialliances"),
)
