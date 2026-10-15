# DedicatedIPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**status** | **str** |  | 
**note** | **str** |  | [optional] 
**admin_note** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**resolved_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.dedicated_ip_request import DedicatedIPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedIPRequest from a JSON string
dedicated_ip_request_instance = DedicatedIPRequest.from_json(json)
# print the JSON string representation of the object
print(DedicatedIPRequest.to_json())

# convert the object into a dict
dedicated_ip_request_dict = dedicated_ip_request_instance.to_dict()
# create an instance of DedicatedIPRequest from a dict
dedicated_ip_request_from_dict = DedicatedIPRequest.from_dict(dedicated_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


