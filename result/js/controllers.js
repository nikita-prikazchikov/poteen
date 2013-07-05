'use strict';

/* Controllers */

function TestResultCtrl($scope, $dialog, $routeParams, $location, TestResult) {
    $scope.testCaseList = TestResult.query();
    $scope.statusList = ["passed", "failed"];
    $scope.testCaseFilter = {};
    $scope.testCaseFilter.status = $location.search().status || "";
    $scope.testCaseFilter.test_suite_name = $location.search().test_suite_name || "";

    $scope.setTestCase=function(testCase){
        $scope.testCase = testCase;
    };

    $scope.fixValue=function(value){
        return value == null ? '': value;
    };

    $scope.showDetails = function( status, testSuite){
        $location.search("status", status ? status : "" );
        $location.search("test_suite_name", testSuite ? testSuite : "" );
        $location.path("/tests");
    };

    $scope.showLog = function (testCase) {
        var d = $dialog.dialog({
                backdrop: true,
                keyboard: true,
                backdropClick: true,
                templateUrl: "partials/log.html",
                controller: 'DialogController',
                dialogClass: "modal full-height big",
                resolve:{
                    testCase:function(){return testCase}
                }
            }
        );
        d.open();
    }
}

function DialogController($scope, dialog, testCase) {

    $scope.testCase = testCase;
    $scope.testStepList = eval(testCase.log);
    $scope.testStepId = 0;

    $scope.close = function () {
        dialog.close();
    };
}