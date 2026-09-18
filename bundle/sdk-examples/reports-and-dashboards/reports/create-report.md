---
type: SDK Example
title: SDK examples - Create Analysis View
description: "Code samples in 9 languages for POST /restapi/v2/workspaces/{workspace-id}/reports (createReport)."
resource: "https://analyticsapi.zoho.com/restapi/v2/workspaces/{workspace-id}/reports"
tags:
  - zoho-analytics
  - sdk
  - code-sample
  - reports-and-dashboards
  - reports
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
  operation_id: createReport
  method: POST
  path: "/restapi/v2/workspaces/{workspace-id}/reports"
  endpoint_doc: "/domains/reports-and-dashboards/reports/create-report.md"
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
    resource: "/domains/reports-and-dashboards/reports/create-report.md"
    title: Endpoint reference - Create Analysis View
generated:
  at: 2026-09-16T12:54:00Z
status: stable
---

# Summary

Code samples for [Create Analysis View](/domains/reports-and-dashboards/reports/create-report.md) (`POST /restapi/v2/workspaces/{workspace-id}/reports`). Replace the placeholder client ID, client secret, refresh token, organization ID, workspace ID and view ID values with your own. The SDK client construction pattern for each language is explained in [SDK clients](/foundations/sdk-clients.md).

# Examples

## cURL

```bash
curl "https://analyticsapi.zoho.com/restapi/v2/workspaces/35130000001055707/reports" -X 'POST' -H 'ZANALYTICS-ORGID: <org-id>' -H 'Authorization: Zoho-oauthtoken <access_token>' --data-urlencode 'CONFIG={"baseTableName":"Sales","title":"New Chart","reportType":"chart","chartType":"bar","axisColumns":[{"type":"xAxis","columnName":"Date","operation":"year"},{"type":"yAxis","columnName":"Sales","operation":"sum"}]}'
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

        public void CreateReport(IAnalyticsClient ac)
        {
            Dictionary<string, object> config = new Dictionary<string, object>();
            config.Add("baseTableName", "Sales");
            config.Add("title", "New Chart");
            config.Add("reportType", "chart");
            List<Dictionary<string, object>> axisColumns = new List<Dictionary<string, object>>();
            axisColumns.Add(new Dictionary<string, object>{{"type","xAxis"},{"columnName","Date"},{"operation","year"}});
            axisColumns.Add(new Dictionary<string, object>{{"type","yAxis"},{"columnName","Sales"},{"operation","sum"}});
            config.Add("axisColumns", axisColumns);
            IWorkspaceAPI ws = ac.GetWorkspaceInstance(orgId, workspaceId);
            long viewId = ws.CreateReport(config);
            Console.WriteLine(viewId);
        }

        static void Main(string[] args)
        {
            string clientId = "1000.xxxxxxx";
            string clientSecret = "xxxxxxx";
            string refreshToken = "1000.xxxxxxx.xxxxxxx";
            IAnalyticsClient ac = new AnalyticsClient(clientId, clientSecret, refreshToken);
            Program obj = new Program();
            obj.CreateReport(ac);
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

func CreateReport(ac ZAnalytics.Client) {
    baseTableName := "Sales"
    xAxis := map[string]interface{}{"type": "xAxis", "columnName": "Date", "operation": "year"}
    yAxis := map[string]interface{}{"type": "yAxis", "columnName": "Sales", "operation": "sum"}
    axisColumns := []map[string]interface{}{xAxis, yAxis}
    config := map[string]interface{}{"baseTableName": baseTableName, "title": "New Chart", "reportType": "chart", "axisColumns": axisColumns}
    workspace := ZAnalytics.GetWorkspaceInstance(&ac, orgId, workspaceId)
    viewId, exception := workspace.CreateReport(config)
    if exception != nil { fmt.Println(exception.ErrorMessage); return }
    fmt.Println(viewId)
}

func main() {
    ac := ZAnalytics.GetAnalyticsClient(clientId, clientSecret, refreshToken)
    CreateReport(ac)
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
            tObj.createReport(ac);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public void createReport(AnalyticsClient ac) throws Exception {
        String baseTableName = "Sales";
        JSONObject xAxis = new JSONObject();
        xAxis.put("type", "xAxis");
        xAxis.put("columnName", "Date");
        xAxis.put("operation", "year");
        JSONObject yAxis = new JSONObject();
        yAxis.put("type", "yAxis");
        yAxis.put("columnName", "Sales");
        yAxis.put("operation", "sum");
        JSONArray axisColumns = new JSONArray();
        axisColumns.put(xAxis);
        axisColumns.put(yAxis);
        JSONObject config = new JSONObject();
        config.put("baseTableName", baseTableName);
        config.put("title", "New Chart");
        config.put("reportType", "chart");
        config.put("axisColumns", axisColumns);
        WorkspaceAPI workspace = ac.getWorkspaceInstance(orgId, workspaceId);
        long viewId = workspace.createReport(config);
        System.out.println(viewId);
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

    function createReport() {
        $base_table_name = "Sales";
        $x_axis = ["type" => "xAxis", "columnName" => "Date", "operation" => "year"];
        $y_axis = ["type" => "yAxis", "columnName" => "Sales", "operation" => "sum"];
        $axis_columns = [$x_axis, $y_axis];
        $config = ["baseTableName" => $base_table_name, "title" => "New Chart", "reportType" => "chart", "axisColumns" => $axis_columns];
        $workspace = $this->ac->getWorkspaceInstance($this->org_id, $this->workspace_id);
        $view_id = $workspace->createReport($config);
        print_r($view_id);
    }
}

$obj = new Test();
$obj->createReport();
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

    def create_report(self, ac):
        base_table_name = "Sales"
        xaxis = {"type": "xAxis", "columnName": "Date", "operation": "year"}
        yaxis = {"type": "yAxis", "columnName": "Sales", "operation": "sum"}
        axis_columns = [xaxis, yaxis]
        config = {"baseTableName": base_table_name, "title": "New Chart", "reportType": "chart", "axisColumns": axis_columns}
        workspace = ac.get_workspace_instance(Config.ORGID, Config.WORKSPACEID)
        view_id = workspace.create_report(config)
        print(view_id)

obj = sample()
obj.create_report(obj.ac)
```

