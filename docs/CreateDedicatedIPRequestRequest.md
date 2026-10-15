# CreateDedicatedIPRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | 

## Example

```python
from lockally.models.create_dedicated_ip_request_request import CreateDedicatedIPRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDedicatedIPRequestRequest from a JSON string
create_dedicated_ip_request_request_instance = CreateDedicatedIPRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDedicatedIPRequestRequest.to_json())

# convert the object into a dict
create_dedicated_ip_request_request_dict = create_dedicated_ip_request_request_instance.to_dict()
# create an instance of CreateDedicatedIPRequestRequest from a dict
create_dedicated_ip_request_request_from_dict = CreateDedicatedIPRequestRequest.from_dict(create_dedicated_ip_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


