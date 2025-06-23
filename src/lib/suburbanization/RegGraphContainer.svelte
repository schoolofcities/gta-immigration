<script>
    import RegGraphDist from "./RegGraphDist.svelte";
    import RegGraphXTop from "./RegGraphXTop.svelte";
</script>

<div class="container plots-title">
    <h4>
        Title
    </h4>
    <p>
        Subtitle
    </p>
</div>

<div>
    <RegGraphXTop />
    
    <RegGraphDist year={1961} showYAxisLabel={true} />
    <RegGraphDist year={1981} />
    <RegGraphDist year={2001} />
    <RegGraphDist year={2021} showXAxisLabel={true} showXAxisTicks={true} />
</div>