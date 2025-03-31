<script>
    import { PARTIES_INFO, PARTY_COLOURS } from "../lib/constants.js";
    import * as d3 from 'd3';

    const parties = PARTIES_INFO.filter(party => party.name !== 'Reform/Alliance');

    // State variables
    let curRegion = $state("federal");
    let curCorrs = $state({
        "Liberals": [], // contains elements of the form [year, corr]
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

    function drawGraph() {
        const svg = d3.select("#correlation-line-graph");
        svg.selectAll("*").remove();

        const containerWidth = svg.node().parentElement.getBoundingClientRect().width || 700;
        const margin = { 
            top: 20, 
            right: containerWidth <= 700 ? 40 : 30, // Increase right margin for smaller screens
            bottom: 50, 
            left: 60 
        };
        const width = Math.min(containerWidth, 700) - margin.left - margin.right;
        const height = 400 - margin.top - margin.bottom;

        svg.attr("width", width + margin.left + margin.right)
           .attr("height", height + margin.top + margin.bottom);

        const g = svg.append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        // Get all years from all parties' data
        const allYears = [];
        Object.values(curCorrs).forEach(partyData => {
            partyData.forEach(item => {
                if (!allYears.includes(item[0])) {
                    allYears.push(item[0]);
                }
            });
        });
        allYears.sort();

        const xScale = d3.scalePoint()
            .domain(allYears)
            .range([0, width]);

        const yScale = d3.scaleLinear()
            .domain([-1, 1]) // Correlation ranges from -1 to 1
            .range([height, 0]);

        // Modified x-axis
        g.append("g")
            .attr("transform", `translate(0,${height})`)
            .call(d3.axisBottom(xScale).tickFormat(d3.format("d")))
            .selectAll("text")
            .style("text-anchor", containerWidth <= 700 ? "end" : "middle")
            .attr("dx", containerWidth <= 700 ? "-0.8em" : "0")
            .attr("dy", containerWidth <= 700 ? "0.15em" : "0.71em")
            .attr("transform", containerWidth <= 700 ? "rotate(-45)" : "rotate(0)");

        // Year label
        g.append("text")
            .attr("fill", "#000")
            .attr("x", width / 2)
            .attr("y", height + (containerWidth <= 700 ? 45 : 40))
            .attr("text-anchor", "middle")
            .style("font-size", "11px")
            .text("Election year");

        // Modified y-axis with all ticks
        g.append("g")
            .call(d3.axisLeft(yScale))
            .append("text")
            .attr("fill", "#000")
            .attr("transform", "rotate(-90)")
            .attr("y", -50)
            .attr("x", -height / 2)
            .attr("dy", "0.71em")
            .attr("text-anchor", "middle")
            .style("font-size", "11px")
            .text("Correlation");

        // Add dotted black line at y = 0
        g.append("line")
            .attr("x1", 0)
            .attr("x2", width)
            .attr("y1", yScale(0))
            .attr("y2", yScale(0))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("stroke-dasharray", "4,4");

        // Add arrowhead definition
        svg.append("defs").append("marker")
            .attr("id", "arrowhead")
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 5)
            .attr("refY", 0)
            .attr("markerWidth", 6)
            .attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("path")
            .attr("d", "M0,-5L10,0L0,5")
            .attr("fill", "black");

        // Position arrows based on screen width
        const arrowX = windowWidth <= 700 ? 10 : 20;
        const lineHeight = 12; // Height between text lines
        const textOffset = windowWidth <= 700 ? 3 : 5; // Smaller offset on mobile

        // Add up arrow (Overperforming)
        g.append("line")
            .attr("x1", arrowX)
            .attr("x2", arrowX)
            .attr("y1", yScale(0.2))
            .attr("y2", yScale(0.9))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("marker-end", "url(#arrowhead)");

        // Overperforming label - line 1
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(0.85))
            .attr("dy", "0")
            .style("font-size", "10px")
            .text("More votes where");
        
        // Overperforming label - line 2
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(0.85))
            .attr("dy", lineHeight + "px")
            .style("font-size", "10px")
            .text("immigrants live");

        // Add down arrow (Underperforming)
        g.append("line")
            .attr("x1", arrowX)
            .attr("x2", arrowX)
            .attr("y1", yScale(-0.2))
            .attr("y2", yScale(-0.9))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("marker-end", "url(#arrowhead)");

        // Underperforming label - line 1
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(-0.85))
            .attr("dy", "0")
            .style("font-size", "10px")
            .text("Less votes where");
        
        // Underperforming label - line 2
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(-0.85))
            .attr("dy", lineHeight + "px")
            .style("font-size", "10px")
            .text("immigrants live");

        const line = d3.line()
            .x(d => xScale(d[0]))
            .y(d => yScale(d[1]))
            .curve(d3.curveMonotoneX);

        // Draw lines and dots for each party
        parties.forEach(party => {
            const partyData = curCorrs[party.name];
            if (!partyData || partyData.length === 0) return;

            g.append("path")
                .datum(partyData)
                .attr("fill", "none")
                .attr("stroke", PARTY_COLOURS[party.tag])
                .attr("stroke-width", 1.5)
                .attr("d", line);

            g.selectAll(`.timeline-correlation-dot-${party.tag}`)
                .data(partyData)
                .enter()
                .append("circle")
                .attr("class", `timeline-correlation-dot-${party.tag}`)
                .attr("r", 3.5)
                .attr("cx", d => xScale(d[0]))
                .attr("cy", d => yScale(d[1]))
                .attr("fill", PARTY_COLOURS[party.tag]);
        });
    }

    $effect(() => {
        curCorrs;
        windowWidth;
        drawGraph();
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

<svg id="correlation-line-graph" height="400"></svg>

<style>
    svg {
        max-width: 100%;
    }
</style>