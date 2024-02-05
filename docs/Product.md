# Product

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Description**](Description.md) |  | [optional] 
**manufacturer** | [**Manufacturer**](Manufacturer.md) |  | [optional] 
**manufacturer_product_number** | **str** | The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for different parts. | [optional] 
**minimum_order_quantity** | **int** | The minimum quantity to order from Digi-Key. | [optional] 
**unit_price** | **float** | The price for a single unit of this product. | [optional] 
**product_url** | **str** | Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values. | [optional] 
**datasheet_url** | **str** | The URL to the product&#39;s datasheet. | [optional] 
**photo_url** | **str** | The URL to the product&#39;s image. | [optional] 
**product_variations** | [**list[ProductVariation]**](ProductVariation.md) |  | [optional] 
**quantity_available** | **int** | The sum of the quantity for all package types that are found in ProductVariations. | [optional] 
**product_status** | [**ProductStatusV3**](ProductStatusV3.md) |  | [optional] 
**back_order_not_allowed** | **bool** | True if back order is not allowed for this product | [optional] 
**discontinued** | **bool** | This product is no longer sold at Digi-Key and will no longer be stocked. | [optional] 
**end_of_life** | **bool** | This product is no longer manufactured and will no longer be stocked once stock is depleted. | [optional] 
**ncnr** | **bool** | Is product non-cancellable and non-returnable | [optional] 
**primary_video_url** | **str** | The URL to the product&#39;s video | [optional] 
**parameters** | [**list[ParameterValue]**](ParameterValue.md) |  | [optional] 
**base_product_number** | [**BaseProduct**](BaseProduct.md) |  | [optional] 
**category** | [**CategoryNode**](CategoryNode.md) |  | [optional] 
**date_last_buy_chance** | **datetime** | Last date that the product will be available for purchase. Date is in ISO 8601. | [optional] 
**manufacturer_lead_weeks** | **str** | The number of weeks expected to receive stock from manufacturer. | [optional] 
**manufacturer_public_quantity** | **int** | Quantity of this product available to order from manufacturer. | [optional] 
**max_quantity_for_distribution** | **int** | Maximum order quantity for Distribution | [optional] 
**series** | [**Series**](Series.md) |  | [optional] 
**standard_package** | **int** | StandardPackage | [optional] 
**shipping_info** | **str** | Additional shipping information - if available | [optional] 
**classifications** | [**Classifications**](Classifications.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


