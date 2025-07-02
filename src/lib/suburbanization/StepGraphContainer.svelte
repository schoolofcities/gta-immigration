<script>
    import StepGraphDist from "./StepGraphDist.svelte";
</script>

<div class="container plots-title">
    <h4>
        The suburbs hosts more and more immigrants, while non-immigrants live all over the region
    </h4>
    <p>
        Number of <span id="non-imm">non-immigrants</span>, <span id="imm">all immigrants</span>, and <span id="new-imm">new immigrants</span> in 1km-bands away from Toronto's city center.
    </p>
</div>

<div>
    <StepGraphDist year={1961} showYAxisLabel={true} showLocationLabels={true} />
    <StepGraphDist year={1981} />
    <StepGraphDist year={2001} />
    <StepGraphDist year={2021} showXAxisLabel={true} showXAxisTicks={true} />
</div>

<style>
    #non-imm {
        background-color: var(--brandYellow);
        border-bottom: solid 2px var(--brandYellow);
    }

    #imm {
        color: #ffffff;
        background-color: var(--brandPurple);
        border-bottom: solid 2px var(--brandPurple);
    }

    #new-imm {
        background-color: #d5a4b2;
        border-bottom: solid 2px #d5a4b2;
    }
</style>