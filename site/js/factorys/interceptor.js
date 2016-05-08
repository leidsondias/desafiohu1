'use strict';

/**
 * @ngdoc function
 * @name desafioApp.factory:HttpInterceptor
 * @description
 * # HttpInterceptor intercepta todas as chamadas http do app.
 * # Chama e esconde o loading para quando houver loading dos dados.
 *
 */

angular.module('desafioApp')
    .factory('HttpInterceptor', ['$q', function($q) {
        var numRequests = 0;

        var hide = function(r) {
        if (!--numRequests) {
          //@TODO
        }
        return r;
        };

        return {
        'request': function(config) {
          numRequests++;
          return config;
        },
        'response': function(response) {
          return hide(response);
        },
        'responseError': function(response) {
          if (response.status == 0) {
            //@TODO
            return;
          }
          return $q.reject(hide(response));
        }
    };
}]);
