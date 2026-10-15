# Tenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**slug** | **str** |  | 
**display_name** | **str** |  | 
**status** | **str** |  | 
**plan** | **str** |  | 
**rate_cap_per_min** | **int** | Per-tenant share of the per-VPS 5/min outbound cap (L6). | 
**daily_msg_quota** | **int** |  | 
**admin_email** | **str** |  | 
**created_at** | **datetime** |  | 
**suspended_at** | **datetime** |  | [optional] 
**closed_at** | **datetime** |  | [optional] 
**hard_delete_after** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.tenant import Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant from a JSON string
tenant_instance = Tenant.from_json(json)
# print the JSON string representation of the object
print(Tenant.to_json())

# convert the object into a dict
tenant_dict = tenant_instance.to_dict()
# create an instance of Tenant from a dict
tenant_from_dict = Tenant.from_dict(tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


