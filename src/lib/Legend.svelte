<script>
    let { 
        title = "", 
        colors = [], 
        labels = [] 
    } = $props();
    
    const LEGEND_WIDTH = 350;
    const LEGEND_HEIGHT = 70;
    const RECT_HEIGHT = 15;
    
    // Calculate rectangle width dynamically based on number of colors
    let RECT_WIDTH = $derived(LEGEND_WIDTH / colors.length);
    
    // Calculate positions for rectangles and labels
    let rectXPositions = $derived(Array.from({length: colors.length}, (_, i) => i * RECT_WIDTH));
    
    // Position labels at rectangle boundaries instead of centers
    let labelXPositions = $derived(Array.from({length: labels.length}, (_, i) => i * RECT_WIDTH));
</script>

<div class="legend">
    <svg width={LEGEND_WIDTH} height={LEGEND_HEIGHT}>
        <text class="legend-title" x="0" y="18">{title}</text>
        
        {#each colors as color, i}
            <rect 
                x={rectXPositions[i]} 
                y="25" 
                width={RECT_WIDTH} 
                height={RECT_HEIGHT} 
                fill={color}
                stroke="#FFFFFF"
                stroke-width="1"
            />
        {/each}
        
        {#each labels as label, i}
            <text 
                class="legend-label" 
                x={labelXPositions[i]} 
                y="55" 
                text-anchor="start"
            >
                {label}
            </text>
        {/each}
    </svg>
</div>

<style>
    .legend {
        border-top: solid 1px #f0f0f0;
        margin: 0 auto;
        margin-top: 10px;
        margin-bottom: 10px;
        max-width: 1000px;
        width: 100%;
        height: 60px;
        padding: 0px;
        padding-top: 10px;
        text-align: center;
    }

    .legend-title {
        font-family: 'RobotoBold', sans-serif;
        font-weight: normal;
        font-size: 17px;
        fill: var(--brandBlack);
    }

    .legend-label {
        font-family: 'Roboto', sans-serif;
        font-weight: normal;
        font-size: 14px;
        fill: var(--brandDarkBlue);
    }
</style>
