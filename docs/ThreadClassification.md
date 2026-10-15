# ThreadClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **UUID** |  | 
**cached** | **bool** | True when a previous classification was reused. | [optional] 
**classification** | [**Classification**](Classification.md) |  | [optional] 

## Example

```python
from lockally.models.thread_classification import ThreadClassification

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadClassification from a JSON string
thread_classification_instance = ThreadClassification.from_json(json)
# print the JSON string representation of the object
print(ThreadClassification.to_json())

# convert the object into a dict
thread_classification_dict = thread_classification_instance.to_dict()
# create an instance of ThreadClassification from a dict
thread_classification_from_dict = ThreadClassification.from_dict(thread_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


