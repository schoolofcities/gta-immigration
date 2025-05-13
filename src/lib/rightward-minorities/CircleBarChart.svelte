<script>
    import { PARTY_COLOURS } from '$lib/constants';
    import { scaleLinear } from 'd3-scale';

    export let info;
    export let data;
    export let vmField;

    let containerWidth = 300;
    const containerHeight = 134;
    const margin = { top: 20, right: 5, bottom: 20, left: 6 };

    $: innerWidth = containerWidth - margin.left - margin.right;
    $: innerHeight = containerHeight - margin.top - margin.bottom;

    // Fixed vertical layout parameters
    const rowHeight = 18;
    const barHeight = 14;
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
                {#each [0, 20, 40, 60] as tick}
                    <line
                        x1={xScale(tick)}
                        y1={0}
                        x2={xScale(tick)}
                        y2={innerHeight}
                        stroke="#e0e0e0"
                        stroke-width="0.5"
                    />
                {/each}

                <!-- X-axis labels -->
                <g transform={`translate(0,${innerHeight})`}>
                    {#each [0, 20, 40, 60] as tick}
                        <text
                            class="bar-chart-tick"
                            x={xScale(tick)}
                            y={10}
                            font-size="9"
                        >
                            {tick}%
                        </text>
                    {/each}
                </g>

                <!-- Title -->
                <text class="bar-chart-title" x={innerWidth / 2} y={-5} font-size=14>
                    {title}
                </text>

                <!-- Conservative vote bar -->
                {#each data as d, i}
                    <rect
                        x={0}
                        y={startY + i * rowHeight - barHeight/2}
                        width={xScale(+d.cons1_pct)}
                        height={barHeight}
                        fill={PARTY_COLOURS.cons1}
                        rx={1}
                        ry={1}
                    />
                {/each}

                <!-- Conservative total line -->
                <line
                    x1={xScale(info.pct_cons_total)}
                    y1={0}
                    x2={xScale(info.pct_cons_total)}
                    y2={innerHeight}
                    stroke="#000000"
                    stroke-width="1"
                    stroke-dasharray="4,3"
                    opacity="1"
                />

                <!-- Visible minority dot -->
                {#each data as d, i}
                    <circle
                        cx={xScale(+d[vmField])}
                        cy={startY + i * rowHeight}
                        r={dotSize}
                        fill="#00A189"
                        stroke="white"
                        stroke-width="0"
                    />
                {/each}
            </g>
        </svg>
    {/if}
</div>

<style>
    .chart-container {
        height: 160px;
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
        text-anchor: middle;
    }
</style>