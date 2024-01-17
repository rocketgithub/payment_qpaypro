# coding: utf-8
import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class AcquirerQPayPro(models.Model):
    _inherit = 'payment.acquirer'
    
    provider = fields.Selection(selection_add=[('qpaypro', 'QPayPro')], ondelete={'qpaypro': 'set default'})
    qpaypro_login = fields.Char('Login', required_if_provider='qpaypro', groups='base.group_user')
    qpaypro_api_secret = fields.Char('API Secret', required_if_provider='qpaypro', groups='base.group_user')

    def _qpaypro_get_api_url(self):
        self.ensure_one()
        if self.state == 'enabled':
            return "https://sandboxpayments.qpaypro.com/checkout/store"
        else:
            return "https://payments.qpaypro.com/checkout/store"
            
    def _get_default_payment_method_id(self):
        self.ensure_one()
        if self.provider != 'qpaypro':
            return super()._get_default_payment_method_id()
        return self.env.ref('payment_qpaypro.payment_method_qpaypro').id
