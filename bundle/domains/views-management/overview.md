---
type: API Domain
title: Views Management
description: "API for Views Management in Zoho Analytics — covering view operations, auto analysis, favorites, and trash management."
tags:
  - zoho-analytics
  - rest-api-v2
  - views-management
  - api-domain
api:
  domain: views-management
  groups:
    - group: view-operations
      title: View Operations
      doc: "/domains/views-management/view-operations/overview.md"
      endpoint_count: 10
    - group: view-preferences
      title: View Preferences
      doc: "/domains/views-management/view-preferences/overview.md"
      endpoint_count: 2
    - group: trash-management
      title: Trash Management
      doc: "/domains/views-management/trash-management/overview.md"
      endpoint_count: 3
    - group: auto-analysis
      title: Auto Analysis
      doc: "/domains/views-management/auto-analysis/overview.md"
      endpoint_count: 2
    - group: tags
      title: Tags
      doc: "/domains/views-management/tags/overview.md"
      endpoint_count: 10
  endpoint_count: 27
  openapi: "/references/openapi/views-management-grouped-api.json"
sources:
  - id: openapi-spec
    resource: "/references/openapi/views-management-grouped-api.json"
    title: OpenAPI 3 specification - views-management-grouped-api.json
    author: team:zoho-analytics-api-docs
    last_modified: 2026-09-16T12:30:51Z
generated:
  at: 2026-09-16T12:54:00Z
status: stable
---

# Summary

API for Views Management in Zoho Analytics — covering view operations, auto analysis, favorites, and trash management.

# API Groups

| Group | Endpoints | Description |
|---|---|---|
| [View Operations](/domains/views-management/view-operations/overview.md) | 10 | APIs for creating, copying, renaming, deleting, and retrieving views. |
| [View Preferences](/domains/views-management/view-preferences/overview.md) | 2 | APIs to mark a view as a favorite for the authenticated user and to remove it from the favorites list. |
| [Trash Management](/domains/views-management/trash-management/overview.md) | 3 | APIs to list the views available in the trash of a workspace, restore a trashed view back to the workspace, and permanently delete a view from the trash. |
| [Auto Analysis](/domains/views-management/auto-analysis/overview.md) | 2 | APIs to automatically generate a curated set of views - charts, pivot tables and summary views - from an entire table or from a single column of it. |
| [Tags](/domains/views-management/tags/overview.md) | 10 | APIs to create, update, delete and list the tags of a workspace, and to attach those tags to views. |

# Endpoints

