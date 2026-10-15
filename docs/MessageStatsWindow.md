# MessageStatsWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | [optional] 
**to** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.message_stats_window import MessageStatsWindow

# TODO update the JSON string below
json = "{}"
# create an instance of MessageStatsWindow from a JSON string
message_stats_window_instance = MessageStatsWindow.from_json(json)
# print the JSON string representation of the object
print(MessageStatsWindow.to_json())

# convert the object into a dict
message_stats_window_dict = message_stats_window_instance.to_dict()
# create an instance of MessageStatsWindow from a dict
message_stats_window_from_dict = MessageStatsWindow.from_dict(message_stats_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


