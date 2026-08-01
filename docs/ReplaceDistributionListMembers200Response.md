# ReplaceDistributionListMembers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**list_address** | **str** |  | 
**members** | **List[str]** |  | 
**member_count** | **int** |  | 

## Example

```python
from lockally.models.replace_distribution_list_members200_response import ReplaceDistributionListMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceDistributionListMembers200Response from a JSON string
replace_distribution_list_members200_response_instance = ReplaceDistributionListMembers200Response.from_json(json)
# print the JSON string representation of the object
print(ReplaceDistributionListMembers200Response.to_json())

# convert the object into a dict
replace_distribution_list_members200_response_dict = replace_distribution_list_members200_response_instance.to_dict()
# create an instance of ReplaceDistributionListMembers200Response from a dict
replace_distribution_list_members200_response_from_dict = ReplaceDistributionListMembers200Response.from_dict(replace_distribution_list_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


