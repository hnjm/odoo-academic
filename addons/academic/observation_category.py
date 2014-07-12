# -*- coding: utf-8 -*-
##############################################################################
#
#    Academic
#    Copyright (C) 2014 No author.
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import re
from openerp import netsvc
from openerp.osv import osv, fields

class observation_category(osv.osv):
    """"""
    
    _name = 'academic.observation_category'
    _description = 'observation_category'

    _columns = {
        'name': fields.char(string='Name', required=True, translate=True),
        'dont_consider': fields.boolean(string='Don not Consider?'),
    }

    _defaults = {
    }


    _constraints = [
    ]




observation_category()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
