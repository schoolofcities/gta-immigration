<script>
    import { scaleLinear, line } from 'd3';
    import { regressionLoess } from "d3-regression";
    import { onMount } from 'svelte';

    export let year;
    export let showYAxisLabel = false;
    export let showXAxisLabel = false;
    export let showXAxisTicks = false;

    let containerWidth = 600;
    const baseHeight = 125;
    const extraLabelSpace = 20;
    
    // Base margins (used for all graphs)
    const baseMargin = { top: 20, right: 30, bottom: 20, left: 50 };
    
    // Calculate actual height and margin based on whether we need the label space
    $: containerHeight = showXAxisLabel ? baseHeight + extraLabelSpace : baseHeight;
    $: margin = {
        ...baseMargin,
        bottom: showXAxisLabel ? baseMargin.bottom + extraLabelSpace : baseMargin.bottom
    };

    $: innerWidth = containerWidth - margin.left - margin.right;
    $: innerHeight = containerHeight - margin.top - margin.bottom;

    let data = [];

    onMount(async () => {
        const response = await fetch(`/gta-immigration/data/immigration_analysis/imm_dist_${year}.csv`);
        const csvText = await response.text();
        
        // Parse CSV data and add (0,0) point
        const rows = csvText.split('\n').slice(1); // Skip header
        const parsedData = rows.filter(row => row.trim() !== '').map(row => {
            const [dist_km, num_pop_tot, num_not_imm_tot, num_imm_tot] = row.split(',');
            return {
                dist_km: +dist_km,
                num_not_imm_tot: +num_not_imm_tot,
                num_imm_tot: +num_imm_tot
            };
        });

        // Add (0,0) point at the beginning
        data = [{ dist_km: 0, num_not_imm_tot: 0, num_imm_tot: 0 }, ...parsedData];
    });

    $: xScale = scaleLinear()
        .domain([0, 50])
        .range([0, innerWidth]);

    $: yScale = scaleLinear()
        .domain([0, 60000])
        .range([innerHeight, 0]);

    // Regression for non-immigrants
    $: notImmRegression = regressionLoess()
        .x(d => d.dist_km)
        .y(d => d.num_not_imm_tot)
        .bandwidth(0.3)(data);

    // Regression for immigrants
    $: immRegression = regressionLoess()
        .x(d => d.dist_km)
        .y(d => d.num_imm_tot)
        .bandwidth(0.3)(data);

    $: lineGenerator = line()
        .x(d => xScale(d[0]))
        .y(d => yScale(d[1]));
</script>

<div class="chart-container" bind:clientWidth={containerWidth}>
    {#if data.length > 0}
        <svg width={containerWidth} height={containerHeight}>
            <g transform={`translate(${margin.left},${margin.top})`}>
                <!-- Y-axis grid lines (horizontal) -->
                {#each [0, 30000, 60000] as tick}
                    <line
                        x1={0}
                        y1={yScale(tick)}
                        x2={innerWidth}
                        y2={yScale(tick)}
                        stroke="#e0e0e0"
                        stroke-width="1"
                    />
                {/each}

                <!-- X-axis grid lines (vertical) -->
                {#each [10, 20, 30, 40] as tick}
                    <line
                        x1={xScale(tick)}
                        y1={5}
                        x2={xScale(tick)}
                        y2={innerHeight - 5}
                        stroke="#e0e0e0"
                        stroke-width="1"
                    />
                {/each}

                <!-- X-axis ticks and labels -->
                {#if showXAxisTicks}
                    <g transform={`translate(0,${innerHeight})`}>
                        {#each [0, 10, 20, 30, 40, 50] as tick}
                            <text
                                class="tick-label"
                                x={xScale(tick)}
                                y={15}  
                                text-anchor="middle"
                                font-size="12"
                            >
                                {tick}
                            </text>
                        {/each}
                    </g>
                {/if}

                <!-- Y-axis ticks and labels -->
                <g>
                    {#each [0, 30000, 60000] as tick}
                        <text
                            class="tick-label"
                            x={-10}  
                            y={yScale(tick)}
                            text-anchor="end"
                            dominant-baseline="middle"
                            font-size="12"
                        >
                            {tick === 0 ? '0' : tick/1000 + 'K'}
                        </text>
                    {/each}
                </g>

                <!-- Y-axis label (conditional) -->
                {#if showYAxisLabel}
                    <text
                        class="axis-label"
                        x={-40}  
                        y={innerHeight / 2}
                        text-anchor="middle"
                        transform="rotate(-90, -40, {innerHeight / 2})"
                        font-size="12"
                    >
                        Population
                    </text>
                {/if}

                <!-- X-axis label (conditional) -->
                {#if showXAxisLabel}
                    <text
                        class="axis-label"
                        x={innerWidth / 2}
                        y={innerHeight + 35}  
                        text-anchor="middle"
                        font-size="12"
                    >
                        Distance (km)
                    </text>
                {/if}

                <!-- Regression lines -->
                <path
                    d={lineGenerator(notImmRegression)}
                    fill="none"
                    stroke="#0D534D"
                    stroke-width="2"
                />

                <path
                    d={lineGenerator(immRegression)}
                    fill="none"
                    stroke="#F1C500"
                    stroke-width="2"
                />
            </g>
        </svg>
    {/if}
</div>

<style>
    .chart-container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
    }

    .tick-label {
        fill: #000;
        font-size: 12px;
    }

    .axis-label {
        fill: #000;
    }
</style>