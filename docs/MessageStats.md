# MessageStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window** | [**MessageStatsWindow**](MessageStatsWindow.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**sent** | **int** |  | [optional] 
**counts** | [**MessageStatsCounts**](MessageStatsCounts.md) |  | [optional] 
**rates** | [**MessageStatsRates**](MessageStatsRates.md) |  | [optional] 

## Example

```python
from lockally.models.message_stats import MessageStats

# TODO update the JSON string below
json = "{}"
# create an instance of MessageStats from a JSON string
message_stats_instance = MessageStats.from_json(json)
# print the JSON string representation of the object
print(MessageStats.to_json())

# convert the object into a dict
message_stats_dict = message_stats_instance.to_dict()
# create an instance of MessageStats from a dict
message_stats_from_dict = MessageStats.from_dict(message_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


