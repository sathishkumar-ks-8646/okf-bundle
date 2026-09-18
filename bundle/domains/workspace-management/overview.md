---
type: API Domain
title: Workspace Management
description: "API for managing workspaces in Zoho Analytics — covering workspace operations, preferences, domain access, and folder management."
tags:
  - zoho-analytics
  - rest-api-v2
  - workspace-management
  - api-domain
api:
  domain: workspace-management
  groups:
    - group: workspace-operations
      title: Workspace Operations
      doc: "/domains/workspace-management/workspace-operations/overview.md"
      endpoint_count: 10
    - group: workspace-folders
      title: Workspace Folders
      doc: "/domains/workspace-management/workspace-folders/overview.md"
      endpoint_count: 8
    - group: workspace-preferences
      title: Workspace Preferences
      doc: "/domains/workspace-management/workspace-preferences/overview.md"
      endpoint_count: 4
    - group: domain-and-white-label
      title: Domain & White Label Access
      doc: "/domains/workspace-management/domain-and-white-label/overview.md"
      endpoint_count: 2
  endpoint_count: 24
  openapi: "/references/openapi/workspace-management-grouped-api.json"
sources:
  - id: openapi-spec
    resource: "/references/openapi/workspace-management-grouped-api.json"
    title: OpenAPI 3 specification - workspace-management-grouped-api.json
    author: team:zoho-analytics-api-docs
    last_modified: 2026-09-16T12:30:51Z
generated:
  at: 2026-09-16T12:54:00Z
status: stable
---

# Summary

API for managing workspaces in Zoho Analytics — covering workspace operations, preferences, domain access, and folder management.

# API Groups

| Group | Endpoints | Description |
|---|---|---|
| [Workspace Operations](/domains/workspace-management/workspace-operations/overview.md) | 10 | APIs that manage the lifecycle and the metadata of workspaces, covering the creation, copying, renaming, deletion and inspection of a workspace. |
| [Workspace Folders](/domains/workspace-management/workspace-folders/overview.md) | 8 | APIs that manage the folders of a workspace, covering the creation, renaming, deletion, nesting and reordering of folders, the movement of views between folders, and the selection of the default folder. |
| [Workspace Preferences](/domains/workspace-management/workspace-preferences/overview.md) | 4 | APIs that manage the workspace preferences of a user, covering the default workspace that opens on login and the favourite workspaces starred for quick access. |
| [Domain & White Label Access](/domains/workspace-management/domain-and-white-label/overview.md) | 2 | APIs that control whether a workspace is reachable through the White Label or Client Portal domain of the organization. |

# Endpoints

