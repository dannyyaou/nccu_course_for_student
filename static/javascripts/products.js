var app = angular.module('store-directives', []);

app.directive("descriptions", function () {
    return {
        restrict: "E",
        templateUrl: "descriptions.html"
    }
});

app.directive("reviews", function () {
    return {
        restrict: "E",
        templateUrl: "reviews.html"
    }
});

app.directive("specs", function () {
    return {
        restrict: "E",
        templateUrl: "specs.html"
    }
});

app.directive("productTabs", function () {
    return {
        restrict: "E",

        templateUrl: "product-tabs.html",
        controller: function () {
            this.tab = 2;

            this.isSet = function (checkTab) {
                return this.tab === checkTab;
            };

            this.setTab = function (activeTab) {
                this.tab = activeTab;
            };
        },
        controllerAs: "tab"
    };
});

app.directive("myTabs", function () {
    return {
        restrict: "E",

        templateUrl: "my-tabs.html",
        controller: function () {

            this.tab = 2;

            this.isSet = function (checkTab) {
                return this.tab === checkTab;
            };

            this.setTab = function (activeTab) {
                this.tab = activeTab;
            };

        },
        controllerAs: "tab"

    }

});

app.directive("mycourses", function () {
    return {
        restrict: "E",
        templateUrl: "mycourse.html"
    }
});

app.directive("generalcourses", function () {
    return {
        restrict: "E",
        templateUrl: "MyCourses/generalcourses.html"
    }
});

app.directive("pecourses", function () {
    return {
        restrict: "E",
        templateUrl: "MyCourses/peCourses.html"
    }
});


app.directive("servicecourses", function () {
    return {
        restrict: "E",
        templateUrl: "MyCourses/servicecourses.html"
    }
});

app.directive("requiredcourses", function () {
    return {
        restrict: "E",
        templateUrl: "MyCourses/requiredCourses.html"
    }
});

app.directive("electivecourses", function () {
    return {
        restrict: "E",
        templateUrl: "MyCourses/electiveCourses.html"
    }
});
app.directive("militarycourses", function () {
    return {
        restrict: "E",
        templateUrl: "MyCourses/militaryCourses.html"
    }
});

app.directive("myrecommendation", function () {
    return {
        restrict: "E",
        templateUrl: "MyCourses/myrecommendation.html"
    }
});

app.directive("allmycourses", function () {
    return {
        restrict: "E",
        templateUrl: "MyCourses/allMyCourses.html"
    }
});


//
//app.directive("PECourses", function () {
//    return {
//        restrict: "E",
//        templateUrl: "specs.html"
//    }
//});
//
//app.directive("serviceCourses", function () {
//    return {
//        restrict: "E",
//        templateUrl: "specs.html"
//    }
//});
//
//app.directive("coreCourses", function () {
//    return {
//        restrict: "E",
//        templateUrl: "specs.html"
//    }
//});
//
//app.directive("electiveCourses", function () {
//    return {
//        restrict: "E",
//        templateUrl: "specs.html"
//    }
//});