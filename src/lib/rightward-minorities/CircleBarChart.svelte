<script>
    import { PARTY_COLOURS } from '$lib/constants';
    import { scaleLinear } from 'd3-scale';

    export let info;
    export let data;
    export let vmField;

    let containerWidth = 300;
    const containerHeight = 170;
    const margin = { top: 30, right: 5, bottom: 20, left: 6 };

    $: innerWidth = containerWidth - margin.left - margin.right;
    $: innerHeight = containerHeight - margin.top - margin.bottom;

    // Fixed vertical layout parameters
    const rowHeight = 24;
    const barHeight = 8;
    const dotSize = 6;
    const startY = 10;

    $: xScale = scaleLinear()
        .domain([0, 75])
        .range([0, innerWidth]);

    $: regionName = info.region === 'ont-' ? 'Ontario' : 'Federal';
    $: vmName = info.vm_type === 'sa' ? 'South Asian' : 'Chinese';
    $: title = `${regionName} ${info.year}`;
</script>

<div class="chart-container" bind:clientWidth={containerWidth}>
    {#if data}
        <svg width={containerWidth} height={containerHeight}>
            <g transform={`translate(${margin.left},${margin.top})`}>
                <!-- X-axis grid lines -->
                {#each [20, 40, 60] as tick}
                    <line
                        x1={xScale(tick)}
                        y1={0}
                        x2={xScale(tick)}
                        y2={innerHeight}
                        stroke="#4d4d4d"
                        stroke-width="0.25"
                    />
                {/each}               

                <!-- X-axis labels -->
                <g transform={`translate(0,${innerHeight})`}>
                    {#each [0, 20, 40, 60] as tick}
                        <text
                            class="bar-chart-tick"
                            x={xScale(tick) + 1}
                            y={12}
                            font-size="11"
                        >
                            {tick}%
                        </text>
                    {/each}
                </g>

                <!-- Title -->
                <text 
                    class="bar-chart-title" 
                    x={-2} 
                    y={-15} 
                    font-size=14
                >
                    {title} election
                </text>

                <!-- Visible minority dot / bar -->
                {#each data as d, i}
                    <!-- <circle
                        cx={xScale(+d[vmField])}
                        cy={startY + i * rowHeight}
                        r={dotSize}
                        fill="#00A189"
                        stroke="white"
                        stroke-width="0"
                    /> -->
                    <rect
                        x={0}
                        y={startY + i * rowHeight - barHeight/2}
                        width={xScale(+d[vmField])}
                        height={barHeight * 2}
                        fill={"#F1C500"}
                        rx={1}
                        ry={1}
                    />
                {/each}

                <!-- Conservative vote bar -->
                {#each data as d, i}
                    <rect
                        x={0}
                        y={startY + i * rowHeight + 1}
                        width={xScale(+d.cons1_pct)}
                        height={barHeight / 1.25}
                        fill={"#007FA3"}
                        rx={1}
                        ry={1}
                    />
                {/each}

                <!-- Conservative total line -->
                <line
                    x1={xScale(info.pct_cons_total)}
                    y1={-8}
                    x2={xScale(info.pct_cons_total)}
                    y2={innerHeight + 5}
                    stroke="#007FA3"
                    stroke-width="2"
                    stroke-dasharray="4,2"
                    opacity="1"
                />

                <!-- thicker base line at x=0% -->
                <line
                    x1={xScale(0)}
                    y1={0}
                    x2={xScale(0)}
                    y2={innerHeight}
                    stroke="#191919"
                    stroke-width="1"
                />

                {#if title =='Ontario 2014'}
                    <text 
                        class="bar-chart-label" 
                        x={xScale(info.pct_cons_total) + 2} 
                        y={2} 
                        font-size=14
                    >
                        National average
                    </text>
                {/if}

            </g>
        </svg>
    {/if}
</div>

<style>
    .chart-container {
        height: 160px;
        padding-top: 10px;
        min-width: 0;
    }

    .bar-chart-tick {
        /* font-family: TradeGothicLTLight; */
        fill: black;
        text-anchor: middle;
    }

    .bar-chart-title {
        font-family: TradeGothicBold;
        fill: black;
        text-anchor: left;
    }

    .bar-chart-label {
        font-family: TradeGothicBold;
        fill: var(--brandMedBlue);
        text-anchor: left;
    }
</style>