## Node.js

```javascript
var analyticsClient = require('./AnalyticsClient');
var ac = new analyticsClient('1000.xxxxxxx', 'xxxxxxx', '1000.xxxxxxx.xxxxxxx');
var orgId = '55522777';
var workspaceId = '35130000001055707';

var baseTableName = 'Sales';
var xAxis = { type: 'xAxis', columnName: 'Date', operation: 'year' };
var yAxis = { type: 'yAxis', columnName: 'Sales', operation: 'sum' };
var axisColumns = [xAxis, yAxis];
var config = { baseTableName: baseTableName, title: 'New Chart', reportType: 'chart', axisColumns: axisColumns };
var workspace = ac.getWorkspaceInstance(orgId, workspaceId);
workspace.createReport(config).then((viewId) => { console.log(viewId); }).catch((error) => { console.log(error); });
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

  def create_report
    base_table_name = "Sales"
    xaxis = { "type" => "xAxis", "columnName" => "Date", "operation" => "year" }
    yaxis = { "type" => "yAxis", "columnName" => "Sales", "operation" => "sum" }
    axis_columns = [xaxis, yaxis]
    config = { "baseTableName" => base_table_name, "title" => "New Chart", "reportType" => "chart", "axisColumns" => axis_columns }
    workspace = @ac.get_workspace_instance(Config::ORGID, Config::WORKSPACEID)
    view_id = workspace.create_report(config)
    puts view_id
  end
end

obj = Sample.new
obj.create_report
```

## Deluge (Zoho scripting)

```deluge
orgId = "55522777";
workspaceId = "35130000001055707";
headersMap = Map();
headersMap.put("ZANALYTICS-ORGID", orgId);
config = Map();
config.put("baseTableName", "Sales");
config.put("title", "New Chart");
config.put("reportType", "chart");
parameters = "CONFIG=" + zoho.encryption.urlEncode(config.toString());
response = invokeurl
[
  url :"https://analyticsapi.zoho.com/restapi/v2/workspaces/" + workspaceId + "/reports"
  type :POST
  parameters:parameters
  headers:headersMap
  connection:"analytics_oauth_connection"
];
info response;
```

# Related

- [Create Analysis View](/domains/reports-and-dashboards/reports/create-report.md) - full endpoint reference.
- [Reports (Analysis Views) overview](/domains/reports-and-dashboards/reports/overview.md).
- [SDK clients](/foundations/sdk-clients.md).
