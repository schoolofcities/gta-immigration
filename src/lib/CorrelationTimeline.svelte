<script>
    import { onMount } from "svelte";
    import { PARTIES_INFO, PARTY_COLOURS } from "../lib/constants.js";
    import * as d3 from 'd3';

    const parties = PARTIES_INFO.filter(party => party.name !== 'Reform/Alliance');

    let curRegion = $state("federal");
    let curCorrs = $state({
        "Liberals": [],  // contains elements of the form [year, corr]
        "Conservatives": [],
        "New Democrats": [],
    });
    let windowWidth = $state(window.innerWidth);

    window.addEventListener('resize', () => windowWidth = window.innerWidth);

    function handleRegionChange(event) {
        curRegion = event.target.value;
    }

    // Function to update correlations based on the selected curRegion
    function updateCorrelations() {
        d3.csv('/gta-immigration/data/elections_analysis/ed_corrs.csv').then(data => {
            const filteredData = data.filter(row => row.region === curRegion);

            // Update the curCorrs state variable
            curCorrs = {
                "Liberals": filteredData.map(row => [parseInt(row.year), parseFloat(row.corr_pct_imm_lib)]),
                "Conservatives": filteredData.map(row => [parseInt(row.year), parseFloat(row.corr_pct_imm_cons1)]),
                "New Democrats": filteredData.map(row => [parseInt(row.year), parseFloat(row.corr_pct_imm_ndp)]),
            };
        }).catch(error => {
            console.error('Error loading or processing CSV data:', error);
        });
    }

    // Function to draw the line graph
    function drawGraph() {
        // Clear the existing SVG content
        d3.select("#correlation-line-graph").selectAll("*").remove();

        // Set up SVG dimensions
        const container = document.getElementById("correlation-line-graph").parentElement;
        const width = container.clientWidth;
        const height = 400;
        const margin = { top: 20, right: 30, bottom: 50, left: 60 };

        // Create the SVG container with viewBox for responsiveness
        const svg = d3.select("#correlation-line-graph")
            .attr("viewBox", `0 0 ${width} ${height}`)
            .attr("preserveAspectRatio", "xMidYMid meet");

        // Get all unique years from curCorrs
        const allYears = [...new Set(Object.values(curCorrs).flatMap(data => data.map(d => d[0])))];

        // Create scales
        const xScale = d3.scalePoint()
            .domain(allYears) // Use all available years
            .range([margin.left, width - margin.right]);

        const yScale = d3.scaleLinear()
            .domain([-1, 1]) // Correlation ranges from -1 to 1
            .range([height - margin.bottom, margin.top]);

        // Create axes
        const xAxis = d3.axisBottom(xScale).tickFormat(d3.format("d")); // Format years as integers
        const yAxis = d3.axisLeft(yScale);

        // Modify x-axis rendering - separate ticks and label
        const xAxisGroup = svg.append("g")
            .attr("transform", `translate(0,${height - margin.bottom})`)
            .call(xAxis);
        
        // Style the tick labels
        xAxisGroup.selectAll("text")
            .style("text-anchor", width <= 700 ? "end" : "middle")
            .attr("dx", width <= 700 ? "-0.8em" : "0")
            .attr("dy", width <= 700 ? "0.15em" : "0.71em")
            .attr("transform", width <= 700 ? "rotate(-45)" : "rotate(0)");

        // Add x-axis label separately
        xAxisGroup.append("text")
            .attr("fill", "#000")
            .attr("transform", `translate(${(width - margin.left - margin.right) / 2 + margin.left}, 40)`)
            .attr("text-anchor", "middle")
            .text("Election year");

        // Add the y-axis
        svg.append("g")
            .attr("transform", `translate(${margin.left},0)`)
            .call(yAxis)
            .append("text")
            .attr("fill", "#000")
            .attr("transform", "rotate(-90)")
            .attr("y", -50)
            .attr("x", -height / 2)
            .attr("dy", "0.71em")
            .attr("text-anchor", "middle")
            .text("Correlation");

        // Add dotted black line at y = 0
        svg.append("line")
            .attr("x1", margin.left)
            .attr("x2", width - margin.right)
            .attr("y1", yScale(0))
            .attr("y2", yScale(0))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("stroke-dasharray", "4,4");

        // Define a line generator
        const line = d3.line()
            .x(d => xScale(d[0]))
            .y(d => yScale(d[1]));

        // Draw lines and dots for each selected party
        parties.forEach(party => {
            const data = curCorrs[party.name];
            if (!data) return;

            // Draw the line
            svg.append("path")
                .datum(data)
                .attr("fill", "none")
                .attr("stroke", PARTY_COLOURS[party.tag] || "black") // Fallback to black if color is missing
                .attr("stroke-width", 2)
                .attr("d", line);

            // Draw dots for each data point with a more specific class name
            svg.selectAll(`.timeline-correlation-dot-${party.tag}`)
                .data(data)
                .enter()
                .append("circle")
                .attr("class", `timeline-correlation-dot-${party.tag}`)
                .attr("cx", d => xScale(d[0]))
                .attr("cy", d => yScale(d[1]))
                .attr("r", 4)
                .attr("fill", PARTY_COLOURS[party.tag])
                .attr("stroke", "none");  // Explicitly set no stroke
        });
    }

    $effect(() => {
        windowWidth;
        curCorrs;
        if (Object.values(curCorrs).some(arr => arr.length > 0)) {
            drawGraph();
        }
    });

    $effect(() => {
        curRegion;
        updateCorrelations();
    });
</script>

<div>
    <div class="sentence-controls">
        <p>
            Show me the correlation between party vote share and percent immigrants over time for the
            <select onchange={handleRegionChange} class="inline-select">
                <option value="federal" selected>federal</option>
                <option value="ontario">ontario</option>
            </select>
            level.
        </p>
    </div>
</div>

<!-- SVG container for the graph -->
<svg id="correlation-line-graph"></svg>

<style>
    svg {
        width: 100%;
        height: auto;
        max-width: 100%;
    }
</style>