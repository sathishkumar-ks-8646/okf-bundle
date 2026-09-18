---
type: SDK Example
title: SDK examples - Create Dashboard
description: "Code samples in 9 languages for POST /restapi/v2/workspaces/{workspace-id}/dashboards (createDashboard)."
resource: "https://analyticsapi.zoho.com/restapi/v2/workspaces/{workspace-id}/dashboards"
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
  operation_id: createDashboard
  method: POST
  path: "/restapi/v2/workspaces/{workspace-id}/dashboards"
  endpoint_doc: "/domains/reports-and-dashboards/dashboards/create-dashboard.md"
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
    resource: "/domains/reports-and-dashboards/dashboards/create-dashboard.md"
    title: Endpoint reference - Create Dashboard
generated:
  at: 2026-09-16T12:54:00Z
status: stable
---

# Summary

Code samples for [Create Dashboard](/domains/reports-and-dashboards/dashboards/create-dashboard.md) (`POST /restapi/v2/workspaces/{workspace-id}/dashboards`). Replace the placeholder client ID, client secret, refresh token, organization ID, workspace ID and view ID values with your own. The SDK client construction pattern for each language is explained in [SDK clients](/foundations/sdk-clients.md).

# Examples

## cURL

```bash
curl "https://analyticsapi.zoho.com/restapi/v2/workspaces/35130000001055707/dashboards" -X 'POST' -H 'ZANALYTICS-ORGID: <org-id>' -H 'Authorization: Zoho-oauthtoken <access_token>' --data-urlencode 'CONFIG={"displayName":"Sales Overview","description":"Monthly sales KPIs","layout":{"1":{"type":"VIEW","width":40,"height":20,"left":0,"top":0,"viewName":"Monthly_Sales_Chart"},"2":{"type":"USERFILTERS","width":80,"height":3,"left":0,"top":20}}}'
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

        public void CreateDashboard(IAnalyticsClient ac)
        {
            Dictionary<string, object> viewCard = new Dictionary<string, object>{{"type","VIEW"},{"width",40},{"height",20},{"left",0},{"top",0},{"viewName","Monthly_Sales_Chart"}};
            Dictionary<string, object> filterCard = new Dictionary<string, object>{{"type","USERFILTERS"},{"width",80},{"height",3},{"left",0},{"top",20}};
            Dictionary<string, object> layout = new Dictionary<string, object>{{"1",viewCard},{"2",filterCard}};
            Dictionary<string, object> config = new Dictionary<string, object>();
            config.Add("displayName", "Sales Overview");
            config.Add("description", "Monthly sales KPIs");
            config.Add("layout", layout);
            IWorkspaceAPI ws = ac.GetWorkspaceInstance(orgId, workspaceId);
            long dashboardId = ws.CreateDashboard(config);
            Console.WriteLine(dashboardId);
        }

        static void Main(string[] args)
        {
            string clientId = "1000.xxxxxxx";
            string clientSecret = "xxxxxxx";
            string refreshToken = "1000.xxxxxxx.xxxxxxx";
            IAnalyticsClient ac = new AnalyticsClient(clientId, clientSecret, refreshToken);
            Program obj = new Program();
            obj.CreateDashboard(ac);
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

func CreateDashboard(ac ZAnalytics.Client) {
    viewCard := map[string]interface{}{"type": "VIEW", "width": 40, "height": 20, "left": 0, "top": 0, "viewName": "Monthly_Sales_Chart"}
    filterCard := map[string]interface{}{"type": "USERFILTERS", "width": 80, "height": 3, "left": 0, "top": 20}
    layout := map[string]interface{}{"1": viewCard, "2": filterCard}
    config := map[string]interface{}{"displayName": "Sales Overview", "description": "Monthly sales KPIs", "layout": layout}
    workspace := ZAnalytics.GetWorkspaceInstance(&ac, orgId, workspaceId)
    dashboardId, exception := workspace.CreateDashboard(config)
    if exception != nil { fmt.Println(exception.ErrorMessage); return }
    fmt.Println(dashboardId)
}

func main() {
    ac := ZAnalytics.GetAnalyticsClient(clientId, clientSecret, refreshToken)
    CreateDashboard(ac)
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
            tObj.createDashboard(ac);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public void createDashboard(AnalyticsClient ac) throws Exception {
        JSONObject viewCard = new JSONObject();
        viewCard.put("type", "VIEW");
        viewCard.put("width", 40);
        viewCard.put("height", 20);
        viewCard.put("left", 0);
        viewCard.put("top", 0);
        viewCard.put("viewName", "Monthly_Sales_Chart");
        JSONObject filterCard = new JSONObject();
        filterCard.put("type", "USERFILTERS");
        filterCard.put("width", 80);
        filterCard.put("height", 3);
        filterCard.put("left", 0);
        filterCard.put("top", 20);
        JSONObject layout = new JSONObject();
        layout.put("1", viewCard);
        layout.put("2", filterCard);
        JSONObject config = new JSONObject();
        config.put("displayName", "Sales Overview");
        config.put("description", "Monthly sales KPIs");
        config.put("layout", layout);
        WorkspaceAPI workspace = ac.getWorkspaceInstance(orgId, workspaceId);
        long dashboardId = workspace.createDashboard(config);
        System.out.println(dashboardId);
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

    function createDashboard() {
        $view_card = ["type" => "VIEW", "width" => 40, "height" => 20, "left" => 0, "top" => 0, "viewName" => "Monthly_Sales_Chart"];
        $filter_card = ["type" => "USERFILTERS", "width" => 80, "height" => 3, "left" => 0, "top" => 20];
        $layout = ["1" => $view_card, "2" => $filter_card];
        $config = ["displayName" => "Sales Overview", "description" => "Monthly sales KPIs", "layout" => $layout];
        $workspace = $this->ac->getWorkspaceInstance($this->org_id, $this->workspace_id);
        $dashboard_id = $workspace->createDashboard($config);
        print_r($dashboard_id);
    }
}

$obj = new Test();
$obj->createDashboard();
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

    def create_dashboard(self, ac):
        view_card = {"type": "VIEW", "width": 40, "height": 20, "left": 0, "top": 0, "viewName": "Monthly_Sales_Chart"}
        filter_card = {"type": "USERFILTERS", "width": 80, "height": 3, "left": 0, "top": 20}
        layout = {"1": view_card, "2": filter_card}
        config = {"displayName": "Sales Overview", "description": "Monthly sales KPIs", "layout": layout}
        workspace = ac.get_workspace_instance(Config.ORGID, Config.WORKSPACEID)
        dashboard_id = workspace.create_dashboard(config)
        print(dashboard_id)

obj = sample()
obj.create_dashboard(obj.ac)
```

