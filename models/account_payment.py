from odoo import models, fields


class AccountPayment(models.Model):
    _inherit = "account.payment"

    # Informations TVA


    vat_return_id = fields.Many2one(
        "l10n.ma.vat.return",
        string="Déclaration TVA",
        help="Déclaration TVA liée à ce paiement.",
    )

    vat_processed = fields.Boolean(
        string="TVA traitée",
        default=False,
        help="Indique si ce paiement a déjà été pris en compte dans une déclaration TVA.",
    )

    payment_reference_dgi = fields.Char(
        string="Référence DGI",
        help="Référence utilisée pour les échanges avec la Direction Générale des Impôts.",
    )

    payment_type_dgi = fields.Selection(
        [
            ("cash", "Espèces"),
            ("bank", "Virement bancaire"),
            ("check", "Chèque"),
            ("card", "Carte bancaire"),
            ("other", "Autre"),
        ],
        string="Mode de paiement DGI",
        help="Mode de paiement utilisé pour la déclaration fiscale.",
    )