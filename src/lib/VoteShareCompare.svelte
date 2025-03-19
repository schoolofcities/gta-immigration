<script>
    import { onMount } from "svelte";
    import { PARTY_COLOURS, PARTY_TAG_MAP } from "../lib/constants.js";
    import * as d3 from 'd3';

    const parties = [
        { name: "Liberals", tag: "lib" },
        { name: "Conservatives", tag: "cons1" },
        { name: "New Democrats", tag: "ndp" },
    ];

    // State variables
    let curRegion = $state("federal");
    let curParty = $state("lib");
    let curScope = $state("gta");
    let curVoteShares = $state([]); // To store the processed data

    // Function to handle curRegion change
    function handleRegionChange(event) {
        curRegion = event.target.value;
    }

    // Function to handle curParty change
    function handlePartyChange(event) {
        curParty = event.target.value;
    }

    // Function to handle curScope change
    function handleScopeChange(event) {
        curScope = event.target.value;
    }

    // Function to load and process the CSV
    function loadVoteShares() {
        const csvPath = "/data/elections_analysis/ed_top_5_imm_results.csv"; // Static path to the CSV file

        d3.csv(csvPath)
            .then((data) => {
                // Filter rows based on curRegion and curParty
                const filteredData = data.filter(
                    (row) => row.region === curRegion && row.party === curParty
                );

                // Group by year and extract the required columns
                const result = [];
                const years = new Set(filteredData.map((row) => row.year));

                years.forEach((year) => {
                    const yearData = filteredData.filter((row) => row.year === year);
                    yearData.forEach((row) => {
                        const firstElement = parseFloat(row.top_5_imm_pct); // Convert to number
                        const secondElement = curScope === 'gta' 
                            ? parseFloat(row.gta_pct) 
                            : parseFloat(row.full_pct); // Convert to number
                        if (!isNaN(firstElement) && !isNaN(secondElement)) {
                            result.push([parseFloat(year), firstElement, secondElement]);
                        }
                    });
                });

                // Save the result to curVoteShares 
                curVoteShares = result;
            })
            .catch((error) => {
                console.error('Error parsing CSV:', error);
            });
    }

    // Load the CSV when the component mounts or when state variables change
    $effect(() => {
        loadVoteShares();
    });
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