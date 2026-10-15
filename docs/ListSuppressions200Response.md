# ListSuppressions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Suppression]**](Suppression.md) |  | [optional] 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from lockally.models.list_suppressions200_response import ListSuppressions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSuppressions200Response from a JSON string
list_suppressions200_response_instance = ListSuppressions200Response.from_json(json)
# print the JSON string representation of the object
print(ListSuppressions200Response.to_json())

# convert the object into a dict
list_suppressions200_response_dict = list_suppressions200_response_instance.to_dict()
# create an instance of ListSuppressions200Response from a dict
list_suppressions200_response_from_dict = ListSuppressions200Response.from_dict(list_suppressions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


