'use strict';

/**
 * @ngdoc function
 * @name desafioApp.factory:Scopes
 * @description
 * # Factory para compartilhamento de variáveis entre controllers
 * Factory of the desafioApp
 */

angular.module('desafioApp').
    factory('Scopes', function ($rootScope) {
        var mem = {};

        return {
            store: function (key, value) {
                $rootScope.$emit('scope.stored', key);
                mem[key] = value;
            },
            get: function (key) {
                return mem[key];
            }
        };
    });