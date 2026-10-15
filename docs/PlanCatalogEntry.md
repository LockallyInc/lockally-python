# PlanCatalogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**price_naira_per_seat** | **int** |  | 
**rate_cap_per_min** | **int** |  | 
**monthly_included_sends** | **int** |  | 
**has_shared_mailboxes** | **bool** |  | 
**has_send_units** | **bool** |  | 
**has_ai_units** | **bool** |  | 
**has_e2e_encryption** | **bool** |  | 

## Example

```python
from lockally.models.plan_catalog_entry import PlanCatalogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PlanCatalogEntry from a JSON string
plan_catalog_entry_instance = PlanCatalogEntry.from_json(json)
# print the JSON string representation of the object
print(PlanCatalogEntry.to_json())

# convert the object into a dict
plan_catalog_entry_dict = plan_catalog_entry_instance.to_dict()
# create an instance of PlanCatalogEntry from a dict
plan_catalog_entry_from_dict = PlanCatalogEntry.from_dict(plan_catalog_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


