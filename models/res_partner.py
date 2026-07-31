from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"#Il modifie le modèle existant.

    # Informations fiscales DES PARTENAIRE :Clients,Fournisseurs,Sociétés,Contacts

    ice = fields.Char(
        string="ICE",
        help="Identifiant Commun de l'Entreprise",
        tracking=True,
    )

    if_number = fields.Char(
        string="Identifiant Fiscal (IF)",
        help="Identifiant Fiscal attribué par l'administration fiscale",
        tracking=True,
    )
    rc = fields.Char(
        string="Registre de Commerce (RC)",
        help="Numéro du Registre de Commerce",
        tracking=True,
    )

    patent = fields.Char(
        string="Patente",
        help="Numéro de patente",
        tracking=True,
    )#une taxe professionnelle.

    tax_certificate = fields.Boolean(
        string="Attestation fiscale valide",
        default=False,
        help="Indique si le partenaire possède une attestation fiscale valide",
        tracking=True,
    )

    tax_certificate_expiry = fields.Date(
        string="Date d'expiration de l'attestation",
        help="Date d'expiration de l'attestation fiscale",
        tracking=True,
    )

    vat_regime = fields.Selection(
        [
            ("cash", "Encaissements"),
            ("accrual", "Débits"),
        ],
        string="Régime TVA",
        default="cash",
        help="Régime de TVA appliqué à ce partenaire",
        tracking=True,
    )

    is_tax_exempt = fields.Boolean(
        string="Exonéré de TVA",
        default=False,
        help="Indique si ce partenaire est exonéré de TVA",
        tracking=True,
    )

    simpl_reference = fields.Char(
        string="Référence SIMPL",
        help="Référence utilisée pour les échanges avec le portail SIMPL",
        tracking=True,
    )
    #Permettre au module TVA marocain de connaître les informations fiscales de chaque entreprise avec laquelle on travaille afin de générer correctement les déclarations TVA et les fichiers XML SIMPL.