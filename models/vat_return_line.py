from odoo import models, fields


class VatReturnLine(models.Model):
    _name = "l10n.ma.vat.return.line"
    _description = "Ligne de déclaration TVA"
    _order = "sequence, id"


    # Informations générales
 
    sequence = fields.Integer(
        string="Ordre",
        default=10,
    )

    vat_return_id = fields.Many2one(
        "l10n.ma.vat.return",
        string="Déclaration TVA",
        required=True,
        ondelete="cascade",
    )

    currency_id = fields.Many2one(
        "res.currency",
        related="vat_return_id.currency_id",
        store=True,
        readonly=True,
    )

    # Rubrique de déclaration
 
    name = fields.Char(
        string="Rubrique",
        required=True,
    )

    line_type = fields.Selection(
        [
            ("sale", "Ventes"),
            ("purchase", "Achats"),
            ("deduction", "Déductions"),
            ("credit", "Crédit TVA"),
            ("autoliquidation", "Autoliquidation"),
            ("ras", "Retenue à la source"),
        ],
        string="Type de rubrique",
        required=True,
    )

    tax_rate = fields.Float(
        string="Taux TVA (%)",
    )

    # Montants
 
    base_amount = fields.Monetary(
        string="Montant HT",
        currency_field="currency_id",
    )

    vat_amount = fields.Monetary(
        string="Montant TVA",
        currency_field="currency_id",
    )

    # Informations complémentaires

    note = fields.Text(
        string="Observations",
    )

    active = fields.Boolean(
        string="Actif",
        default=True,
    )