---
type: SDK Example
title: SDK examples - Update Dashboard
description: "Code samples in 9 languages for PUT /restapi/v2/workspaces/{workspace-id}/dashboards/{dashboard-id} (updateDashboard)."
resource: "https://analyticsapi.zoho.com/restapi/v2/workspaces/{workspace-id}/dashboards/{dashboard-id}"
tags:
  - zoho-analytics
  - sdk
  - code-sample
  - reports-and-dashboards
  - dashboards
  - bash
  - csharp
  - go
  - java
  - php
  - python
  - javascript
  - ruby
  - deluge
api:
  operation_id: updateDashboard
  method: PUT
  path: "/restapi/v2/workspaces/{workspace-id}/dashboards/{dashboard-id}"
  endpoint_doc: "/domains/reports-and-dashboards/dashboards/update-dashboard.md"
  languages:
    - cURL
    - "C#"
    - Go
    - Java
    - PHP
    - Python
    - Node.js
    - Ruby
    - Deluge (Zoho scripting)
sources:
  - id: openapi-spec
    resource: "/references/openapi/reports-dashboards-grouped-api.json"
    title: OpenAPI 3 specification - reports-dashboards-grouped-api.json
    author: team:zoho-analytics-api-docs
    last_modified: 2026-09-16T12:30:51Z
  - id: endpoint-doc
    resource: "/domains/reports-and-dashboards/dashboards/update-dashboard.md"
    title: Endpoint reference - Update Dashboard
generated:
  at: 2026-09-16T12:54:00Z
status: stable
---

# Summary

Code samples for [Update Dashboard](/domains/reports-and-dashboards/dashboards/update-dashboard.md) (`PUT /restapi/v2/workspaces/{workspace-id}/dashboards/{dashboard-id}`). Replace the placeholder client ID, client secret, refresh token, organization ID, workspace ID and view ID values with your own. The SDK client construction pattern for each language is explained in [SDK clients](/foundations/sdk-clients.md).

# Examples

## cURL

```bash
curl "https://analyticsapi.zoho.com/restapi/v2/workspaces/35130000001055707/dashboards/35130000001055801" -X 'PUT' -H 'ZANALYTICS-ORGID: <org-id>' -H 'Authorization: Zoho-oauthtoken <access_token>' --data-urlencode 'CONFIG={"settings":{"enableGlobalUF":"true","reportAsFilter":"true","fitToWidth":"false","allowExport":{"pdf":"false","excel":"true","csv":"true","html":"false"}}}'
```

## C#

```csharp
using System;
using System.Collections.Generic;
using System.Text.Json;
using ZohoAnalytics;

namespace ZohoAnalyticsTest
{
    class Program
    {
        long orgId = 55522777;
        long workspaceId = 35130000001055707;

        public void UpdateDashboard(IAnalyticsClient ac)
        {
            long dashboardId = 35130000001055801L;
            Dictionary<string, object> allowExport = new Dictionary<string, object>{{"pdf","false"},{"excel","true"},{"csv","true"},{"html","false"}};
            Dictionary<string, object> settings = new Dictionary<string, object>();
            settings.Add("enableGlobalUF", "true");
            settings.Add("reportAsFilter", "true");
            settings.Add("fitToWidth", "false");
            settings.Add("allowExport", allowExport);
            Dictionary<string, object> config = new Dictionary<string, object>();
            config.Add("settings", settings);
            IWorkspaceAPI ws = ac.GetWorkspaceInstance(orgId, workspaceId);
            ws.UpdateDashboard(dashboardId, config);
            Console.WriteLine("Success");
        }

        static void Main(string[] args)
        {
            string clientId = "1000.xxxxxxx";
            string clientSecret = "xxxxxxx";
            string refreshToken = "1000.xxxxxxx.xxxxxxx";
            IAnalyticsClient ac = new AnalyticsClient(clientId, clientSecret, refreshToken);
            Program obj = new Program();
            obj.UpdateDashboard(ac);
        }
    }
}
```

