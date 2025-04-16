<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { PARTY_COLOURS, PARTIES_INFO } from "../lib/constants.js";

    // Configuration
    const elections = [
        { year: 1999, region: "ontario" },
        { year: 2014, region: "ontario" },
        { year: 2025, region: "ontario" }
    ];
    const party = "cons1";
    const partyPropertyTag = PARTIES_INFO.find(p => p.tag === party).propertyTag;

    // Data storage
    let electionData = $state([]);
    let loaded = $state(false);

    onMount(() => {
        loadAllData();
    });

    function loadAllData() {
        const promises = elections.map(election => {
            return Promise.all([
                d3.json(`/gta-immigration/data/elections/ont-ed_stats_${election.year}.geojson`),
                d3.csv(`/gta-immigration/data/elections_analysis/ed_corrs.csv`)
            ]).then(([geoJsonData, corrData]) => {
                const row = corrData.find(d => 
                    d.year === election.year.toString() && d.region === election.region
                );
                
                const points = geoJsonData.features.map(d => ({
                    x: d.properties.pct_imm,
                    y: d.properties[partyPropertyTag],
                    geoname: d.properties.geoname
                }));

                return {
                    year: election.year,
                    points,
                    correlation: row ? parseFloat(row[`corr_pct_imm_${party}`]) : 0,
                    xMean: d3.mean(points, d => d.x),
                    yMean: d3.mean(points, d => d.y),
                    xDev: d3.deviation(points, d => d.x),
                    yDev: d3.deviation(points, d => d.y)
                };
            });
        });

        Promise.all(promises).then(results => {
            electionData = results.sort((a, b) => a.year - b.year);
            loaded = true;
            renderAllPlots();
        }).catch(error => {
            console.error("Error loading data:", error);
        });
    }

    function renderAllPlots() {
        if (!loaded || !electionData.length) return;

        const container = d3.select("#static-correlation-container");
        container.html("");

        const containerWidth = Math.min(1000, window.innerWidth - 40);
        const plotWidth = containerWidth / 3 - 20;

        const grid = container.append("div")
            .attr("class", "static-correlation-grid");

        electionData.forEach((data, i) => {
            const plotContainer = grid.append("div")
                .attr("class", "static-correlation-plot");

            const margin = { top: 40, right: 20, bottom: 50, left: 40 };
            const width = plotWidth - margin.left - margin.right;
            const height = 250 - margin.top - margin.bottom;

            const svg = plotContainer.append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", `translate(${margin.left},${margin.top})`);

            // Scales
            const x = d3.scaleLinear()
                .domain([0, 70])
                .range([0, width]);

            const y = d3.scaleLinear()
                .domain([0, 80])
                .range([height, 0]);

            // Grid lines
            svg.append("g")
                .attr("class", "grid")
                .attr("transform", `translate(0,${height})`)
                .call(d3.axisBottom(x)
                    .ticks(5)
                    .tickSize(-height)
                    .tickFormat(""))
                .selectAll("line")
                .attr("stroke", "#D0D1C9")
                .attr("stroke-width", 1)
                .attr("stroke-opacity", 0.5);

            svg.append("g")
                .attr("class", "grid")
                .call(d3.axisLeft(y)
                    .ticks(5)
                    .tickSize(-width)
                    .tickFormat(""))
                .selectAll("line")
                .attr("stroke", "#D0D1C9")
                .attr("stroke-width", 1)
                .attr("stroke-opacity", 0.5);

            // Add points
            svg.selectAll(".dot")
                .data(data.points)
                .enter().append("circle")
                .attr("class", "dot")
                .attr("cx", d => x(d.x))
                .attr("cy", d => y(d.y))
                .attr("r", 3)
                .attr("fill", PARTY_COLOURS[party])
                .attr("opacity", 0.7);

            // Add correlation line
            const slope = data.correlation * (data.yDev / data.xDev);
            const intercept = data.yMean - slope * data.xMean;

            svg.append("path")
                .datum([{ x: 0, y: intercept }, { x: 70, y: intercept + slope * 70 }])
                .attr("fill", "none")
                .attr("stroke", "#00A189")
                .attr("stroke-width", 2)
                .attr("stroke-dasharray", "3,3")
                .attr("d", d3.line()
                    .x(d => x(d.x))
                    .y(d => y(d.y)));

            // Year label
            svg.append("text")
                .attr("x", width / 2)
                .attr("y", -15)
                .attr("text-anchor", "middle")
                .style("font-size", "14px")
                .style("font-weight", "bold")
                .style("fill", "#1E3765")
                .text(data.year);

            // Axis labels only on first plot
            if (i === 0) {
                // Y-axis label
                svg.append("text")
                    .attr("x", -25)
                    .attr("y", height / 2)
                    .attr("text-anchor", "middle")
                    .attr("transform", "rotate(-90)")
                    .style("font-size", "12px")
                    .style("fill", "#1E3765")
                    .text("Conservative vote %");

                // X-axis label
                svg.append("text")
                    .attr("x", width / 2)
                    .attr("y", height + 35)
                    .attr("text-anchor", "middle")
                    .style("font-size", "12px")
                    .style("fill", "#1E3765")
                    .text("Immigrant population %");
            }
        });
    }
</script>

<div id="static-correlation-container">
    {#if !loaded}
        <div class="loading">Loading election data...</div>
    {:else if !electionData.length}
        <div class="error">No data available</div>
    {/if}
</div>

<style>
    #static-correlation-container {
        width: 100%;
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
        min-height: 350px;
    }

    .loading, .error {
        text-align: center;
        padding: 2rem;
        color: #666;
    }

    .error {
        color: #d32f2f;
    }

    .static-correlation-grid {
        display: flex;
        flex-direction: row; /* Explicit row direction */
        justify-content: space-around; /* Better space distribution */
        align-items: flex-start; /* Align items at the top */
        gap: 15px; /* Reduced gap */
        width: 100%;
        overflow: visible; /* Prevent any clipping */
    }

    .static-correlation-plot {
        flex: 0 0 30%; /* Don't grow, don't shrink, base 30% width */
        min-width: 0; /* Allows flex shrinking */
        box-sizing: border-box; /* Include padding in width */
    }

    @media (max-width: 900px) {
        .static-correlation-grid {
            flex-direction: column;
            align-items: center;
        }
        
        .static-correlation-plot {
            flex: 0 0 auto;
            width: 100%;
            max-width: 400px;
            margin-bottom: 20px;
        }
    }
</style>