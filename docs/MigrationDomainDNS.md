# MigrationDomainDNS

Each record is `healthy`, `warning` or `critical`, or empty when it could not be checked.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**mx** | **str** |  | 
**spf** | **str** |  | 
**dkim** | **str** |  | 
**dmarc** | **str** |  | 

## Example

```python
from lockally.models.migration_domain_dns import MigrationDomainDNS

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationDomainDNS from a JSON string
migration_domain_dns_instance = MigrationDomainDNS.from_json(json)
# print the JSON string representation of the object
print(MigrationDomainDNS.to_json())

# convert the object into a dict
migration_domain_dns_dict = migration_domain_dns_instance.to_dict()
# create an instance of MigrationDomainDNS from a dict
migration_domain_dns_from_dict = MigrationDomainDNS.from_dict(migration_domain_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


