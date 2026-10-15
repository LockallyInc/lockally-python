# CreateDistributionListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_address** | **str** |  | 
**name** | **str** |  | [optional] 
**members** | **List[str]** |  | [optional] 

## Example

```python
from lockally.models.create_distribution_list_request import CreateDistributionListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDistributionListRequest from a JSON string
create_distribution_list_request_instance = CreateDistributionListRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDistributionListRequest.to_json())

# convert the object into a dict
create_distribution_list_request_dict = create_distribution_list_request_instance.to_dict()
# create an instance of CreateDistributionListRequest from a dict
create_distribution_list_request_from_dict = CreateDistributionListRequest.from_dict(create_distribution_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


