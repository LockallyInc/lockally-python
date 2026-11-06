# TenantHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Stable identifier, today one of &#x60;domain_verification&#x60;, &#x60;smtp&#x60;, &#x60;storage&#x60;, &#x60;security&#x60;. Treat unknown keys as new checks, not errors. | 
**label** | **str** | Human-readable name for display. | 
**status** | **str** | &#x60;healthy&#x60;, &#x60;warning&#x60; or &#x60;critical&#x60;. | 
**detail** | **str** |  | 

## Example

```python
from lockally.models.tenant_health_check import TenantHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of TenantHealthCheck from a JSON string
tenant_health_check_instance = TenantHealthCheck.from_json(json)
# print the JSON string representation of the object
print(TenantHealthCheck.to_json())

# convert the object into a dict
tenant_health_check_dict = tenant_health_check_instance.to_dict()
# create an instance of TenantHealthCheck from a dict
tenant_health_check_from_dict = TenantHealthCheck.from_dict(tenant_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


