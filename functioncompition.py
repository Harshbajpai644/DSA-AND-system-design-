
var compose = function(functions) {
    if (functions.length === 0) {
        return function(x) {
            return x;
        };
    }

    return function(x) {
        return functions.reduceRight((acc, fn) => {
            return fn(acc);
        }, x);
    };
