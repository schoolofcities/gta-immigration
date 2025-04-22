<script>
    import { onMount } from 'svelte';
    import { FELXN_YEARS, ONTELXN_YEARS, PARTY_COLOURS, PARTIES_INFO } from "../lib/constants.js";
    import { getRegionTag, updatePartyOptions } from "./utils.js";
    import * as d3 from 'd3';

    let curRegion = $state("ontario");
    let curRegionTag = $derived(getRegionTag(curRegion));

    let years = $state(ONTELXN_YEARS);
    let curYear = $state(2025);

    let geoJsonData = $state(null);

    let curParties = $derived(updatePartyOptions(geoJsonData));
    let curParty = $state("cons1");

    let correlation = $state(0);
    let activePoint = $state(null); 

    let windowWidth = $state(400);
    
    function loadGeoJson() {
        const filePath = `/gta-immigration/data/elections/${curRegionTag}_stats_${curYear}.geojson`;
        fetch(filePath)
            .then(response => response.json())
            .then(data => {
                geoJsonData = data;
                // console.log($state.snapshot(geoJsonData));
                updateSelectOptions();
                loadCorrelation();
            });
    }

    function updateSelectOptions() {
        if (geoJsonData && geoJsonData.features.length > 0) {
            if (!curParties.some(p => p.tag === curParty)) {
                curParty = curParties.length > 0 ? curParties[0].tag : null;
            }
        }
    }

    function handleRegionChange(event) {
        curRegion = event.target.value;
        years = curRegion === "federal" ? FELXN_YEARS : ONTELXN_YEARS;
        curYear = years[years.length - 1];
        clearPointSelection();
        loadGeoJson();
    }

    function handleYearChange(event) {
        curYear = parseInt(event.target.value);  
        clearPointSelection();
        loadGeoJson();
    }

    function handlePartyChange(event) {
        curParty = event.target.value;
        clearPointSelection();
        loadCorrelation();
    }

    function loadCorrelation() {
        // Load the CSV file using a Promise
        d3.csv(`/gta-immigration/data/elections_analysis/ed_corrs.csv`)
            .then(data => {
                const columnName = `corr_pct_imm_${curParty}`;

                // Find the row that matches the curYear and curRegion
                const row = data.find(d => d.year === curYear.toString() && d.region === curRegion);

                // Set the correlation value
                if (row && row[columnName]) {
                    correlation = parseFloat(row[columnName]);
                } else {
                    correlation = 0; 
                }

                // console.log($state.snapshot(correlation));
                renderScatterPlot();
            })
            .catch(error => {
                console.error('Error loading CSV file:', error);
                correlation = 0; 
            });
    }

    function clearPointSelection() {
        activePoint = null;
    }

    function resetPointStyle(selection) {
        selection
            .attr("r", 5)
            .attr("stroke", "#000000")
            .attr("stroke-width", 0)
            .attr("fill", PARTY_COLOURS[curParty]);
    }

    function highlightPoint(selection) {
        selection
            .attr("r", 6)
            .attr("stroke", "#000000")
            .attr("stroke-width", 2);
    }

    function renderScatterPlot() {
        if (!geoJsonData) return;

        const partyPropertyTag = PARTIES_INFO.find(party => party.tag === curParty).propertyTag;
        
        const data = geoJsonData.features.map(d => ({
            x: d.properties.pct_imm, 
            y: d.properties[partyPropertyTag],
            geoname: d.properties.geoname
        }));

        // Clear previous SVG content
        const container = d3.select("#scatter-display");
        container.html("");

        const margin = { top: 20, right: 20, bottom: 60, left: 60 };
        
        // Create SVG with a viewBox for better responsiveness
        const containerWidth = Math.min(700, container.node().getBoundingClientRect().width);
        const width = containerWidth - margin.left - margin.right;
        const height = 450 - margin.top - margin.bottom;

        const svg = container.append("svg")
            .attr("width", containerWidth)
            .attr("height", 500)
            .attr("viewBox", `0 0 ${containerWidth} 500`)
            .attr("preserveAspectRatio", "xMinYMin meet");

        // Create the main group element that will contain the plot
        const g = svg.append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        const x = d3.scaleLinear()
            .domain([0, 70])  
            .range([0, width]);

        const y = d3.scaleLinear()
            .domain([0, 80])  
            .range([height, 0]);

        const xAxis = g => g
            .attr("transform", `translate(0,${height})`)
            .call(d3.axisBottom(x).ticks(7))
            .call(g => g.select(".domain").remove())
            .call(g => g.selectAll(".tick line")
                .clone()
                .attr("y2", -height) 
                .attr("stroke", "#D0D1C9") 
                .attr("stroke-width", 1) 
                .attr("stroke-opacity", 0.1)) 
            .call(g => g.selectAll(".tick line") 
                .attr("stroke", "#000000")) 
            .call(g => g.selectAll(".tick text") 
                .attr("fill", "#000000")) 
            .append("text")
                .attr("x", width / 2 - 14)
                .attr("y", 40)
                .attr("fill", "#000000")
                .attr("text-anchor", "middle")
                .text("Percentage of immigrants (%)")
                .style("font-size", "13px")
                .style("font-family", "RobotoRegular");  

        const yAxis = g => g
            .attr("transform", `translate(0,0)`)
            .call(d3.axisLeft(y).ticks(8))
            .call(g => g.select(".domain").remove())
            .call(g => g.selectAll(".tick line")
                .clone()
                .attr("x2", width) 
                .attr("stroke", "#ccc") 
                .attr("stroke-width", 1) 
                .attr("stroke-opacity", 0.1))
            .call(g => g.selectAll(".tick line") 
                .attr("stroke", "#000000")) 
            .call(g => g.selectAll(".tick text") 
                .attr("fill", "#000000")) 
            .append("text")
                .attr("x", -height / 2)
                .attr("y", -40)
                .attr("fill", "#000000")
                .attr("text-anchor", "middle")
                .attr("transform", "rotate(-90)")
                .text("Party vote share (%)")
                .style("font-size", "13px")
                .style("font-family", "RobotoRegular");  

        // Append axes to the main group
        g.append("g").call(xAxis);
        g.append("g").call(yAxis);

        const pointsGroup = g.append("g")
            .attr("stroke", "#000000")
            .attr("stroke-width", 0);

        pointsGroup.selectAll(".scatter-correlation-dot")
            .data(data)
            .join("circle")
            .attr("class", "scatter-correlation-dot")
            .attr("cx", d => x(d.x))
            .attr("cy", d => y(d.y))
            .attr("r", 5)
            .attr("fill", PARTY_COLOURS[curParty])
            .on("mouseover", (event, d) => {
                event.stopPropagation();
                activePoint = d;
                
                d3.select("#scatter-display")
                    .selectAll("circle")
                    .each(function() {
                        resetPointStyle(d3.select(this));
                    });
                
                highlightPoint(d3.select(event.target));
            })
            .on("mouseout", (event, d) => {
                event.stopPropagation();
                if (activePoint && activePoint.geoname === d.geoname && 
                    event.target.__data__ === activePoint) {
                    activePoint = null;
                    resetPointStyle(d3.select(event.target));
                }
            })
            .on("click", (event, d) => {
                event.stopPropagation();
                activePoint = d;
                
                d3.select("#scatter-display")
                    .selectAll("circle")
                    .each(function() {
                        resetPointStyle(d3.select(this));
                    });
                
                highlightPoint(d3.select(event.target));
            });

        // Add click handler to the SVG container
        svg.on("click", (event) => {
            // Only clear if clicking outside points (not a point or its children)
            if (!event.target.classList.contains("scatter-correlation-dot")) {
                activePoint = null;
                d3.select("#scatter-display")
                    .selectAll("circle")
                    .each(function() {
                        resetPointStyle(d3.select(this));
                    });
            }
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
            { x: 70, y: intercept + slope * 70 } 
        ];

        // Add the correlation line to the main group
        g.append("path")
            .datum(lineData)
            .attr("fill", "none")
            .attr("stroke", "#000000")
            .attr("stroke-width", 1.5)
            .attr("stroke-dasharray", "8,2")
            .attr("d", line);
    }

    $effect(() => {
        windowWidth;
        renderScatterPlot();
    });

    onMount(() => {
        loadGeoJson();
    });
</script>


<div style="margin-bottom: 0px; margin-top: -25px;">


    <div class="sentence-controls">
        <p>
            View the correlation between percent immigrants and party vote share for the
            <select onchange={handlePartyChange} class="inline-select" bind:value={curParty}>
                {#each curParties as party}
                    <option value={party.tag} selected={party.tag === curParty}>{party.name}</option>
                {/each}
            </select>
            in the 
            <select onchange={handleYearChange} class="inline-select" bind:value={curYear}>
                {#each years as y}
                    <option value={y} selected={y === curYear}>{y}</option>
                {/each}
            </select>
            <select onchange={handleRegionChange} class="inline-select" bind:value={curRegion}>
                <option value="federal" selected={curRegion === 'federal'}>federal</option>
                <option value="ontario" selected={curRegion === 'ontario'}>Ontario</option>
            </select>
            election.
        </p>
    </div>

    <div id='scatter-display' bind:clientWidth={windowWidth}></div>

    <div>
        <div class="info-row" style="border-top: solid 1px #f0f0f0;">
            {#if activePoint}
                <p><b>{activePoint.geoname}</b></p>
            {:else}
                <p><i>Hover/click on a point</i></p>
            {/if}
        </div>
        <div class="info-row">
            {#if activePoint}
                <p>Vote share = <b>{(activePoint.y).toFixed(1)}%</b></p>
            {:else} 
                <p>Vote share = <b>N/A</b></p>
            {/if}
        </div>
        <div class="info-row">
            {#if activePoint}
                <p>Percent immigrants = <b>{(activePoint.x).toFixed(1)}%</b></p>
            {:else} 
                <p>Percent immigrants = <b>N/A</b></p>
            {/if}
        </div>
    </div>

</div>

<style>
    #scatter-display {
        width: 100%;
        max-width: 700px;
        margin-bottom: -55px;
    }
</style>