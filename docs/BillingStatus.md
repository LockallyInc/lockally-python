# BillingStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** |  | 
**display_name** | **str** |  | 
**mode** | **str** |  | 
**rate_cap_per_min** | **int** |  | 
**monthly_included_sends** | **int** |  | 
**msgs_this_period** | **int** |  | 
**status** | **str** |  | 
**price_naira_per_seat** | **int** |  | 
**subscribed_at** | **datetime** |  | [optional] 
**current_period_end** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**send_units_balance** | **int** |  | 
**send_units_next_expiry** | **datetime** |  | [optional] 
**unit_bundles** | [**List[UnitBundle]**](UnitBundle.md) |  | 
**catalog** | [**List[PlanCatalogEntry]**](PlanCatalogEntry.md) |  | 

## Example

```python
from lockally.models.billing_status import BillingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BillingStatus from a JSON string
billing_status_instance = BillingStatus.from_json(json)
# print the JSON string representation of the object
print(BillingStatus.to_json())

# convert the object into a dict
billing_status_dict = billing_status_instance.to_dict()
# create an instance of BillingStatus from a dict
billing_status_from_dict = BillingStatus.from_dict(billing_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


