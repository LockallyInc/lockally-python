# HealthzGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**time** | **datetime** |  | 

## Example

```python
from lockally.models.healthz_get200_response import HealthzGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HealthzGet200Response from a JSON string
healthz_get200_response_instance = HealthzGet200Response.from_json(json)
# print the JSON string representation of the object
print(HealthzGet200Response.to_json())

# convert the object into a dict
healthz_get200_response_dict = healthz_get200_response_instance.to_dict()
# create an instance of HealthzGet200Response from a dict
healthz_get200_response_from_dict = HealthzGet200Response.from_dict(healthz_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


