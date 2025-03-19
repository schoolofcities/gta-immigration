<script>
    import { onMount } from "svelte";
    import { PARTY_COLOURS, PARTY_TAG_MAP } from "../lib/constants.js";
    import * as d3 from 'd3';

    const parties = [
        { name: "Liberals", tag: "lib" },
        { name: "Conservatives", tag: "cons1" },
        { name: "New Democrats", tag: "ndp" },
    ]

    let curRegion = $state("federal");
    let curParty = $state("lib");
    let curScope = $state("gta");

    // Function to handle curRegion change
    function handleRegionChange(event) {
        curRegion = event.target.value;
    }

    function handlePartyChange(event) {
        curParty = event.target.value;
    }

    function handleScopeChange(event) {
        curScope = event.target.value;
    }
</script>

<div>
    <select onchange={handleRegionChange}>
        <option value="federal" selected>Federal</option>
        <option value="ontario">Ontario</option>
    </select>
    <select onchange={handlePartyChange}>
        {#each parties as party}
            <option value={party.tag}>{party.name}</option>
        {/each}
    </select>
    <select onchange={handleScopeChange}>
        <option value="gta" selected>GTA</option>
        <option value="full">Full</option>
    </select>
</div>

<!-- SVG container for the graph -->
<svg id="graph"></svg>


<style>
    select {
        width: 100%;
        margin-bottom: 10px;
    }
</style>