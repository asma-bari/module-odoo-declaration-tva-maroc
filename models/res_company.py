from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    # Paramètres TVA

    vat_regime = fields.Selection(
        [
            ("cash", "Encaissements"),
            ("accrual", "Débits"),
        ],
        string="Régime TVA",
        default="cash",
        required=True,
        help="Régime de TVA utilisé par la société.",
    )

    vat_periodicity = fields.Selection(
        [
            ("monthly", "Mensuelle"),
            ("quarterly", "Trimestrielle"),
        ],
        string="Périodicité TVA",
        default="monthly",
        required=True,
        help="Fréquence de déclaration de la TVA.",
    )

    vat_prorata = fields.Float(
        string="Prorata TVA (%)",
        default=100.0,
        help="Pourcentage de TVA récupérable.",
    )

    cash_payment_limit = fields.Monetary(
        string="Seuil de paiement en espèces",
        currency_field="currency_id",
        help="Montant maximum autorisé pour un paiement en espèces.",
    )

    simpl_username = fields.Char(
        string="Identifiant SIMPL",
        help="Identifiant utilisé pour le portail SIMPL.",
    )

    simpl_reference = fields.Char(
        string="Référence fiscale",
        help="Référence utilisée pour les déclarations SIMPL.",
    )