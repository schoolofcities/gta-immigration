<script>
    import StepGraphDist from "./StepGraphDist.svelte";
</script>

<div class="container plots-title">
    <h4>
        The suburbs have hosted more and more immigrants, while non-immigrants spread out across the region
    </h4>
    <p>
        Population of <span id="non-imm">non-immigrants</span>, <span id="imm">all immigrants</span>, and <span id="new-imm">new immigrants</span> in 1km-bands away from central Toronto.
    </p>
    <br>
</div>

<div>
    <StepGraphDist year={1961} showYAxisLabel={false} showLocationLabels={true} />
    <!-- <StepGraphDist year={1981} showYAxisLabel={true} showXAxisTicks={true} />
    <StepGraphDist year={2001} showYAxisLabel={true} showXAxisTicks={true} /> -->
    <StepGraphDist year={2021} showYAxisLabel={false} showXAxisTicks={true} showXAxisLabel={true}/>
</div>

<style>
    #non-imm {
        /* background-color: var(--brandYellow); */
        border-bottom: solid 2px var(--brandLightGreen);
    }

    #imm {
        /* color: #ffffff; */
        /* background-color: var(--brandPurple); */
        border-bottom: solid 2px var(--brandPurple);
    }

    #new-imm {
        /* background-color: #d5a4b2; */
        border-bottom: solid 1.5px var(--brandPink);
    }
</style>