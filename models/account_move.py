from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    # Informations TVA

    vat_return_id = fields.Many2one(
        "l10n.ma.vat.return",
        string="Déclaration TVA",
        help="Déclaration TVA à laquelle cette facture est rattachée.",
    )

    vat_due_date = fields.Date(
        string="Date d'exigibilité TVA",
        help="Date à partir de laquelle la TVA devient exigible.",
    )

    vat_processed = fields.Boolean(
        string="TVA traitée",
        default=False,
        help="Indique si cette facture a déjà été prise en compte dans une déclaration TVA.",
    )

    vat_payment_regime = fields.Selection(
        [
            ("cash", "Encaissements"),
            ("accrual", "Débits"),
        ],
        string="Régime TVA",
        help="Régime de TVA appliqué à cette facture.",
    )