## Go

```go
package main

import (
    "fmt"
    ZAnalytics "zoho/pkg/analyticsclient"
)

var (
    clientId = "1000.xxxxxxx"
    clientSecret = "xxxxxxx"
    refreshToken = "1000.xxxxxxx.xxxxxxx"
    orgId = "55522777"
    workspaceId = "35130000001055707"
)

func UpdateDashboard(ac ZAnalytics.Client) {
    dashboardId := "35130000001055801"
    allowExport := map[string]interface{}{"pdf": "false", "excel": "true", "csv": "true", "html": "false"}
    settings := map[string]interface{}{"enableGlobalUF": "true", "reportAsFilter": "true", "fitToWidth": "false", "allowExport": allowExport}
    config := map[string]interface{}{"settings": settings}
    workspace := ZAnalytics.GetWorkspaceInstance(&ac, orgId, workspaceId)
    exception := workspace.UpdateDashboard(dashboardId, config)
    if exception != nil { fmt.Println(exception.ErrorMessage); return }
    fmt.Println("Success")
}

func main() {
    ac := ZAnalytics.GetAnalyticsClient(clientId, clientSecret, refreshToken)
    UpdateDashboard(ac)
}
```

## Java

```java
import com.zoho.analytics.client.*;
import org.json.*;

public class Test {
    private long orgId = 55522777l;
    private long workspaceId = 35130000001055707l;

    public static void main(String args[]) {
        String clientId = "1000.xxxxxxx";
        String clientSecret = "xxxxxxx";
        String refreshToken = "1000.xxxxxxx.xxxxxxx";
        Test tObj = new Test();
        AnalyticsClient ac = new AnalyticsClient(clientId, clientSecret, refreshToken);
        try {
            tObj.updateDashboard(ac);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public void updateDashboard(AnalyticsClient ac) throws Exception {
        long dashboardId = 35130000001055801l;
        JSONObject allowExport = new JSONObject();
        allowExport.put("pdf", "false");
        allowExport.put("excel", "true");
        allowExport.put("csv", "true");
        allowExport.put("html", "false");
        JSONObject settings = new JSONObject();
        settings.put("enableGlobalUF", "true");
        settings.put("reportAsFilter", "true");
        settings.put("fitToWidth", "false");
        settings.put("allowExport", allowExport);
        JSONObject config = new JSONObject();
        config.put("settings", settings);
        WorkspaceAPI workspace = ac.getWorkspaceInstance(orgId, workspaceId);
        workspace.updateDashboard(dashboardId, config);
        System.out.println("success");
    }
}
```

## PHP

```php
<?php
require 'AnalyticsClient.php';

class Test {
    public $ac;
    public $org_id = "55522777";
    public $workspace_id = "35130000001055707";
    function __construct() {
        $this->ac = new AnalyticsClient("1000.xxxxxxx", "xxxxxxx", "1000.xxxxxxx.xxxxxxx");
    }

    function updateDashboard() {
        $dashboard_id = "35130000001055801";
        $allow_export = ["pdf" => "false", "excel" => "true", "csv" => "true", "html" => "false"];
        $settings = ["enableGlobalUF" => "true", "reportAsFilter" => "true", "fitToWidth" => "false", "allowExport" => $allow_export];
        $config = ["settings" => $settings];
        $workspace = $this->ac->getWorkspaceInstance($this->org_id, $this->workspace_id);
        $workspace->updateDashboard($dashboard_id, $config);
        echo "success";
    }
}

$obj = new Test();
$obj->updateDashboard();
?>
```

## Python

