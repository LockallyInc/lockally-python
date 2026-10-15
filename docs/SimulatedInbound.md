# SimulatedInbound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **UUID** |  | [optional] 
**message_id** | **UUID** |  | [optional] 
**annotations** | [**Annotations**](Annotations.md) |  | [optional] 

## Example

```python
from lockally.models.simulated_inbound import SimulatedInbound

# TODO update the JSON string below
json = "{}"
# create an instance of SimulatedInbound from a JSON string
simulated_inbound_instance = SimulatedInbound.from_json(json)
# print the JSON string representation of the object
print(SimulatedInbound.to_json())

# convert the object into a dict
simulated_inbound_dict = simulated_inbound_instance.to_dict()
# create an instance of SimulatedInbound from a dict
simulated_inbound_from_dict = SimulatedInbound.from_dict(simulated_inbound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


