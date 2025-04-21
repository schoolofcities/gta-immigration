<script>
    import { PARTIES_INFO, PARTY_COLOURS } from "../lib/constants.js";
    import * as d3 from 'd3';
    import { browser } from '$app/environment';

    const parties = PARTIES_INFO.filter(party => party.name !== 'Reform/Alliance');

    // State variables
    let curRegion = $state("ontario");
    let curCorrs = $state({
        "Liberals": [], // contains elements of the form [year, corr]
        "Conservatives": [],
        "New Democrats": [],
    });

    let windowWidth = $state(0);

    // Use $effect to run only in the browser environment
    $effect(() => {
        if (!browser) return; // Don't run on the server

        // Set the initial width value
        windowWidth = window.innerWidth;

        // Define the function to update the width
        const updateWidth = () => windowWidth = window.innerWidth;

        // Add the resize event listener
        window.addEventListener('resize', updateWidth);

        // Clean up the event listener when the component is destroyed
        return () => {
            window.removeEventListener('resize', updateWidth);
        };
    });

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

    function setLabelPos(partyName, region) {
        let dx;
        let dy;
        let textAnchor = "start";

        if (region === 'ontario') {
            if (partyName === "Liberals") {
                dx = 5; // to the right
                dy = -5; // slightly above
            } else if (partyName === "New Democrats") {
                dx = 5; // to the right
                dy = 0; // middle height
            } else if (partyName === "Conservatives") {
                dx = 5; // to the right
                dy = 10; // slightly below
            }
        } else { // federal
            if (partyName === "Liberals") {
                dx = -20; // to the left
                dy = -5; // slightly above
            } else if (partyName === "New Democrats") {
                dx = 5; // to the right
                dy = -5; // slightly above
            } else if (partyName === "Conservatives") {
                dx = 5; // to the right
                dy = 10; // slightly below
            }
        }

        return { dx, dy, textAnchor };
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
            .domain([-0.98, 0.98]) // Correlation ranges from -1 to 1
            .range([height, 0]);

        // Add x-axis grid lines
        g.selectAll(".x-grid-line")
            .data(allYears)
            .enter()
            .append("line")
            .attr("class", "x-grid-line")
            .attr("x1", d => xScale(d))
            .attr("x2", d => xScale(d))
            .attr("y1", 0)
            .attr("y2", height)
            .attr("stroke", "#d3d3d3")
            .attr("stroke-width", 0.5);

        // Add y-axis grid lines
        g.selectAll(".y-grid-line")
            .data([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]) // Specific ticks
            .enter()
            .append("line")
            .attr("class", "y-grid-line")
            .attr("x1", 0)
            .attr("x2", width)
            .attr("y1", d => yScale(d))
            .attr("y2", d => yScale(d))
            .attr("stroke", "#d3d3d3")
            .attr("stroke-width", 0.5);

        // Modified x-axis with proper mobile rotation
        const xAxis = g.append("g")
            .attr("transform", `translate(0,${height})`)
            .call(d3.axisBottom(xScale)
                .tickFormat(d3.format("d"))
                .tickSize(0));
        
        xAxis.select(".domain").remove();
        
        // Add subtle tick marks that match grid lines (only on mobile)
        if (containerWidth <= 700) {
            xAxis.selectAll(".tick")
                .append("line")
                .attr("class", "x-tick-line")
                .attr("x1", 0)
                .attr("x2", 0)
                .attr("y1", 0)
                .attr("y2", 6)
                .attr("stroke", "#d3d3d3")
                .attr("stroke-width", 0.5);
        }

        // Style x-axis labels
        xAxis.selectAll("text")
            .style("font-size", "11px")
            .style("font-family", "RobotoRegular")
            .style("text-anchor", containerWidth <= 700 ? "end" : "middle")
            .attr("dx", containerWidth <= 700 ? "-0.5em" : "0")
            .attr("dy", containerWidth <= 700 ? "1.2em" : "0.71em")
            .attr("transform", containerWidth <= 700 ? "rotate(-45)" : "rotate(0)");

        // Modified y-axis with specific ticks
        const yAxis = g.append("g")
            .attr("transform", "translate(-5,0)")
            .call(d3.axisLeft(yScale)
                .tickValues([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75])
                .tickFormat(d => d.toFixed(2)) // Show 2 decimal places
                .tickSize(0))
            .select(".domain").remove();

        // Style y-axis tick labels
        yAxis.selectAll("text")
            .attr("fill", "#666")
            .style("font-size", "11px")
            .style("font-family", "RobotoRegular");

        // Add y-axis label
        g.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", -50)
            .attr("x", -height / 2)
            .attr("dy", "0.71em")
            .attr("text-anchor", "middle")
            .style("font-size", "13px")
            .style("font-family", "RobotoRegular")
            .text("Correlation");

        // Add dotted black line at y = 0
        g.append("line")
            .attr("x1", 0)
            .attr("x2", width)
            .attr("y1", yScale(0))
            .attr("y2", yScale(0))
            .attr("stroke", "#D0D1C9")
            .attr("stroke-width", 2);

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
        const lineHeight = 15;
        const textOffset = 8;

        // Add up arrow (Positive correlation)
        g.append("line")
            .attr("x1", arrowX)
            .attr("x2", arrowX)
            .attr("y1", yScale(0.2))
            .attr("y2", yScale(0.95))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("marker-end", "url(#arrowhead)");

        // Positive correlation label - line 1
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(0.85))
            .attr("dy", "0")
            .style("font-size", "14px")
            .style("font-family", "RobotoRegular")
            .text("More votes where");
        
        // Positive correlation label - line 2
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(0.85))
            .attr("dy", lineHeight + "px")
            .style("font-size", "14px")
            .style("font-family", "RobotoRegular")
            .text("immigrants live");

        // Add down arrow (Negative correlation)
        g.append("line")
            .attr("x1", arrowX)
            .attr("x2", arrowX)
            .attr("y1", yScale(-0.2))
            .attr("y2", yScale(-0.9))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("marker-end", "url(#arrowhead)");

        // Negative correlation label - line 1
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(-0.82))
            .attr("dy", "0")
            .style("font-size", "14px")
            .style("font-family", "RobotoRegular")
            .text("Fewer votes where");
        
        // Negative correlation label - line 2
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(-0.82))
            .attr("dy", lineHeight + "px")
            .style("font-size", "14px")
            .style("font-family", "RobotoRegular")
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

            // Add party labels based on the requirements
            const labelIndex = curRegion === 'ontario' ? 9 : 12;
            if (partyData.length > labelIndex) {
                const labelData = partyData[labelIndex];
                const xPos = xScale(labelData[0]);
                const yPos = yScale(labelData[1]);
                
                const { dx, dy, textAnchor } = setLabelPos(party.name, curRegion);

                g.append("text")
                    .attr("x", xPos)
                    .attr("y", yPos)
                    .attr("dx", dx)
                    .attr("dy", dy)
                    .attr("text-anchor", textAnchor)
                    .style("font-size", "14px")
                    .style("font-family", "RobotoRegular")
                    .style("fill", PARTY_COLOURS[party.tag])
                    .style("stroke", "white")
                    .style("stroke-width", "4px")
                    .text(party.name);

                g.append("text")
                    .attr("x", xPos)
                    .attr("y", yPos)
                    .attr("dx", dx)
                    .attr("dy", dy)
                    .attr("text-anchor", textAnchor)
                    .style("font-size", "14px")
                    .style("font-family", "RobotoRegular")
                    .style("fill", PARTY_COLOURS[party.tag])
                    .text(party.name);
            }
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

<div style="margin-bottom: -20px; margin-top: -25px;">
    <div class="sentence-controls">
        <p>
            Show how the correlation between party vote share and percentage of immigrants in each riding changes over time in all
            <select onchange={handleRegionChange} class="inline-select">
                <option value="federal">federal</option>
                <option value="ontario" selected>Ontario</option>
            </select>
            elections.
        </p>
    </div>

<svg id="correlation-line-graph" height="400"></svg>

</div>

<style>
    svg {
        max-width: 100%;
        font-family: RobotoRegular;
    }
</style>