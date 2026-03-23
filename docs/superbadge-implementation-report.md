# Superbadge Implementation Report

## Scope

This repository records the metadata, governance configuration, and operational actions used to complete the Salesforce Trailhead **Superbadge: Access Governance** in a dedicated Developer Edition org.

## Implementation Summary

### 1. Privileged access governance

- Reviewed privileged access across users, permission sets, and permission set groups.
- Corrected access that exceeded the principle of least privilege.
- Preserved the temporary-access operating model required by the challenge instead of removing all elevated access indiscriminately.
- Configured Rahul Patel's temporary `Customize Application` access with a 30-day expiration.
- Corrected the `PERSONA_Sales_Representative` permission set group so it no longer grants unauthorized delete access on Opportunities.
- Enabled assignment expiration support for permission sets and permission set groups through `UserManagementSettings`.

### 2. Opportunity data change monitoring

- Enabled Opportunity history tracking at the object level.
- Enabled field history tracking for:
  - `CloseDate`
  - `OwnerId`
  - `StageName`
  - `Amount`
- Added the Opportunity history-related list configuration required for page-level visibility.
- Created the supporting report folder and documented the report setup used for recent Opportunity field-history review.

### 3. Sensitive history cleanup

- Enabled the org setting that allows field history deletion.
- Created the temporary `Delete Field History` permission set.
- Assigned the permission temporarily with a one-day expiration.
- Rebuilt and verified the expected `AccountHistory` sequence for the target account where necessary.
- Deleted only the authorized history records containing exposed credit card data and preserved the remaining audit trail.

## Metadata Captured in This Repository

- `force-app/main/default/objects/Opportunity`
- `force-app/main/default/layouts`
- `force-app/main/default/permissionsets`
- `force-app/main/default/settings`
- `manifest/package.xml`

## Operational Constraints

- Some challenge checks depend on runtime data and UI state, not only deployable metadata.
- The Opportunity related-list step can require manual layout confirmation depending on org behavior.
- The selective history-deletion step depends on exact `AccountHistory` record values and therefore required controlled execution.

## Repository Quality Controls

- XML well-formedness validation for Salesforce metadata
- repository structure validation
- GitHub Actions CI workflow
- optional GitHub Actions Salesforce org validation workflow for authenticated environments

## Author

**Leandro da Silva Stampini**
