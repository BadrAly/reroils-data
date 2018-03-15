angular.module('reroilsUtils', [])
    .controller('exportController', ['$scope', function($scope) {
        $scope.csvURL = function() {
          return window.location.href.toString().replace('search', 'api/export/records/csv').replace(/size=\d+/, 'size=19999');
        };
    }])
    .directive('reroilsExportCsv', function() {
        return {
            template: '<div ng-controller="exportController"><a ng-href="{{ csvURL() }}" type="button" class="btn pull-right btn-success" translate>CSV Export</a></div>'
        };
    })

    .controller('recordController', ['$scope', function($scope) {

      record = $scope.rec;

      $scope.numberOfCitemsAvailable = function() {
        // console.log(record);
        var record = this.record;
        if(!record.metadata.hasOwnProperty('itemslist')){
          return 0;
        }
        var items = record.metadata.itemslist;
        var available = 0;
        angular.forEach(items, function(item, key) {
          if (item._circulation.status === 'on_shelf') {
            available += 1;
          }
        });
        return available;
      };
    }]);
