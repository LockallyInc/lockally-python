# ThreadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox** | **str** |  | 
**threads** | [**List[ThreadSummary]**](ThreadSummary.md) |  | 

## Example

```python
from lockally.models.thread_list import ThreadList

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadList from a JSON string
thread_list_instance = ThreadList.from_json(json)
# print the JSON string representation of the object
print(ThreadList.to_json())

# convert the object into a dict
thread_list_dict = thread_list_instance.to_dict()
# create an instance of ThreadList from a dict
thread_list_from_dict = ThreadList.from_dict(thread_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


