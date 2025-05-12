<script>
    import Gen2Profile from "./Gen2Profile.svelte";

    const profiles = [
        {
            'votes': ['lib', 'lib', 'ndp', 'ndp', 'cons1'],
            'header': 'Ahmed, early 30s, Don Valley West',
            'description': '2-3 sentence quote from qualitative data',
        },
        {
            'votes': ['NA', 'ndp', 'ndp', 'lib', 'lib'],
            'header': 'Edward, mid 20s, Markham-Unionville',
            'description': '2-3 sentence quote from qualitative data',
        },
        {
            'votes': ['NA', 'NA', 'ndp', 'ndp', 'ndp'],
            'header': 'Priya, early 20s, Brampton East',
            'description': '2-3 sentence quote from qualitative data',
        },
        {
            'votes': ['lib', 'ndp', 'lib', 'ndp', 'cons1'],
            'header': 'Olivia, late 20s, Scarborough North',
            'description': '2-3 sentence quote from qualitative data',
        },
    ]
    
    const electionLabels = ["Fed. 2015", "Ont. 2018", "Fed. 2019", "Fed. 2021", "Ont. 2022"];
</script>

<div class="profiles-grid">
    {#each profiles as profile, i}
        <Gen2Profile 
            profile={profile}
            showLabels={i === 0}
            electionLabels={electionLabels}
        />
    {/each}
</div>

<style>
    .profiles-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
    }

    @media (max-width: 650px) {
        .profiles-grid {
            grid-template-columns: 1fr;
        }
    }
</style>