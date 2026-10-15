# UpdateResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**capacity** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from lockally.models.update_resource_request import UpdateResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResourceRequest from a JSON string
update_resource_request_instance = UpdateResourceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateResourceRequest.to_json())

# convert the object into a dict
update_resource_request_dict = update_resource_request_instance.to_dict()
# create an instance of UpdateResourceRequest from a dict
update_resource_request_from_dict = UpdateResourceRequest.from_dict(update_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


