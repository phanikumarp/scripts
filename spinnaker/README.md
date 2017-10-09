Check wiki [pages](https://github.com/OpsMx/scripts/wiki) also
#### How to run `autopipeline.jar`?(How to update `account` name in ACA/Canary stage.)
0. Make sure you tunneled to Spinnaker
1. Download & Run: `wget -qO autopipeline.jar https://goo.gl/hmxGio && java -jar autopipeline.jar`
2. Enter "Application name" and "Pipeline name"
3. Get he template json file from http://localhost:8084//applications/{application}/pipelineConfigs/{pipelineName}. Update the `Account`. 
   * For example, the application is `gama` and the pipeline name is `ACA`, the URL is like http://localhost:8084//applications/gama/pipelineConfigs/ACA
   * Please refere [aca.txt](https://github.com/OpsMx/scripts/blob/master/spinnaker/aca.txt) to know where to add `Account`
4. Specify json file that you want to update. 

#### Canary Enable in `hal` deployment
   1. Place [`settings.js`](https://github.com/OpsMx/scripts/blob/master/spinnaker/settings.js) in `~/.hal/default/profiles/`
   2. Make sure you have `var canaryEnabled = true;` at line [15](https://github.com/OpsMx/scripts/blob/84c046d1623446bf6e0aa3080b027053071bf4e6/spinnaker/settings.js#L15) and `canary: canaryEnabled,` at line [137](https://github.com/OpsMx/scripts/blob/84c046d1623446bf6e0aa3080b027053071bf4e6/spinnaker/settings.js#L137)
   3. Edit [`orca-local.yml`](https://github.com/OpsMx/scripts/blob/master/spinnaker/orca-local.yml)-> `mine` URL and place the file in `~/.hal/default/profiles/`
