# Copyright (C) 2017 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

from ggrc import db
from .mixins import BusinessObject, Timeboxed, CustomAttributable
from .object_owner import Ownable
from .object_person import Personable
from .relationship import Relatable
from .track_object_state import HasObjectState, track_state_for_class


class OrgGroup(HasObjectState, CustomAttributable,
               Personable, Relatable, Timeboxed,
               Ownable, BusinessObject, db.Model):
  __tablename__ = 'org_groups'
  _aliases = {"url": "Org Group URL"}

track_state_for_class(OrgGroup)
