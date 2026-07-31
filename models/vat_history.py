from odoo import models, fields

class VatHistory(models.Model):
    _name = "l10n.ma.vat.history"
    _description = "Historique des déclarations TVA"
    _order = "action_date desc, id"

    # Relations

    vat_return_id = fields.Many2one(
        "l10n.ma.vat.return",
        string="Déclaration TVA",
        required=True,
        ondelete="cascade",
    )

    user_id = fields.Many2one(
        "res.users",#représente les utilisateurs du système.
        string="Utilisateur",
        required=True,
        default=lambda self: self.env.user,#Prends automatiquement l'utilisateur actuellement connecté à Odoo.
        readonly=True,
    )#Cette ligne d'historique a été réalisée par quel utilisateur ?


    # Informations sur l'action

    action = fields.Selection(
        [
            ("create", "Création"),
            ("prepare", "Préparation"),
            ("check", "Contrôle"),
            ("validate", "Validation"),
            ("submit", "Dépôt"),
            ("export_xml", "Export XML"),
            ("export_excel", "Export Excel"),
            ("export_pdf", "Export PDF"),
            ("cancel", "Annulation"),
        ],
        string="Action",
        required=True,
    )

    action_date = fields.Datetime(
        string="Date de l'action",
        default=fields.Datetime.now,
        readonly=True,
    )

    state = fields.Selection(
        [
            ("draft", "Brouillon"),
            ("prepared", "Préparée"),
            ("checked", "Contrôlée"),
            ("validated", "Validée"),
            ("submitted", "Déposée"),
            ("cancel", "Annulée"),
        ],
        string="État de la déclaration",
    )#l'état de la déclaration après l'action.

    # Informations complémentaires
    
    description = fields.Text(
        string="Description",
    )

    ip_address = fields.Char(
        string="Adresse IP",
    )#depuis quelle machine ou quel réseau l'action a été faite.

    active = fields.Boolean(
        string="Actif",
        default=True,
    )#archiver un enregistrement