# ListDistributionLists200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DistributionListSummary]**](DistributionListSummary.md) |  | 

## Example

```python
from lockally.models.list_distribution_lists200_response import ListDistributionLists200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDistributionLists200Response from a JSON string
list_distribution_lists200_response_instance = ListDistributionLists200Response.from_json(json)
# print the JSON string representation of the object
print(ListDistributionLists200Response.to_json())

# convert the object into a dict
list_distribution_lists200_response_dict = list_distribution_lists200_response_instance.to_dict()
# create an instance of ListDistributionLists200Response from a dict
list_distribution_lists200_response_from_dict = ListDistributionLists200Response.from_dict(list_distribution_lists200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


