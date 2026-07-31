# from odoo import http


# class L10nMaVatSimpl(http.Controller):
#     @http.route('/l10n_ma_vat_simpl/l10n_ma_vat_simpl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_ma_vat_simpl/l10n_ma_vat_simpl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_ma_vat_simpl.listing', {
#             'root': '/l10n_ma_vat_simpl/l10n_ma_vat_simpl',
#             'objects': http.request.env['l10n_ma_vat_simpl.l10n_ma_vat_simpl'].search([]),
#         })

#     @http.route('/l10n_ma_vat_simpl/l10n_ma_vat_simpl/objects/<model("l10n_ma_vat_simpl.l10n_ma_vat_simpl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_ma_vat_simpl.object', {
#             'object': obj
#         })

