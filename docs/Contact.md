# Contact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**contact_type** | **str** |  | 
**source** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**external_system** | **str** | The system that owns this contact&#39;s external id. Absent on contacts made by hand. | [optional] 
**external_id** | **str** | The contact&#39;s id in &#x60;external_system&#x60;. Absent on contacts made by hand. | [optional] 

## Example

```python
from lockally.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print(Contact.to_json())

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_from_dict = Contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