## Node.js

```javascript
var analyticsClient = require('./AnalyticsClient');
var ac = new analyticsClient('1000.xxxxxxx', 'xxxxxxx', '1000.xxxxxxx.xxxxxxx');
var orgId = '55522777';
var workspaceId = '35130000001055707';

var viewCard = { type: 'VIEW', width: 40, height: 20, left: 0, top: 0, viewName: 'Monthly_Sales_Chart' };
var filterCard = { type: 'USERFILTERS', width: 80, height: 3, left: 0, top: 20 };
var layout = { '1': viewCard, '2': filterCard };
var config = { displayName: 'Sales Overview', description: 'Monthly sales KPIs', layout: layout };
var workspace = ac.getWorkspaceInstance(orgId, workspaceId);
workspace.createDashboard(config).then((dashboardId) => { console.log(dashboardId); }).catch((error) => { console.log(error); });
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

  def create_dashboard
    view_card = { "type" => "VIEW", "width" => 40, "height" => 20, "left" => 0, "top" => 0, "viewName" => "Monthly_Sales_Chart" }
    filter_card = { "type" => "USERFILTERS", "width" => 80, "height" => 3, "left" => 0, "top" => 20 }
    layout = { "1" => view_card, "2" => filter_card }
    config = { "displayName" => "Sales Overview", "description" => "Monthly sales KPIs", "layout" => layout }
    workspace = @ac.get_workspace_instance(Config::ORGID, Config::WORKSPACEID)
    dashboard_id = workspace.create_dashboard(config)
    puts dashboard_id
  end
end

obj = Sample.new
obj.create_dashboard
```

## Deluge (Zoho scripting)

```deluge
orgId = "55522777";
workspaceId = "35130000001055707";
headersMap = Map();
headersMap.put("ZANALYTICS-ORGID", orgId);
viewCard = Map();
viewCard.put("type", "VIEW");
viewCard.put("width", 40);
viewCard.put("height", 20);
viewCard.put("left", 0);
viewCard.put("top", 0);
viewCard.put("viewName", "Monthly_Sales_Chart");
filterCard = Map();
filterCard.put("type", "USERFILTERS");
filterCard.put("width", 80);
filterCard.put("height", 3);
filterCard.put("left", 0);
filterCard.put("top", 20);
layout = Map();
layout.put("1", viewCard);
layout.put("2", filterCard);
config = Map();
config.put("displayName", "Sales Overview");
config.put("description", "Monthly sales KPIs");
config.put("layout", layout);
parameters = "CONFIG=" + zoho.encryption.urlEncode(config.toString());
response = invokeurl
[
  url :"https://analyticsapi.zoho.com/restapi/v2/workspaces/" + workspaceId + "/dashboards"
  type :POST
  parameters:parameters
  headers:headersMap
  connection:"analytics_oauth_connection"
];
info response;
```

# Related

- [Create Dashboard](/domains/reports-and-dashboards/dashboards/create-dashboard.md) - full endpoint reference.
- [Dashboards overview](/domains/reports-and-dashboards/dashboards/overview.md).
- [SDK clients](/foundations/sdk-clients.md).
