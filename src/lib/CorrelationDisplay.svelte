<script>
    import { onMount } from 'svelte';
    import { FELXN_YEARS, ONTELXN_YEARS } from "../lib/constants.js";

    let region = $state("fed");

    let years = $state(FELXN_YEARS);
    let curYear = $state(2021);

    let parties = $state([]);
    let curParty = $state("lib_pct");

    let geoJsonData = $state(null);
    
    const partyColors = {
        lib_pct: "#da121a",
        cons1_pct: "#15284c", 
        ndp_pct: "#f07c00", 
        cons2_pct: "#2db56b", 
    };

    function loadGeoJson() {
        const filePath = `/data/elections/${region}_stats_${curYear}.geojson`;
        fetch(filePath)
            .then(response => response.json())
            .then(data => {
                geoJsonData = data;
                console.log($state.snapshot(geoJsonData));
                updateSelectOptions();
            });
    }
    
    function updateSelectOptions() {
        if (geoJsonData && geoJsonData.features.length > 0) {
            const properties = geoJsonData.features[0].properties;

            parties = [];
            if (properties.lib_pct !== null) parties.push({ name: "Liberals", property: "lib_pct" });
            if (properties.cons1_pct !== null) parties.push({ name: "Conservatives", property: "cons1_pct" });
            if (properties.ndp_pct !== null) parties.push({ name: "New Democrats", property: "ndp_pct" });
            if (properties.cons2_pct !== null) parties.push({ name: "Reform/Alliance", property: "cons2_pct" });

            // Ensure curParty and selectedCensusVariable are valid
            if (!parties.some(p => p.property === curParty)) {
                curParty = parties.length > 0 ? parties[0].property : null;
            }
        }
    }

    function handleRegionChange(event) {
        region = event.target.value;
        years = region === "fed" ? FELXN_YEARS : ONTELXN_YEARS;
        curYear = years[years.length - 1];
        loadGeoJson();
    }

    function handleYearChange(event) {
        curYear = event.target.value;
        loadGeoJson();
    }

    function handlePartyChange(event) {
        curParty = event.target.value;
    }

    // $effect(() => {
    //     loadGeoJson();
    // });
    
    onMount(() => {
        loadGeoJson();
    });

</script>


<div>
    <select onchange={handleRegionChange}>
        <option value="fed" selected>Federal</option>
        <option value="ont-ed">Ontario</option>
    </select>

    <select onchange={handleYearChange}>
        {#each years as y}
            <option value={y} selected={y === curYear}>{y}</option>
        {/each}
    </select>

    <select onchange={handlePartyChange}>
        {#each parties as party}
            <option value={party.property}>{party.name}</option>
        {/each}
    </select>
</div>


<style>
    select {
        width: 100%;
        margin-bottom: 10px;
    }
</style>