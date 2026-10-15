# ThreadSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**subject** | **str** |  | [optional] 
**participants** | **List[str]** |  | 
**message_count** | **int** |  | 
**last_message_at** | **datetime** |  | [optional] 
**last_direction** | **str** |  | [optional] 

## Example

```python
from lockally.models.thread_summary import ThreadSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadSummary from a JSON string
thread_summary_instance = ThreadSummary.from_json(json)
# print the JSON string representation of the object
print(ThreadSummary.to_json())

# convert the object into a dict
thread_summary_dict = thread_summary_instance.to_dict()
# create an instance of ThreadSummary from a dict
thread_summary_from_dict = ThreadSummary.from_dict(thread_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


