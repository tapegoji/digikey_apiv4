# coding: utf-8

"""
    ProductSearch Api

    ProductSearch Api  # noqa: E501

    OpenAPI spec version: v4
    Contact: dl_Agile_Team_B2B_API@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dk_api_client.configuration import Configuration


class Product(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'Description',
        'manufacturer': 'Manufacturer',
        'manufacturer_product_number': 'str',
        'minimum_order_quantity': 'int',
        'unit_price': 'float',
        'product_url': 'str',
        'datasheet_url': 'str',
        'photo_url': 'str',
        'product_variations': 'list[ProductVariation]',
        'quantity_available': 'int',
        'product_status': 'ProductStatusV3',
        'back_order_not_allowed': 'bool',
        'discontinued': 'bool',
        'end_of_life': 'bool',
        'ncnr': 'bool',
        'primary_video_url': 'str',
        'parameters': 'list[ParameterValue]',
        'base_product_number': 'BaseProduct',
        'category': 'CategoryNode',
        'date_last_buy_chance': 'datetime',
        'manufacturer_lead_weeks': 'str',
        'manufacturer_public_quantity': 'int',
        'max_quantity_for_distribution': 'int',
        'series': 'Series',
        'standard_package': 'int',
        'shipping_info': 'str',
        'classifications': 'Classifications'
    }

    attribute_map = {
        'description': 'Description',
        'manufacturer': 'Manufacturer',
        'manufacturer_product_number': 'ManufacturerProductNumber',
        'minimum_order_quantity': 'MinimumOrderQuantity',
        'unit_price': 'UnitPrice',
        'product_url': 'ProductUrl',
        'datasheet_url': 'DatasheetUrl',
        'photo_url': 'PhotoUrl',
        'product_variations': 'ProductVariations',
        'quantity_available': 'QuantityAvailable',
        'product_status': 'ProductStatus',
        'back_order_not_allowed': 'BackOrderNotAllowed',
        'discontinued': 'Discontinued',
        'end_of_life': 'EndOfLife',
        'ncnr': 'Ncnr',
        'primary_video_url': 'PrimaryVideoUrl',
        'parameters': 'Parameters',
        'base_product_number': 'BaseProductNumber',
        'category': 'Category',
        'date_last_buy_chance': 'DateLastBuyChance',
        'manufacturer_lead_weeks': 'ManufacturerLeadWeeks',
        'manufacturer_public_quantity': 'ManufacturerPublicQuantity',
        'max_quantity_for_distribution': 'MaxQuantityForDistribution',
        'series': 'Series',
        'standard_package': 'StandardPackage',
        'shipping_info': 'ShippingInfo',
        'classifications': 'Classifications'
    }

    def __init__(self, description=None, manufacturer=None, manufacturer_product_number=None, minimum_order_quantity=None, unit_price=None, product_url=None, datasheet_url=None, photo_url=None, product_variations=None, quantity_available=None, product_status=None, back_order_not_allowed=None, discontinued=None, end_of_life=None, ncnr=None, primary_video_url=None, parameters=None, base_product_number=None, category=None, date_last_buy_chance=None, manufacturer_lead_weeks=None, manufacturer_public_quantity=None, max_quantity_for_distribution=None, series=None, standard_package=None, shipping_info=None, classifications=None, _configuration=None):  # noqa: E501
        """Product - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._manufacturer = None
        self._manufacturer_product_number = None
        self._minimum_order_quantity = None
        self._unit_price = None
        self._product_url = None
        self._datasheet_url = None
        self._photo_url = None
        self._product_variations = None
        self._quantity_available = None
        self._product_status = None
        self._back_order_not_allowed = None
        self._discontinued = None
        self._end_of_life = None
        self._ncnr = None
        self._primary_video_url = None
        self._parameters = None
        self._base_product_number = None
        self._category = None
        self._date_last_buy_chance = None
        self._manufacturer_lead_weeks = None
        self._manufacturer_public_quantity = None
        self._max_quantity_for_distribution = None
        self._series = None
        self._standard_package = None
        self._shipping_info = None
        self._classifications = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if manufacturer_product_number is not None:
            self.manufacturer_product_number = manufacturer_product_number
        if minimum_order_quantity is not None:
            self.minimum_order_quantity = minimum_order_quantity
        if unit_price is not None:
            self.unit_price = unit_price
        if product_url is not None:
            self.product_url = product_url
        if datasheet_url is not None:
            self.datasheet_url = datasheet_url
        if photo_url is not None:
            self.photo_url = photo_url
        if product_variations is not None:
            self.product_variations = product_variations
        if quantity_available is not None:
            self.quantity_available = quantity_available
        if product_status is not None:
            self.product_status = product_status
        if back_order_not_allowed is not None:
            self.back_order_not_allowed = back_order_not_allowed
        if discontinued is not None:
            self.discontinued = discontinued
        if end_of_life is not None:
            self.end_of_life = end_of_life
        if ncnr is not None:
            self.ncnr = ncnr
        if primary_video_url is not None:
            self.primary_video_url = primary_video_url
        if parameters is not None:
            self.parameters = parameters
        if base_product_number is not None:
            self.base_product_number = base_product_number
        if category is not None:
            self.category = category
        if date_last_buy_chance is not None:
            self.date_last_buy_chance = date_last_buy_chance
        if manufacturer_lead_weeks is not None:
            self.manufacturer_lead_weeks = manufacturer_lead_weeks
        if manufacturer_public_quantity is not None:
            self.manufacturer_public_quantity = manufacturer_public_quantity
        if max_quantity_for_distribution is not None:
            self.max_quantity_for_distribution = max_quantity_for_distribution
        if series is not None:
            self.series = series
        if standard_package is not None:
            self.standard_package = standard_package
        if shipping_info is not None:
            self.shipping_info = shipping_info
        if classifications is not None:
            self.classifications = classifications

    @property
    def description(self):
        """Gets the description of this Product.  # noqa: E501


        :return: The description of this Product.  # noqa: E501
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Product.


        :param description: The description of this Product.  # noqa: E501
        :type: Description
        """

        self._description = description

    @property
    def manufacturer(self):
        """Gets the manufacturer of this Product.  # noqa: E501


        :return: The manufacturer of this Product.  # noqa: E501
        :rtype: Manufacturer
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this Product.


        :param manufacturer: The manufacturer of this Product.  # noqa: E501
        :type: Manufacturer
        """

        self._manufacturer = manufacturer

    @property
    def manufacturer_product_number(self):
        """Gets the manufacturer_product_number of this Product.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for different parts.  # noqa: E501

        :return: The manufacturer_product_number of this Product.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_product_number

    @manufacturer_product_number.setter
    def manufacturer_product_number(self, manufacturer_product_number):
        """Sets the manufacturer_product_number of this Product.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for different parts.  # noqa: E501

        :param manufacturer_product_number: The manufacturer_product_number of this Product.  # noqa: E501
        :type: str
        """

        self._manufacturer_product_number = manufacturer_product_number

    @property
    def minimum_order_quantity(self):
        """Gets the minimum_order_quantity of this Product.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this Product.  # noqa: E501
        :rtype: int
        """
        return self._minimum_order_quantity

    @minimum_order_quantity.setter
    def minimum_order_quantity(self, minimum_order_quantity):
        """Sets the minimum_order_quantity of this Product.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this Product.  # noqa: E501
        :type: int
        """

        self._minimum_order_quantity = minimum_order_quantity

    @property
    def unit_price(self):
        """Gets the unit_price of this Product.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this Product.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this Product.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this Product.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def product_url(self):
        """Gets the product_url of this Product.  # noqa: E501

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :return: The product_url of this Product.  # noqa: E501
        :rtype: str
        """
        return self._product_url

    @product_url.setter
    def product_url(self, product_url):
        """Sets the product_url of this Product.

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :param product_url: The product_url of this Product.  # noqa: E501
        :type: str
        """

        self._product_url = product_url

    @property
    def datasheet_url(self):
        """Gets the datasheet_url of this Product.  # noqa: E501

        The URL to the product's datasheet.  # noqa: E501

        :return: The datasheet_url of this Product.  # noqa: E501
        :rtype: str
        """
        return self._datasheet_url

    @datasheet_url.setter
    def datasheet_url(self, datasheet_url):
        """Sets the datasheet_url of this Product.

        The URL to the product's datasheet.  # noqa: E501

        :param datasheet_url: The datasheet_url of this Product.  # noqa: E501
        :type: str
        """

        self._datasheet_url = datasheet_url

    @property
    def photo_url(self):
        """Gets the photo_url of this Product.  # noqa: E501

        The URL to the product's image.  # noqa: E501

        :return: The photo_url of this Product.  # noqa: E501
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """Sets the photo_url of this Product.

        The URL to the product's image.  # noqa: E501

        :param photo_url: The photo_url of this Product.  # noqa: E501
        :type: str
        """

        self._photo_url = photo_url

    @property
    def product_variations(self):
        """Gets the product_variations of this Product.  # noqa: E501


        :return: The product_variations of this Product.  # noqa: E501
        :rtype: list[ProductVariation]
        """
        return self._product_variations

    @product_variations.setter
    def product_variations(self, product_variations):
        """Sets the product_variations of this Product.


        :param product_variations: The product_variations of this Product.  # noqa: E501
        :type: list[ProductVariation]
        """

        self._product_variations = product_variations

    @property
    def quantity_available(self):
        """Gets the quantity_available of this Product.  # noqa: E501

        The sum of the quantity for all package types that are found in ProductVariations.  # noqa: E501

        :return: The quantity_available of this Product.  # noqa: E501
        :rtype: int
        """
        return self._quantity_available

    @quantity_available.setter
    def quantity_available(self, quantity_available):
        """Sets the quantity_available of this Product.

        The sum of the quantity for all package types that are found in ProductVariations.  # noqa: E501

        :param quantity_available: The quantity_available of this Product.  # noqa: E501
        :type: int
        """

        self._quantity_available = quantity_available

    @property
    def product_status(self):
        """Gets the product_status of this Product.  # noqa: E501


        :return: The product_status of this Product.  # noqa: E501
        :rtype: ProductStatusV3
        """
        return self._product_status

    @product_status.setter
    def product_status(self, product_status):
        """Sets the product_status of this Product.


        :param product_status: The product_status of this Product.  # noqa: E501
        :type: ProductStatusV3
        """

        self._product_status = product_status

    @property
    def back_order_not_allowed(self):
        """Gets the back_order_not_allowed of this Product.  # noqa: E501

        True if back order is not allowed for this product  # noqa: E501

        :return: The back_order_not_allowed of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._back_order_not_allowed

    @back_order_not_allowed.setter
    def back_order_not_allowed(self, back_order_not_allowed):
        """Sets the back_order_not_allowed of this Product.

        True if back order is not allowed for this product  # noqa: E501

        :param back_order_not_allowed: The back_order_not_allowed of this Product.  # noqa: E501
        :type: bool
        """

        self._back_order_not_allowed = back_order_not_allowed

    @property
    def discontinued(self):
        """Gets the discontinued of this Product.  # noqa: E501

        This product is no longer sold at Digi-Key and will no longer be stocked.  # noqa: E501

        :return: The discontinued of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._discontinued

    @discontinued.setter
    def discontinued(self, discontinued):
        """Sets the discontinued of this Product.

        This product is no longer sold at Digi-Key and will no longer be stocked.  # noqa: E501

        :param discontinued: The discontinued of this Product.  # noqa: E501
        :type: bool
        """

        self._discontinued = discontinued

    @property
    def end_of_life(self):
        """Gets the end_of_life of this Product.  # noqa: E501

        This product is no longer manufactured and will no longer be stocked once stock is depleted.  # noqa: E501

        :return: The end_of_life of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._end_of_life

    @end_of_life.setter
    def end_of_life(self, end_of_life):
        """Sets the end_of_life of this Product.

        This product is no longer manufactured and will no longer be stocked once stock is depleted.  # noqa: E501

        :param end_of_life: The end_of_life of this Product.  # noqa: E501
        :type: bool
        """

        self._end_of_life = end_of_life

    @property
    def ncnr(self):
        """Gets the ncnr of this Product.  # noqa: E501

        Is product non-cancellable and non-returnable  # noqa: E501

        :return: The ncnr of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._ncnr

    @ncnr.setter
    def ncnr(self, ncnr):
        """Sets the ncnr of this Product.

        Is product non-cancellable and non-returnable  # noqa: E501

        :param ncnr: The ncnr of this Product.  # noqa: E501
        :type: bool
        """

        self._ncnr = ncnr

    @property
    def primary_video_url(self):
        """Gets the primary_video_url of this Product.  # noqa: E501

        The URL to the product's video  # noqa: E501

        :return: The primary_video_url of this Product.  # noqa: E501
        :rtype: str
        """
        return self._primary_video_url

    @primary_video_url.setter
    def primary_video_url(self, primary_video_url):
        """Sets the primary_video_url of this Product.

        The URL to the product's video  # noqa: E501

        :param primary_video_url: The primary_video_url of this Product.  # noqa: E501
        :type: str
        """

        self._primary_video_url = primary_video_url

    @property
    def parameters(self):
        """Gets the parameters of this Product.  # noqa: E501


        :return: The parameters of this Product.  # noqa: E501
        :rtype: list[ParameterValue]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Product.


        :param parameters: The parameters of this Product.  # noqa: E501
        :type: list[ParameterValue]
        """

        self._parameters = parameters

    @property
    def base_product_number(self):
        """Gets the base_product_number of this Product.  # noqa: E501


        :return: The base_product_number of this Product.  # noqa: E501
        :rtype: BaseProduct
        """
        return self._base_product_number

    @base_product_number.setter
    def base_product_number(self, base_product_number):
        """Sets the base_product_number of this Product.


        :param base_product_number: The base_product_number of this Product.  # noqa: E501
        :type: BaseProduct
        """

        self._base_product_number = base_product_number

    @property
    def category(self):
        """Gets the category of this Product.  # noqa: E501


        :return: The category of this Product.  # noqa: E501
        :rtype: CategoryNode
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Product.


        :param category: The category of this Product.  # noqa: E501
        :type: CategoryNode
        """

        self._category = category

    @property
    def date_last_buy_chance(self):
        """Gets the date_last_buy_chance of this Product.  # noqa: E501

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :return: The date_last_buy_chance of this Product.  # noqa: E501
        :rtype: datetime
        """
        return self._date_last_buy_chance

    @date_last_buy_chance.setter
    def date_last_buy_chance(self, date_last_buy_chance):
        """Sets the date_last_buy_chance of this Product.

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :param date_last_buy_chance: The date_last_buy_chance of this Product.  # noqa: E501
        :type: datetime
        """

        self._date_last_buy_chance = date_last_buy_chance

    @property
    def manufacturer_lead_weeks(self):
        """Gets the manufacturer_lead_weeks of this Product.  # noqa: E501

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :return: The manufacturer_lead_weeks of this Product.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_lead_weeks

    @manufacturer_lead_weeks.setter
    def manufacturer_lead_weeks(self, manufacturer_lead_weeks):
        """Sets the manufacturer_lead_weeks of this Product.

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :param manufacturer_lead_weeks: The manufacturer_lead_weeks of this Product.  # noqa: E501
        :type: str
        """

        self._manufacturer_lead_weeks = manufacturer_lead_weeks

    @property
    def manufacturer_public_quantity(self):
        """Gets the manufacturer_public_quantity of this Product.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this Product.  # noqa: E501
        :rtype: int
        """
        return self._manufacturer_public_quantity

    @manufacturer_public_quantity.setter
    def manufacturer_public_quantity(self, manufacturer_public_quantity):
        """Sets the manufacturer_public_quantity of this Product.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this Product.  # noqa: E501
        :type: int
        """

        self._manufacturer_public_quantity = manufacturer_public_quantity

    @property
    def max_quantity_for_distribution(self):
        """Gets the max_quantity_for_distribution of this Product.  # noqa: E501

        Maximum order quantity for Distribution  # noqa: E501

        :return: The max_quantity_for_distribution of this Product.  # noqa: E501
        :rtype: int
        """
        return self._max_quantity_for_distribution

    @max_quantity_for_distribution.setter
    def max_quantity_for_distribution(self, max_quantity_for_distribution):
        """Sets the max_quantity_for_distribution of this Product.

        Maximum order quantity for Distribution  # noqa: E501

        :param max_quantity_for_distribution: The max_quantity_for_distribution of this Product.  # noqa: E501
        :type: int
        """

        self._max_quantity_for_distribution = max_quantity_for_distribution

    @property
    def series(self):
        """Gets the series of this Product.  # noqa: E501


        :return: The series of this Product.  # noqa: E501
        :rtype: Series
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this Product.


        :param series: The series of this Product.  # noqa: E501
        :type: Series
        """

        self._series = series

    @property
    def standard_package(self):
        """Gets the standard_package of this Product.  # noqa: E501

        StandardPackage  # noqa: E501

        :return: The standard_package of this Product.  # noqa: E501
        :rtype: int
        """
        return self._standard_package

    @standard_package.setter
    def standard_package(self, standard_package):
        """Sets the standard_package of this Product.

        StandardPackage  # noqa: E501

        :param standard_package: The standard_package of this Product.  # noqa: E501
        :type: int
        """

        self._standard_package = standard_package

    @property
    def shipping_info(self):
        """Gets the shipping_info of this Product.  # noqa: E501

        Additional shipping information - if available  # noqa: E501

        :return: The shipping_info of this Product.  # noqa: E501
        :rtype: str
        """
        return self._shipping_info

    @shipping_info.setter
    def shipping_info(self, shipping_info):
        """Sets the shipping_info of this Product.

        Additional shipping information - if available  # noqa: E501

        :param shipping_info: The shipping_info of this Product.  # noqa: E501
        :type: str
        """

        self._shipping_info = shipping_info

    @property
    def classifications(self):
        """Gets the classifications of this Product.  # noqa: E501


        :return: The classifications of this Product.  # noqa: E501
        :rtype: Classifications
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this Product.


        :param classifications: The classifications of this Product.  # noqa: E501
        :type: Classifications
        """

        self._classifications = classifications

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Product, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Product):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Product):
            return True

        return self.to_dict() != other.to_dict()