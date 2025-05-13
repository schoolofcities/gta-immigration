<script>
    import { scaleLinear } from 'd3-scale';
    import { mean, deviation } from 'd3-array';
    import { PARTY_SHADES } from './constants';
    import * as d3 from 'd3';
    
    let {
        points,
        correlation = 0,
        year,
        xEnd = 70,
        height = 100,
        plotWidth = 100,
        colorStart = -1.5,
        colorEnd = 0.35,
    } = $props();

    const scales = {
        x: scaleLinear().domain([0, xEnd]).range([0, plotWidth]),
        y: scaleLinear().domain([0, 80]).range([height, 0])
    };

    const colorScale = d3.scaleLinear()
        .domain([colorStart, 0, colorEnd])
        .range(["#4d4d4d","#D0D1C9", "#007FA3"])
        .interpolate(d3.interpolateLab);
  
    const xMean = mean(points, d => d.x);
    const yMean = mean(points, d => d.y);
    const xDev = deviation(points, d => d.x);
    const yDev = deviation(points, d => d.y);
    
    const slope = correlation * (yDev / xDev);
    const intercept = yMean - slope * xMean;

    const correlationLine = (() => {
        return {
            x1: scales.x(0),
            y1: scales.y(intercept),
            x2: scales.x(xEnd),
            y2: scales.y(slope * xEnd + intercept)
        };
    })();
  
    // Arrow positioning 
    const arrowX = 20; 
    const lineHeight = 12;
</script>
  
<div class="scatter-plot" style="width: {plotWidth}px; height: {height}px;">
    <svg
        width={plotWidth}
        height={height}
        style="background-color: {colorScale(slope)}"
    >
        <!-- Data points -->
        {#each points as point}
            <circle
                cx={scales.x(point.x)}
                cy={scales.y(point.y)}
                r={2}
                fill={"white"}
                fill-opacity="0.75"
            />
        {/each}

        <!-- Correlation line -->
        <line
            x1={correlationLine.x1}
            y1={correlationLine.y1}
            x2={correlationLine.x2}
            y2={correlationLine.y2}
            stroke="#ffffff"
            stroke-width="5"
            stroke-linecap="round"
        />
      
        <!-- Year label -->
        <text class="scatter-title" x={scales.x(xEnd / 2)} y={15} font-size=14>
            {year}
        </text>
    </svg>
</div>
  
<style>
    .scatter-plot {
        margin: 0 auto;
        /* background-color: #6FC7EA; */
        /* border-left: solid 2px #D0D1C9; */
        /* border-bottom: solid 2px #D0D1C9; */
    }
    
    svg {
        display: block;
        /* background-color: #6FC7EA; */
    }

    .scatter-title {
        font-family: TradeGothicBold;
        fill: white;
        text-anchor: middle;
    }
</style>