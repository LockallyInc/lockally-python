# MessageStatsRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivered** | **float** |  | [optional] 
**bounced** | **float** |  | [optional] 
**deferred** | **float** |  | [optional] 
**complaint** | **float** |  | [optional] 

## Example

```python
from lockally.models.message_stats_rates import MessageStatsRates

# TODO update the JSON string below
json = "{}"
# create an instance of MessageStatsRates from a JSON string
message_stats_rates_instance = MessageStatsRates.from_json(json)
# print the JSON string representation of the object
print(MessageStatsRates.to_json())

# convert the object into a dict
message_stats_rates_dict = message_stats_rates_instance.to_dict()
# create an instance of MessageStatsRates from a dict
message_stats_rates_from_dict = MessageStatsRates.from_dict(message_stats_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


