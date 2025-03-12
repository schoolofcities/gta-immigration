<script>
    import { onMount } from 'svelte';
    import { FELXN_YEARS, ONTELXN_YEARS } from "../lib/constants.js";
    import * as d3 from 'd3';

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
                renderScatterPlot();
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
        renderScatterPlot();
    }

    function renderScatterPlot() {
        if (!geoJsonData) return;

        const data = geoJsonData.features.map(d => ({
            x: d.properties[curParty],
            y: d.properties.pct_imm
        }));

        const svg = d3.select("#scatter-display").html("").append("svg")
            .attr("width", 500)
            .attr("height", 500);

        const margin = { top: 20, right: 30, bottom: 40, left: 40 };
        const width = +svg.attr("width") - margin.left - margin.right;
        const height = +svg.attr("height") - margin.top - margin.bottom;

        const x = d3.scaleLinear()
            .domain(d3.extent(data, d => d.x)).nice()
            .range([margin.left, width - margin.right]);

        const y = d3.scaleLinear()
            .domain(d3.extent(data, d => d.y)).nice()
            .range([height - margin.bottom, margin.top]);

        const xAxis = g => g
            .attr("transform", `translate(0,${height - margin.bottom})`)
            .call(d3.axisBottom(x).ticks(width / 80))
            .call(g => g.select(".domain").remove());

        const yAxis = g => g
            .attr("transform", `translate(${margin.left},0)`)
            .call(d3.axisLeft(y))
            .call(g => g.select(".domain").remove());

        svg.append("g").call(xAxis);
        svg.append("g").call(yAxis);

        svg.append("g")
            .attr("stroke", "black")
            .attr("stroke-width", 1.5)
            .selectAll("circle")
            .data(data)
            .join("circle")
            .attr("cx", d => x(d.x))
            .attr("cy", d => y(d.y))
            .attr("r", 3)
            .attr("fill", partyColors[curParty]);
    }

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

    <div id='scatter-display'></div>
</div>

<style>
    select {
        width: 100%;
        margin-bottom: 10px;
    }
</style>