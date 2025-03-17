<script>
    import { onMount } from 'svelte';
    import { FELXN_YEARS, ONTELXN_YEARS, PARTY_COLOURS } from "../lib/constants.js";
    import * as d3 from 'd3';

    let region = $state("fed");
    let years = $state(FELXN_YEARS);
    let curYear = $state(2021);
    let parties = $state([]);
    let curParty = $state("lib_pct");
    let geoJsonData = $state(null);
    let correlation = $state(0);
    let hoveredPoint = $state(null);

    function loadGeoJson() {
        const filePath = `/data/elections/${region}_stats_${curYear}.geojson`;
        fetch(filePath)
            .then(response => response.json())
            .then(data => {
                geoJsonData = data;
                console.log($state.snapshot(geoJsonData));
                updateSelectOptions();
                loadCorrelation();
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
        loadCorrelation();
    }

    function loadCorrelation() {
        // Load the CSV file using a Promise
        d3.csv(`/data/elections_analysis/ed_corrs.csv`)
            .then(data => {
                const normalizedRegion = region === 'ont-ed' ? 'ontario' : region === 'fed' ? 'federal' : region;
                const party = curParty.split('_')[0];
                const columnName = `corr_pct_imm_${party}`;

                // Find the row that matches the curYear and normalizedRegion
                const row = data.find(d => d.year === curYear.toString() && d.region === normalizedRegion);

                // Set the correlation value
                if (row && row[columnName]) {
                    correlation = parseFloat(row[columnName]);
                } else {
                    correlation = 0; // Set to zero if no value is found
                }

                // console.log($state.snapshot(correlation));
                renderScatterPlot();
            })
            .catch(error => {
                console.error('Error loading CSV file:', error);
                correlation = 0; // Set to zero in case of an error
            });
    }

    function renderScatterPlot() {
        if (!geoJsonData) return;

        const data = geoJsonData.features.map(d => ({
            x: d.properties[curParty],
            y: d.properties.pct_imm,
            geoname: d.properties.geoname
        }));

        const svg = d3.select("#scatter-display").html("").append("svg")
            .attr("width", "100%")
            .attr("height", 500);

        const margin = { top: 20, right: 30, bottom: 60, left: 60 };
        const width = svg.node().getBoundingClientRect().width - margin.left - margin.right;
        const height = +svg.attr("height") - margin.top - margin.bottom;

        const x = d3.scaleLinear()
            .domain([0, 80])
            .range([margin.left, width - margin.right]);

        const y = d3.scaleLinear()
            .domain([0, 0.7])
            .range([height - margin.bottom, margin.top]);

        const xAxis = g => g
            .attr("transform", `translate(0,${height - margin.bottom})`)
            .call(d3.axisBottom(x).ticks(8))
            .call(g => g.select(".domain").remove())
            .append("text")
            .attr("x", width / 2)
            .attr("y", 40)
            .attr("fill", "black")
            .attr("text-anchor", "middle")
            .text(parties.find(p => p.property === curParty)?.name + " vote percent");

        const yAxis = g => g
            .attr("transform", `translate(${margin.left},0)`)
            .call(d3.axisLeft(y).ticks(7))
            .call(g => g.select(".domain").remove())
            .append("text")
            .attr("x", -height / 2)
            .attr("y", -40)
            .attr("fill", "black")
            .attr("text-anchor", "middle")
            .attr("transform", "rotate(-90)")
            .text("Proportion of immigrants");

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
            .attr("fill", PARTY_COLOURS[curParty])
            .on("mouseover", (event, d) => {
                hoveredPoint = d;
                d3.select(event.target).attr("r", 6).attr("stroke", "red").attr("stroke-width", 2);
            })
            .on("mouseout", (event, d) => {
                hoveredPoint = null;
                d3.select(event.target).attr("r", 3).attr("stroke", "black").attr("stroke-width", 1.5).attr("fill", PARTY_COLOURS[curParty]);
            });

        // Add correlation line
        const line = d3.line()
            .x(d => x(d.x))
            .y(d => y(d.y));

        const xMean = d3.mean(data, d => d.x);
        const yMean = d3.mean(data, d => d.y);
        const slope = correlation * (d3.deviation(data, d => d.y) / d3.deviation(data, d => d.x));
        const intercept = yMean - slope * xMean;

        const lineData = [
            { x: 0, y: intercept },
            { x: 80, y: intercept + slope * 80 }
        ];

        svg.append("path")
            .datum(lineData)
            .attr("fill", "none")
            .attr("stroke", "purple")
            .attr("stroke-width", 2)
            .attr("stroke-dasharray", "4,4")
            .attr("clip-path", "url(#clip)")
            .attr("d", line);

        svg.append("defs").append("clipPath")
            .attr("id", "clip")
            .append("rect")
            .attr("x", margin.left)
            .attr("y", margin.top)
            .attr("width", width - margin.left - margin.right)
            .attr("height", height - margin.top - margin.bottom);
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

    <div class="hover-panel">
        <div><strong>Riding:</strong> {#if hoveredPoint} {hoveredPoint.geoname} {/if}</div>
        <div><strong>Vote Share:</strong> {#if hoveredPoint} {hoveredPoint.x}% {/if}</div>
        <div><strong>Proportion of Immigrants:</strong> {#if hoveredPoint} {hoveredPoint.y} {/if}</div>
    </div>
</div>

<style>
    select {
        width: 100%;
        margin-bottom: 10px;
    }

    .hover-panel {
        margin-top: 10px;
        padding: 10px;
        border: 1px solid #ccc;
        background-color: #f9f9f9;
    }
</style>