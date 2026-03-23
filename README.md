# Salesforce Access Governance

[![CI](https://github.com/stampini81/salesforce-access-governance/actions/workflows/ci.yml/badge.svg)](https://github.com/stampini81/salesforce-access-governance/actions/workflows/ci.yml)
[![Salesforce Org Validation](https://github.com/stampini81/salesforce-access-governance/actions/workflows/salesforce-org-validation.yml/badge.svg)](https://github.com/stampini81/salesforce-access-governance/actions/workflows/salesforce-org-validation.yml)
[![Salesforce](https://img.shields.io/badge/Salesforce-Metadata%20API-00A1E0?logo=salesforce&logoColor=white)](https://developer.salesforce.com/)
[![API Version](https://img.shields.io/badge/API-v66.0-0176D3)](./sfdx-project.json)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Trailhead Superbadge](https://img.shields.io/badge/Trailhead-Access%20Governance-5e17eb)](https://trailhead.salesforce.com/)

<p align="center">
  <img src="./assets/images/salesforce-cloud.svg" alt="Salesforce logo" width="180">
</p>

<p align="center">
  <img src="./assets/images/superbadge-badge.svg" alt="Access Governance superbadge badge" width="180">
</p>

<p align="center">
  <img src="./assets/images/superbadge-completion.svg" alt="Access Governance superbadge completion" width="860">
</p>

Production-ready Salesforce DX repository that documents, preserves, and validates the implementation used to earn the **Salesforce Trailhead Superbadge: Access Governance**.

## Overview

This repository was organized to go beyond a one-off superbadge submission. It captures the maintainable metadata, the governance decisions, and the operational notes required to explain how the badge was achieved and how the solution can be reviewed over time.

The project includes:

- Salesforce metadata for access governance and monitoring controls
- GitHub Actions workflows for repository and metadata validation
- deployment-validation automation for authenticated Salesforce environments
- implementation notes for challenge-specific runtime and data steps
- repository hygiene with license, ignore rules, and reusable project structure

## Tools and Platform

- Salesforce CLI
- Salesforce DX project structure
- Salesforce Metadata API
- GitHub Actions
- Python 3.12
- Trailhead

## What Was Implemented to Earn the Superbadge

### Privileged Access Governance

- Reviewed privileged access across users, permission sets, and permission set groups.
- Corrected unauthorized privileged access in the org.
- Preserved temporary-access policy behavior instead of only stripping permissions.
- Enabled assignment expiration support for permission sets and permission set groups.
- Configured temporary privileged access with the expected expiration model.

### Opportunity Data Change Monitoring

- Enabled Opportunity history tracking.
- Enabled field history tracking for `CloseDate`, `OwnerId`, `StageName`, and `Amount`.
- Added the `Opportunity Field History` related list to Opportunity page layouts.
- Documented the report configuration required to monitor recent Opportunity history changes.

### Sensitive Data Exposure Mitigation

- Enabled the org setting that allows field history deletion.
- Created the temporary `Delete Field History` permission set.
- Assigned temporary access with a one-day expiration.
- Removed only the authorized `AccountHistory` records that exposed credit card data.

## Repository Structure

```text
.
|-- .github/
|   `-- workflows/
|-- assets/
|   `-- images/
|-- docs/
|   `-- superbadge-implementation-report.md
|-- force-app/
|   `-- main/default/
|-- manifest/
|   `-- package.xml
|-- scripts/
|   |-- check_repository.py
|   `-- validate_metadata.py
|-- .editorconfig
|-- .gitignore
|-- LICENSE
|-- README.md
`-- sfdx-project.json
```

## CI Workflows

### `ci.yml`

Runs on `push` and `pull_request` and validates:

- required repository structure
- critical project files
- Salesforce metadata XML well-formedness

### `salesforce-org-validation.yml`

Runs on `workflow_dispatch` and on pushes to `main` or `master` when the repository secret `SF_AUTH_URL` is configured.

This workflow:

- installs Salesforce CLI
- authenticates to a target org
- runs `sf project deploy validate` against the metadata in `force-app`

## Challenge Report

The full implementation record is available in [docs/superbadge-implementation-report.md](./docs/superbadge-implementation-report.md).

That report summarizes:

- privileged-access corrections
- Opportunity history-tracking configuration
- selective Account History cleanup
- operational constraints and validation notes

## Notes

Some superbadge requirements depend on runtime org state, data conditions, and UI actions that are not fully represented by deployable metadata alone. This repository intentionally combines source-tracked metadata with documentation so the deliverable remains reviewable, reproducible, and portfolio-ready.

## Author

**Leandro da Silva Stampini**

## License

This project is licensed under the [MIT License](./LICENSE).