```python
from AnalyticsClient import AnalyticsClient

class Config:
    CLIENTID = "1000.xxxxxxx"
    CLIENTSECRET = "xxxxxxx"
    REFRESHTOKEN = "1000.xxxxxxx.xxxxxxx"
    ORGID = "55522777"
    WORKSPACEID = "35130000001055707"

class sample:
    ac = AnalyticsClient(Config.CLIENTID, Config.CLIENTSECRET, Config.REFRESHTOKEN)

    def update_dashboard(self, ac):
        dashboard_id = "35130000001055801"
        allow_export = {"pdf": "false", "excel": "true", "csv": "true", "html": "false"}
        settings = {"enableGlobalUF": "true", "reportAsFilter": "true", "fitToWidth": "false", "allowExport": allow_export}
        config = {"settings": settings}
        workspace = ac.get_workspace_instance(Config.ORGID, Config.WORKSPACEID)
        workspace.update_dashboard(dashboard_id, config)
        print("success")

obj = sample()
obj.update_dashboard(obj.ac)
```

## Node.js

```javascript
var analyticsClient = require('./AnalyticsClient');
var ac = new analyticsClient('1000.xxxxxxx', 'xxxxxxx', '1000.xxxxxxx.xxxxxxx');
var orgId = '55522777';
var workspaceId = '35130000001055707';

var dashboardId = '35130000001055801';
var allowExport = { pdf: 'false', excel: 'true', csv: 'true', html: 'false' };
var settings = { enableGlobalUF: 'true', reportAsFilter: 'true', fitToWidth: 'false', allowExport: allowExport };
var config = { settings: settings };
var workspace = ac.getWorkspaceInstance(orgId, workspaceId);
workspace.updateDashboard(dashboardId, config).then(() => { console.log('success'); }).catch((error) => { console.log(error); });
```

## Ruby

```ruby
require 'zoho_analytics_client'

class Config
  ORGID = "55522777"
  WORKSPACEID = "35130000001055707"
end

class Sample
  def initialize
    @ac = AnalyticsClient.new.with_data_center("US").with_oauth({
      "clientId" => "1000.xxxxxxx",
      "clientSecret" => "xxxxxxx",
      "refreshToken" => "1000.xxxxxxx.xxxxxxx"
    }).build
  end

  def update_dashboard
    dashboard_id = "35130000001055801"
    allow_export = { "pdf" => "false", "excel" => "true", "csv" => "true", "html" => "false" }
    settings = { "enableGlobalUF" => "true", "reportAsFilter" => "true", "fitToWidth" => "false", "allowExport" => allow_export }
    config = { "settings" => settings }
    workspace = @ac.get_workspace_instance(Config::ORGID, Config::WORKSPACEID)
    workspace.update_dashboard(dashboard_id, config)
    puts "success"
  end
end

obj = Sample.new
obj.update_dashboard
```

## Deluge (Zoho scripting)

```deluge
orgId = "55522777";
workspaceId = "35130000001055707";
dashboardId = "35130000001055801";
headersMap = Map();
headersMap.put("ZANALYTICS-ORGID", orgId);
allowExport = Map();
allowExport.put("pdf", "false");
allowExport.put("excel", "true");
allowExport.put("csv", "true");
allowExport.put("html", "false");
settings = Map();
settings.put("enableGlobalUF", "true");
settings.put("reportAsFilter", "true");
settings.put("fitToWidth", "false");
settings.put("allowExport", allowExport);
config = Map();
config.put("settings", settings);
parameters = "CONFIG=" + zoho.encryption.urlEncode(config.toString());
invokeurl
[
  url :"https://analyticsapi.zoho.com/restapi/v2/workspaces/" + workspaceId + "/dashboards/" + dashboardId
  type :PUT
  parameters:parameters
  headers:headersMap
  connection:"analytics_oauth_connection"
];
info "success";
```

# Related

- [Update Dashboard](/domains/reports-and-dashboards/dashboards/update-dashboard.md) - full endpoint reference.
- [Dashboards overview](/domains/reports-and-dashboards/dashboards/overview.md).
- [SDK clients](/foundations/sdk-clients.md).
