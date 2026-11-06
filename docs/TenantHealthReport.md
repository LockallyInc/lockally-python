# TenantHealthReport

The workspace health snapshot behind the console dashboard. DNS checks are live lookups, so a domain whose DNS cannot be read shows as a warning rather than an error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_score** | **int** |  | 
**checks** | [**List[TenantHealthCheck]**](TenantHealthCheck.md) |  | 
**generated_at** | **datetime** |  | 

## Example

```python
from lockally.models.tenant_health_report import TenantHealthReport

# TODO update the JSON string below
json = "{}"
# create an instance of TenantHealthReport from a JSON string
tenant_health_report_instance = TenantHealthReport.from_json(json)
# print the JSON string representation of the object
print(TenantHealthReport.to_json())

# convert the object into a dict
tenant_health_report_dict = tenant_health_report_instance.to_dict()
# create an instance of TenantHealthReport from a dict
tenant_health_report_from_dict = TenantHealthReport.from_dict(tenant_health_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


