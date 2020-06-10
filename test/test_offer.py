# coding: utf-8

"""
    Yagna Market API

     ## Yagna Market The Yagna Market is a core component of the Yagna Network, which enables computational Offers and Demands circulation. The Market is open for all entities willing to buy computations (Demands) or monetize computational resources (Offers). ## Yagna Market API The Yagna Market API is the entry to the Yagna Market through which Requestors and Providers can publish their Demands and Offers respectively, find matching counterparty, conduct negotiations and make an agreement.  This version of Market API conforms with capability level 1 of the <a href=\"https://docs.google.com/document/d/1Zny_vfgWV-hcsKS7P-Kdr3Fb0dwfl-6T_cYKVQ9mkNg\"> Market API specification</a>.  Market API contains two roles: Requestors and Providers which are symmetrical most of the time (excluding agreement phase).   # noqa: E501

    The version of the OpenAPI document: 1.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ya_market
from ya_market.models.offer import Offer  # noqa: E501
from ya_market.rest import ApiException

class TestOffer(unittest.TestCase):
    """Offer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Offer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ya_market.models.offer.Offer()  # noqa: E501
        if include_optional :
            return Offer(
                properties = None, 
                constraints = '0', 
                offer_id = '0', 
                provider_id = '0'
            )
        else :
            return Offer(
                properties = None,
                constraints = '0',
        )

    def testOffer(self):
        """Test Offer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