| Endpoint | Method | Path | Operation ID | OAuth scope | Success |
|---|---|---|---|---|---|
| [Save As View](/domains/views-management/view-operations/save-as-view.md) | POST | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/saveas` | `saveAsView` | `ZohoAnalytics.modeling.create` | 200 |
| [Copy Views](/domains/views-management/view-operations/copy-views.md) | POST | `/restapi/v2/workspaces/{workspace-id}/views/copy` | `copyViews` | `ZohoAnalytics.modeling.create` | 200 |
| [Create Similar Views](/domains/views-management/view-operations/create-similar-views.md) | POST | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/similarviews` | `createSimilarViews` | `ZohoAnalytics.modeling.create` | 204 |
| [Rename View](/domains/views-management/view-operations/rename-view.md) | PUT | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}` | `renameView` | `ZohoAnalytics.modeling.update` | 204 |
| [Delete View](/domains/views-management/view-operations/delete-view.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}` | `deleteView` | `ZohoAnalytics.modeling.delete` | 204 |
| [Get View List](/domains/views-management/view-operations/get-views.md) | GET | `/restapi/v2/workspaces/{workspace-id}/views` | `getViews` | `ZohoAnalytics.metadata.read` | 200 |
| [Get View Details](/domains/views-management/view-operations/get-view-details.md) | GET | `/restapi/v2/views/{view-id}` | `getViewDetails` | `ZohoAnalytics.metadata.read` | 200 |
| [Get View URL](/domains/views-management/view-operations/get-view-url.md) | GET | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/publish` | `getViewUrl` | `ZohoAnalytics.embed.read` | 200 |
| [Get View Dependents](/domains/views-management/view-operations/get-view-dependents.md) | GET | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/dependents` | `getViewDependents` | `ZohoAnalytics.metadata.read` | 200 |
| [Get Recent Views](/domains/views-management/view-operations/get-recent-views.md) | GET | `/restapi/v2/recentviews` | `getRecentViews` | `ZohoAnalytics.metadata.read` | 200 |
| [Add Favourite View](/domains/views-management/view-preferences/add-favorite-view.md) | POST | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/favorite` | `addFavoriteView` | `ZohoAnalytics.metadata.update` | 204 |
| [Remove Favourite View](/domains/views-management/view-preferences/remove-favorite-view.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/favorite` | `removeFavoriteView` | `ZohoAnalytics.metadata.update` | 204 |
| [Get Trash Views](/domains/views-management/trash-management/get-trash-views.md) | GET | `/restapi/v2/workspaces/{workspace-id}/trash` | `getTrashViews` | `ZohoAnalytics.metadata.read` | 200 |
| [Restore Trash View](/domains/views-management/trash-management/restore-trash-view.md) | POST | `/restapi/v2/workspaces/{workspace-id}/trash/{view-id}` | `restoreTrashView` | `ZohoAnalytics.modeling.create` | 204 |
| [Delete Trash View](/domains/views-management/trash-management/delete-trash-view.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/trash/{view-id}` | `deleteTrashView` | `ZohoAnalytics.modeling.delete` | 204 |
| [Auto Analyse View](/domains/views-management/auto-analysis/auto-analyse-view.md) | POST | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/autoanalyse` | `autoAnalyseView` | `ZohoAnalytics.modeling.create` | 200 |
| [Auto Analyse Column](/domains/views-management/auto-analysis/auto-analyse-column.md) | POST | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/columns/{column-id}/autoanalyse` | `autoAnalyseColumn` | `ZohoAnalytics.modeling.create` | 200 |
| [Get Tags List](/domains/views-management/tags/get-tags.md) | GET | `/restapi/v2/workspaces/{workspace-id}/tags` | `getTags` | `ZohoAnalytics.metadata.read` | 200 |
| [Get Tagged Views](/domains/views-management/tags/get-tagged-views.md) | GET | `/restapi/v2/workspaces/{workspace-id}/tags/{tag-id}/views` | `getTaggedViews` | `ZohoAnalytics.metadata.read` | 200 |
| [Get View Tags](/domains/views-management/tags/get-view-tags.md) | GET | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/tags` | `getViewTags` | `ZohoAnalytics.metadata.read` | 200 |
| [Create Tag](/domains/views-management/tags/create-tag.md) | POST | `/restapi/v2/workspaces/{workspace-id}/tags` | `createTag` | `ZohoAnalytics.modeling.create` | 200 |
| [Update Tag](/domains/views-management/tags/update-tag.md) | PUT | `/restapi/v2/workspaces/{workspace-id}/tags/{tag-id}` | `updateTag` | `ZohoAnalytics.modeling.update` | 204 |
| [Delete Tag](/domains/views-management/tags/delete-tag.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/tags/{tag-id}` | `deleteTag` | `ZohoAnalytics.modeling.delete` | 204 |
| [Add Tag To Multiple Views](/domains/views-management/tags/add-tag-to-views.md) | POST | `/restapi/v2/workspaces/{workspace-id}/tags/{tag-id}/views` | `addTagToViews` | `ZohoAnalytics.modeling.create` | 204 |
| [Remove Tag From Multiple Views](/domains/views-management/tags/remove-tag-from-views.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/tags/{tag-id}/views` | `removeTagFromViews` | `ZohoAnalytics.modeling.delete` | 204 |
| [Add Multiple Tags To View](/domains/views-management/tags/add-tags-to-view.md) | POST | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/tags` | `addTagsToView` | `ZohoAnalytics.modeling.create` | 204 |
| [Remove Multiple Tags From View](/domains/views-management/tags/remove-tags-from-view.md) | DELETE | `/restapi/v2/workspaces/{workspace-id}/views/{view-id}/tags` | `removeTagsFromView` | `ZohoAnalytics.modeling.delete` | 204 |

# Related

- [All domains](/domains/index.md)
- [OpenAPI specification for this domain](/references/openapi/views-management-grouped-api.json)
- [Foundations](/foundations/index.md)
