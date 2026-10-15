# CreateSuppressionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**reason** | **str** |  | [optional] [default to 'manual']

## Example

```python
from lockally.models.create_suppression_request import CreateSuppressionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSuppressionRequest from a JSON string
create_suppression_request_instance = CreateSuppressionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSuppressionRequest.to_json())

# convert the object into a dict
create_suppression_request_dict = create_suppression_request_instance.to_dict()
# create an instance of CreateSuppressionRequest from a dict
create_suppression_request_from_dict = CreateSuppressionRequest.from_dict(create_suppression_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


