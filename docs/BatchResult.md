# BatchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**id** | **UUID** |  | [optional] 
**message_id** | **str** |  | [optional] 
**status** | **str** | \&quot;suppressed\&quot; means every recipient of that slot was on your suppression list, and it carries no id or message_id. \&quot;delivered\&quot; only appears on a test key: the send was simulated, not transmitted. | [optional] 
**error** | **str** | Present when this message failed; the others are then absent. | [optional] 

## Example

```python
from lockally.models.batch_result import BatchResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResult from a JSON string
batch_result_instance = BatchResult.from_json(json)
# print the JSON string representation of the object
print(BatchResult.to_json())

# convert the object into a dict
batch_result_dict = batch_result_instance.to_dict()
# create an instance of BatchResult from a dict
batch_result_from_dict = BatchResult.from_dict(batch_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


