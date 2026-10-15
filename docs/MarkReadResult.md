# MarkReadResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **UUID** |  | [optional] 
**read** | **bool** |  | [optional] 

## Example

```python
from lockally.models.mark_read_result import MarkReadResult

# TODO update the JSON string below
json = "{}"
# create an instance of MarkReadResult from a JSON string
mark_read_result_instance = MarkReadResult.from_json(json)
# print the JSON string representation of the object
print(MarkReadResult.to_json())

# convert the object into a dict
mark_read_result_dict = mark_read_result_instance.to_dict()
# create an instance of MarkReadResult from a dict
mark_read_result_from_dict = MarkReadResult.from_dict(mark_read_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


