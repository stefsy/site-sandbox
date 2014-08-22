// from http://bl.ocks.org/mbostock/4061502

//what is this enclosing function?
(function() {

    d3.box = function() {
        var width = 1,
            height = 1,
            duration = 0,
            domain = null,
            value = Number,
            whiskers = boxWhiskers,
            quartiles = boxQuartiles,
            tickFormat = null;

    //for each small multiple
    function box(g) {
        g.each(function(d,i){
            d = d.map(value).sort(d3.ascending);
            var g = d3.select(this),
                n = d.length,
                min = d[0],
                max = d[n-1];

            //compute quartiles, returns 3
            var quartileData = d.quartiles = quartiles(d);

            //compute whiskers. must return 2 elements or null.
            //what? doesn't this evaluate into booleans?
            var whiskerIndices = whiskers && whiskers.call(this,d,i),
                whiskerData = whiskerIndices && whiskerIndices.map(function(i) {return d[i]; });


            //compute outliers
            //compute outliers as indices to join across transitions?
            var outlierIndices = whiskerIndices ? drange(0,whiskerIndices[0]).concat(d3.range(whiskterIndices[1]+1,n)): d3.range(n);



        })
    }

    }
})
