# MessageStatsCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivered** | **int** |  | [optional] 
**bounced** | **int** |  | [optional] 
**deferred** | **int** |  | [optional] 
**complaint** | **int** |  | [optional] 

## Example

```python
from lockally.models.message_stats_counts import MessageStatsCounts

# TODO update the JSON string below
json = "{}"
# create an instance of MessageStatsCounts from a JSON string
message_stats_counts_instance = MessageStatsCounts.from_json(json)
# print the JSON string representation of the object
print(MessageStatsCounts.to_json())

# convert the object into a dict
message_stats_counts_dict = message_stats_counts_instance.to_dict()
# create an instance of MessageStatsCounts from a dict
message_stats_counts_from_dict = MessageStatsCounts.from_dict(message_stats_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