| Endpoint | Method | Path | Operation ID | OAuth scope | Success |
|---|---|---|---|---|---|
| [Create Workspace](/domains/workspace-management/workspace-operations/create-workspace.md) | POST | `/restapi/v2/workspaces` | `createWorkspace` | `ZohoAnalytics.modeling.create` | 200 |
| [Copy Workspace](/domains/workspace-management/workspace-operations/copy-workspace.md) | POST | `/restapi/v2/workspaces/{workspace-id}` | `copyWorkspace` | `ZohoAnalytics.modeling.create` | 200 |
| [Rename Workspace](/domains/workspace-management/workspace-operations/rename-workspace.md) | PUT | `/restapi/v2/workspaces/{workspace-id}` | `renameWorkspace` | `ZohoAnalytics.modeling.update` | 204 |
| [Delete Workspace](/domains/workspace-management/workspace-operations/delete-workspace.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}` | `deleteWorkspace` | `ZohoAnalytics.modeling.delete` | 204 |
| [Export as Template](/domains/workspace-management/workspace-operations/export-as-template.md) | GET | `/restapi/v2/workspaces/{workspace-id}/template/data` | `exportAsTemplate` | `ZohoAnalytics.metadata.read` | 200 |
| [Get All Workspace List](/domains/workspace-management/workspace-operations/get-all-workspaces.md) | GET | `/restapi/v2/workspaces` | `getAllWorkspaces` | `ZohoAnalytics.metadata.read` | 200 |
| [Get Owned Workspace List](/domains/workspace-management/workspace-operations/get-owned-workspaces.md) | GET | `/restapi/v2/workspaces/owned` | `getOwnedWorkspaces` | `ZohoAnalytics.metadata.read` | 200 |
| [Get Shared Workspace List](/domains/workspace-management/workspace-operations/get-shared-workspaces.md) | GET | `/restapi/v2/workspaces/shared` | `getSharedWorkspaces` | `ZohoAnalytics.metadata.read` | 200 |
| [Get Workspace Secret Key](/domains/workspace-management/workspace-operations/get-workspace-secret-key.md) | GET | `/restapi/v2/workspaces/{workspace-id}/secretkey` | `getWorkspaceSecretKey` | `ZohoAnalytics.metadata.read` | 200 |
| [Get Workspace Info](/domains/workspace-management/workspace-operations/get-workspace-details.md) | GET | `/restapi/v2/workspaces/{workspace-id}` | `getWorkspaceDetails` | `ZohoAnalytics.metadata.read` | 200 |
| [Get Folder List](/domains/workspace-management/workspace-folders/get-folders.md) | GET | `/restapi/v2/workspaces/{workspace-id}/folders` | `getFolders` | `ZohoAnalytics.metadata.read` | 200 |
| [Create Folder](/domains/workspace-management/workspace-folders/create-folder.md) | POST | `/restapi/v2/workspaces/{workspace-id}/folders` | `createFolder` | `ZohoAnalytics.modeling.create` | 200 |
| [Rename Folder](/domains/workspace-management/workspace-folders/rename-folder.md) | PUT | `/restapi/v2/workspaces/{workspace-id}/folders/{folder-id}` | `renameFolder` | `ZohoAnalytics.modeling.update` | 204 |
| [Delete Folder](/domains/workspace-management/workspace-folders/delete-folder.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/folders/{folder-id}` | `deleteFolder` | `ZohoAnalytics.modeling.delete` | 204 |
| [Change Folder Hierarchy](/domains/workspace-management/workspace-folders/change-folder-hierarchy.md) | PUT | `/restapi/v2/workspaces/{workspace-id}/folders/{folder-id}/move` | `changeFolderHierarchy` | `ZohoAnalytics.modeling.update` | 204 |
| [Change Folder Position](/domains/workspace-management/workspace-folders/change-folder-position.md) | PUT | `/restapi/v2/workspaces/{workspace-id}/folders/{folder-id}/reorder` | `changeFolderPosition` | `ZohoAnalytics.modeling.update` | 204 |
| [Move Views To Folder](/domains/workspace-management/workspace-folders/move-views-to-folder.md) | PUT | `/restapi/v2/workspaces/{workspace-id}/views/movetofolder` | `moveViewsToFolder` | `ZohoAnalytics.modeling.update` | 204 |
| [Make Default Folder](/domains/workspace-management/workspace-folders/make-default-folder.md) | PUT | `/restapi/v2/workspaces/{workspace-id}/folders/{folder-id}/default` | `makeDefaultFolder` | `ZohoAnalytics.modeling.update` | 204 |
| [Add Default Workspace](/domains/workspace-management/workspace-preferences/add-default-workspace.md) | POST | `/restapi/v2/workspaces/{workspace-id}/default` | `addDefaultWorkspace` | `ZohoAnalytics.metadata.update` | 204 |
| [Remove Default Workspace](/domains/workspace-management/workspace-preferences/remove-default-workspace.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/default` | `removeDefaultWorkspace` | `ZohoAnalytics.metadata.update` | 204 |
| [Add Favourite Workspace](/domains/workspace-management/workspace-preferences/add-favorite-workspace.md) | POST | `/restapi/v2/workspaces/{workspace-id}/favorite` | `addFavoriteWorkspace` | `ZohoAnalytics.metadata.update` | 204 |
| [Remove Favourite Workspace](/domains/workspace-management/workspace-preferences/remove-favorite-workspace.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/favorite` | `removeFavoriteWorkspace` | `ZohoAnalytics.metadata.update` | 204 |
| [Enable Workspace for Domain Access](/domains/workspace-management/domain-and-white-label/enable-domain-workspace.md) | POST | `/restapi/v2/workspaces/{workspace-id}/wlaccess` | `enableDomainWorkspace` | `ZohoAnalytics.metadata.update` | 204 |
| [Disable Workspace for Domain Access](/domains/workspace-management/domain-and-white-label/disable-domain-workspace.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/wlaccess` | `disableDomainWorkspace` | `ZohoAnalytics.metadata.update` | 204 |

# Related

- [All domains](/domains/index.md)
- [OpenAPI specification for this domain](/references/openapi/workspace-management-grouped-api.json)
- [Foundations](/foundations/index.md)
