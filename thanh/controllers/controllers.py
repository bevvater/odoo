# -*- coding: utf-8 -*-
from openerp import http

# class Thanh(http.Controller):
#     @http.route('/thanh/thanh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/thanh/thanh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('thanh.listing', {
#             'root': '/thanh/thanh',
#             'objects': http.request.env['thanh.thanh'].search([]),
#         })

#     @http.route('/thanh/thanh/objects/<model("thanh.thanh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('thanh.object', {
#             'object': obj
#         })