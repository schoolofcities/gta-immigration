<script>
    import StepGraphDist from "./StepGraphDist.svelte";
</script>

<div class="container plots-title">
    <h4>
        The suburbs hosts more and more immigrants, while non-immigrants live all over the region
    </h4>
    <p>
        Number of non-immigrants, all immigrants, and new immigrants in 1km-bands away from Toronto's city center.
    </p>
</div>

<div>
    <StepGraphDist year={1961} showYAxisLabel={true} showLocationLabels={true} />
    <StepGraphDist year={1981} />
    <StepGraphDist year={2001} />
    <StepGraphDist year={2021} showXAxisLabel={true} showXAxisTicks={true} />
</div>