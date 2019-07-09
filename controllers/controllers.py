# -*- coding: utf-8 -*-
from odoo import http

# class F2fTestModule(http.Controller):
#     @http.route('/f2f_test_module/f2f_test_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/f2f_test_module/f2f_test_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('f2f_test_module.listing', {
#             'root': '/f2f_test_module/f2f_test_module',
#             'objects': http.request.env['f2f_test_module.f2f_test_module'].search([]),
#         })

#     @http.route('/f2f_test_module/f2f_test_module/objects/<model("f2f_test_module.f2f_test_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('f2f_test_module.object', {
#             'object': obj
#         })