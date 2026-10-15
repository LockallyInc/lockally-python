# DistributionListDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**list_address** | **str** |  | 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**members** | **List[str]** |  | 
**member_count** | **int** |  | 

## Example

```python
from lockally.models.distribution_list_detail import DistributionListDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionListDetail from a JSON string
distribution_list_detail_instance = DistributionListDetail.from_json(json)
# print the JSON string representation of the object
print(DistributionListDetail.to_json())

# convert the object into a dict
distribution_list_detail_dict = distribution_list_detail_instance.to_dict()
# create an instance of DistributionListDetail from a dict
distribution_list_detail_from_dict = DistributionListDetail.from_dict(distribution_list_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


