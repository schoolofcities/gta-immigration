<script>
    import { scaleLinear } from 'd3-scale';
    import { mean, deviation } from 'd3-array';
    import { PARTY_SHADES } from './constants';
    
    let {
        points,
        correlation = 0,
        year,
        showArrows = false,
    } = $props();

    const plotWidth = 300;
    const height = 200;

    const scales = {
        x: scaleLinear().domain([0, 70]).range([0, plotWidth]),
        y: scaleLinear().domain([0, 80]).range([height, 0])
    };
  
    const correlationLine = (() => {
        const xMean = mean(points, d => d.x);
        const yMean = mean(points, d => d.y);
        const xDev = deviation(points, d => d.x);
        const yDev = deviation(points, d => d.y);
        
        const slope = correlation * (yDev / xDev);
        const intercept = yMean - slope * xMean;
        
        return {
            x1: scales.x(0),
            y1: scales.y(intercept),
            x2: scales.x(70),
            y2: scales.y(slope * 70 + intercept)
        };
    })();
  
    // Arrow positioning 
    const arrowX = 20; 
    const lineHeight = 12;
</script>
  
<div class="scatter-plot" style="width: {plotWidth}px; height: {height}px;">
    <svg width={plotWidth} {height}>
        <!-- Arrowhead definition -->
        <defs>
            <marker
                id="arrowhead"
                viewBox="0 -5 10 10"
                refX="5"
                refY="0"
                markerWidth="6"
                markerHeight="6"
                orient="auto"
            >
                <path d="M0,-5L10,0L0,5" fill="black" />
            </marker>
        </defs>
  
        <!-- Grid lines -->
        {#each [20, 40, 60] as value}
            <line
                x1={scales.x(value)}
                y1={0}
                x2={scales.x(value)}
                y2={height}
                stroke="#eee"
                stroke-width="1"
            />
            <line
                x1={0}
                y1={scales.y(value)}
                x2={plotWidth}
                y2={scales.y(value)}
                stroke="#eee"
                stroke-width="1"
            />
        {/each}
      
        <!-- Correlation line -->
        <line
            x1={correlationLine.x1}
            y1={correlationLine.y1}
            x2={correlationLine.x2}
            y2={correlationLine.y2}
            stroke="#666"
            stroke-width="1"
            stroke-dasharray="2,2"
        />
      
        <!-- Data points -->
        {#each points as point}
            <circle
                cx={scales.x(point.x)}
                cy={scales.y(point.y)}
                r={3}
                fill={PARTY_SHADES.cons1[6]}
                fill-opacity="1"
            />
        {/each}
  
        <!-- Arrows and labels -->
        {#if showArrows}
            <!-- Horizontal arrow (More immigrants) -->
            <line
                x1={scales.x(15)}
                y1={height - 15}
                x2={scales.x(55)}
                y2={height - 15}
                stroke="black"
                stroke-width="1"
                marker-end="url(#arrowhead)"
            />
            <text
                x={scales.x(50)}
                y={height - 3}
                text-anchor="middle"
                font-size="11px"
                font-family=""
                fill="black"
            >
                More immigrants
            </text>
    
            <!-- Vertical arrow (More conservative) -->
            <line
                x1={arrowX}
                y1={scales.y(25)}
                x2={arrowX}
                y2={scales.y(75)}
                stroke="black"
                stroke-width="1"
                marker-end="url(#arrowhead)"
            />
            <text
                x={arrowX + 5}
                y={scales.y(75)}
                font-size="11px"
                font-family=""
                fill="black"
            >
                More
            </text>
            <text
                x={arrowX + 5}
                y={scales.y(70)}
                font-size="11px"
                font-family=""
                fill="black"
            >
                conservative
            </text>
        {/if}
      
        <!-- Year label -->
        <text x={scales.x(35)} y={20} text-anchor="middle" font-size="14" fill="black">
            {year}
        </text>
    </svg>
</div>
  
<style>
    .scatter-plot {
        margin: 0 auto;
        background-color: white;
    }
    
    svg {
        display: block;
        background-color: white;
    }

    text {
        font-family: TradeGothicBold;
    }
</style>