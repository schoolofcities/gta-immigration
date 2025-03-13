<script>
    import { onMount } from "svelte";
    import { PARTY_COLOURS } from "../lib/constants.js";
    import * as d3 from 'd3';

    const partyTagMap = {
        "Liberals": "lib",
        "Conservatives": "cons1",
        "New Democrats": "ndp"
    };
    const parties = ["Liberals", "Conservatives", "New Democrats"];
    
    let region = $state("fed");
    let curParties = $state([]);
    let curCorrs = $state({
        "Liberals": [],  // contains elements of the form [year, corr]
        "Conservatives": [],
        "New Democrats": [],
    })

    function handleRegionChange(event) {
        region = event.target.value;
        updateCorrelations();
    }

    function toggleParty(party) {
        if (curParties.includes(party)) {
            curParties = curParties.filter(p => p !== party);
        } else {
            curParties = [...curParties, party];
        }
    }

    function updateCorrelations() {
        d3.csv('/data/elections_analysis/ed_corrs.csv').then(data => {
            const regionFilter = region === 'fed' ? 'federal' : 'ontario';
            const filteredData = data.filter(row => row.region === regionFilter);

            // Update the curCorrs state variable
            curCorrs = {
                "Liberals": filteredData.map(row => [parseInt(row.year), parseFloat(row.corr_pct_imm_lib)]),
                "Conservatives": filteredData.map(row => [parseInt(row.year), parseFloat(row.corr_pct_imm_cons1)]),
                "New Democrats": filteredData.map(row => [parseInt(row.year), parseFloat(row.corr_pct_imm_ndp)]),
            };
            // console.log($state.snapshot(curCorrs));
        }).catch(error => {
            console.error('Error loading or processing CSV data:', error);
        });
    }

    onMount(() => {
        updateCorrelations();
    })
</script>

<div>
    <select onchange={handleRegionChange}>
        <option value="fed" selected>Federal</option>
        <option value="ont-ed">Ontario</option>
    </select>
    {#each parties as party}
        <button 
            onclick={() => toggleParty(party)} 
            class:active={curParties.includes(party)}
        >
            {party}
        </button>
    {/each}
</div>

<style>
    select {
        width: 100%;
        margin-bottom: 10px;
    }

    button {
        background-color: gray;
        color: white;
        margin-right: 10px;
        padding: 10px;
        border: none;
        cursor: pointer;
    }
    button.active {
        background-color: blue;
    }
</style>