# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# Author: Kiall Mac Innes <kiall@hpe.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# See https://blueprints.launchpad.net/nova/+spec/backportable-db-migrations
# http://lists.openstack.org/pipermail/openstack-dev/2013-March/006827.html
from sqlalchemy.schema import Table, MetaData


meta = MetaData()


def upgrade(migrate_engine):
    meta.bind = migrate_engine

    status_table = Table('pool_manager_statuses', meta, autoload=True)

    status_table.c.domain_id.alter(name='zone_id')


def downgrade(migration_engine):
    pass
