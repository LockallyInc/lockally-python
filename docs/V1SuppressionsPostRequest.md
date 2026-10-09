# V1SuppressionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**reason** | **str** |  | [optional] [default to 'manual']

## Example

```python
from lockally.models.v1_suppressions_post_request import V1SuppressionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SuppressionsPostRequest from a JSON string
v1_suppressions_post_request_instance = V1SuppressionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SuppressionsPostRequest.to_json())

# convert the object into a dict
v1_suppressions_post_request_dict = v1_suppressions_post_request_instance.to_dict()
# create an instance of V1SuppressionsPostRequest from a dict
v1_suppressions_post_request_from_dict = V1SuppressionsPostRequest.from_dict(v1_suppressions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


