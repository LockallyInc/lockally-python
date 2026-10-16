# WhoamiTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**name** | **str** | What the account calls itself. | [optional] 
**plan** | **str** |  | [optional] 

## Example

```python
from lockally.models.whoami_tenant import WhoamiTenant

# TODO update the JSON string below
json = "{}"
# create an instance of WhoamiTenant from a JSON string
whoami_tenant_instance = WhoamiTenant.from_json(json)
# print the JSON string representation of the object
print(WhoamiTenant.to_json())

# convert the object into a dict
whoami_tenant_dict = whoami_tenant_instance.to_dict()
# create an instance of WhoamiTenant from a dict
whoami_tenant_from_dict = WhoamiTenant.from_dict(whoami_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


