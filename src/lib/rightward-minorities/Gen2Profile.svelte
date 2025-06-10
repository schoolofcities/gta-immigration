<script>
    import { PARTY_NAMES_SHORT, PARTY_COLOURS } from "$lib/constants";
    import { parseMarkdown } from "$lib/footnoteUtils";

    let {
        profile,
        showLabels = false,
        electionLabels = [],
    } = $props();
    
    let containerWidth = $state(340);
    let availableWidth = $derived(containerWidth - 20);
    let rectWidth = $derived(Math.max(40, Math.floor(availableWidth / 5)));
    
    // Always use the same dimensions regardless of showLabels
    const rectHeight = 30;
    const svgHeight = 40; 
    const textYOffset = 32; 
    const rectsYPosition = 15;
</script>

<div class="profile-container" bind:clientWidth={containerWidth}>
    
    <svg width="100%" height={svgHeight} viewBox={`0 0 ${rectWidth * 5} ${svgHeight}`} preserveAspectRatio="xMinYMin meet">
        <!-- Always reserve space for labels, only show when flag is true -->
        {#each electionLabels as label, i}
            <text 
                x={i * rectWidth + rectWidth/2} 
                y="12" 
                text-anchor="middle"
                font-size="11" 
                opacity={showLabels ? 1 : 0}
            >
                {label}
            </text>
        {/each}
        
        <!-- Party rectangles -->
        {#each profile.votes as vote, i}
            <rect 
                x={i * rectWidth} 
                y={rectsYPosition} 
                width={rectWidth} 
                height={rectHeight} 
                fill={PARTY_COLOURS[vote] || PARTY_COLOURS.NA}
                stroke="#ffffff"
                stroke-width="1"
            />
            {#if showLabels}
                <text 
                    x={i * rectWidth + rectWidth/2} 
                    y={textYOffset} 
                    text-anchor="middle"
                    fill="white"
                    font-weight="bold"
                    font-size="11" 
                >
                    {PARTY_NAMES_SHORT[vote] || 'NA'}
                </text>
            {/if}
        {/each}
    </svg>
    
    <div class="header">{profile.header}</div>
    <div class="description">{@html parseMarkdown(profile.description)}</div>
</div>

<style>
    .profile-container {
        margin-bottom: 10px;
    }
    
    .header {
        font-family: RobotoBold;
        color: var(--brandGray90);
        margin-top: 2px;  
    }
    
    .description {
        margin-top: 2px;  
        font-family: SourceSerif;
        color: var(--brandGray90);
    }

    .description strong {
        font-family: SourceSerifBold;
    }
</style>