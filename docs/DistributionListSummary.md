# DistributionListSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**list_address** | **str** |  | 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**member_count** | **int** |  | 

## Example

```python
from lockally.models.distribution_list_summary import DistributionListSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionListSummary from a JSON string
distribution_list_summary_instance = DistributionListSummary.from_json(json)
# print the JSON string representation of the object
print(DistributionListSummary.to_json())

# convert the object into a dict
distribution_list_summary_dict = distribution_list_summary_instance.to_dict()
# create an instance of DistributionListSummary from a dict
distribution_list_summary_from_dict = DistributionListSummary.from_dict(distribution_list_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


