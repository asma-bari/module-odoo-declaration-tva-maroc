from odoo import models, fields


class VatDeductionLine(models.Model):
    _name = "l10n.ma.vat.deduction.line"
    _description = "Ligne du relevé des déductions TVA"
    _order = "invoice_date desc, id"

    # Relations

    vat_return_id = fields.Many2one(
        "l10n.ma.vat.return",
        string="Déclaration TVA",
        required=True,
        ondelete="cascade",
    )

    move_id = fields.Many2one(
        "account.move",
        string="Facture fournisseur",
        required=False,
    )

    partner_id = fields.Many2one(
        "res.partner",
        string="Fournisseur",
        required=True,
    )

    currency_id = fields.Many2one(
        "res.currency",
        related="vat_return_id.currency_id",
        store=True,
        readonly=True,
    )

    # Informations facture

    invoice_number = fields.Char(
        string="Numéro de facture",
    )

    invoice_date = fields.Date(
        string="Date de facture",
    )

    payment_date = fields.Date(
        string="Date de paiement",
    )

    # Informations fiscales

    supplier_ice = fields.Char(
        string="ICE Fournisseur",
    )#L'ICE (Identifiant Commun de l'Entreprise)

    supplier_if = fields.Char(
        string="IF Fournisseur",
    )#IF (Identifiant Fiscal).

    supplier_rc = fields.Char(
        string="RC Fournisseur",
    )#RC (Registre de Commerce).

    # Montants

    amount_untaxed = fields.Monetary(
        string="Montant HT",
        currency_field="currency_id",
    )

    tax_amount = fields.Monetary(
        string="Montant TVA",
        currency_field="currency_id",
    )

    total_amount = fields.Monetary(
        string="Montant TTC",
        currency_field="currency_id",
    )

    # Paiement

    payment_method = fields.Selection(
        [
            ("cash", "Espèces"),
            ("bank", "Virement bancaire"),
            ("check", "Chèque"),
            ("card", "Carte bancaire"),
            ("other", "Autre"),
        ],
        string="Mode de paiement",
    )

    # Etat


    deductible = fields.Boolean(
        string="TVA déductible",
        default=True,
    )

    note = fields.Text(
        string="Observations",
    )

    active = fields.Boolean(
        string="Actif",
        default=True,
    )