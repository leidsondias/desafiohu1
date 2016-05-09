'use strict';

/**
 * @ngdoc function
 * @name desafioApp.controller:SearchCtrl
 * @description
 * # Controlador responsável pela busca da aplicação
 * Controller of the desafioApp
 */
angular.module('desafioApp')
    .controller('SearchCtrl', function ($scope, $http, $location, CONFIG, Scopes) {
        var auto_complete_list = angular.element('.auto-complete');
        var local_error = angular.element('span.error');

        $scope.doHide = function(){
            auto_complete_list.css("display", "none");
        };

        $scope.autoComplete = function(){
            if($scope.search.local && $scope.search.local.length > 3){
                $http.get(CONFIG.url_proxy+'/list', {params: {"query": $scope.search.local}})
                    .success(function(data) {
                        auto_complete_list.css("display", "block");

                        if(data.length !== 0){
                            $scope.autoCompleteList = data
                        }else{
                            $scope.autoCompleteList = [{"name": "Nenhum resultado para esta pesquisa."}]
                        }
                    })
                    .error(function(data){
                        //@TODO: Retorno falha
                    });
            }else{
                auto_complete_list.css("display", "none");
            }

        };

        $scope.doSearch = function(){
            if($scope.search_form.$valid && $scope.search.localObj && $scope.search.local.length > 3){
                var params = {"kind": $scope.search.localObj.kind, "id": $scope.search.localObj.id,
                        "start_date": $scope.search.start_date, "end_date": $scope.search.end_date}
                $location.path('/result').search(params);
            }else if(!$scope.search.localObj || $scope.search.local.length <= 3){
                local_error.css('display','block');
            }
        };


        $scope.setLocal = function(item){
            $scope.search.local = item.name;
            $scope.search.localObj = item;
            auto_complete_list.css("display", "none");
            local_error.css('display','none');
        };

    });
