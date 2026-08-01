# ReplaceDistributionListMembersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** |  | 

## Example

```python
from lockally.models.replace_distribution_list_members_request import ReplaceDistributionListMembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceDistributionListMembersRequest from a JSON string
replace_distribution_list_members_request_instance = ReplaceDistributionListMembersRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceDistributionListMembersRequest.to_json())

# convert the object into a dict
replace_distribution_list_members_request_dict = replace_distribution_list_members_request_instance.to_dict()
# create an instance of ReplaceDistributionListMembersRequest from a dict
replace_distribution_list_members_request_from_dict = ReplaceDistributionListMembersRequest.from_dict(replace_distribution_list_members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


