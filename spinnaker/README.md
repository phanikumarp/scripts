Check wiki [pages](https://github.com/OpsMx/scripts/wiki) also
#### How to run `autopipeline.jar`?
1. Run `java -jar autopipeline.jar`
2. Enter "Application name" and "Pipeline name"
3. Get he template json file from http://localhost:8084//applications/{application}/pipelineConfigs/{pipelineName}. Update the `Account`. 
   * For example, the application is `gama` and the pipeline name is `ACA`, the URL is like http://localhost:8084//applications/gama/pipelineConfigs/ACA
   * Please refere [aca.txt](https://github.com/OpsMx/scripts/blob/master/spinnaker/aca.txt) to know where to add `Account`
4. Specify json file that you want to update. 

#### Canary Enable in `hal` deployment
   * Place [`settings.js`](https://github.com/OpsMx/scripts/blob/master/spinnaker/settings.js) in `~/.hal/default/profiles/`
   * Make sure you have `var canaryEnabled = true;` at line [15](https://github.com/OpsMx/scripts/blob/84c046d1623446bf6e0aa3080b027053071bf4e6/spinnaker/settings.js#L15) and `canary: canaryEnabled,` at line [137](https://github.com/OpsMx/scripts/blob/84c046d1623446bf6e0aa3080b027053071bf4e6/spinnaker/settings.js#L137)

#### Links
* Spinnaker API reference: https://www.spinnaker.io/reference/api/docs.html
* ACA configuration refence: https://github.com/OpsMx/scripts/wiki/ACA-Configuration
* Spinaker with Halyard deployment : https://www.spinnaker.io/setup/install/
* Kubernetes Source To Prod : https://www.spinnaker.io/guides/tutorials/codelabs/kubernetes-source-to-prod/
* Spinnaker custom configuration : https://www.spinnaker.io/reference/halyard/custom/

##### Spinnaker Issue
* [ACA task is failing immediately(Kubernetes)](https://github.com/spinnaker/spinnaker/issues/1904)
* [Kubernetes Account is not showing in Canary Stage UI(Dev-Spinnaker with Canary)](https://github.com/spinnaker/spinnaker/issues/1814)
