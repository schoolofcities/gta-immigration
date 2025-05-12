<script>
    import { onMount } from "svelte";
    import { csvParse } from 'd3-dsv';
    import CircleBarChart from "./CircleBarChart.svelte";

    const NUM_RIDINGS = 5;
    const electionsInfo = [
        {'region': 'ont-', 'vm_type': 'sa', 'year': 2014, 'vm_field': 'pct_vm_sa'},
        {'region': 'ont-', 'vm_type': 'sa', 'year': 2025, 'vm_field': 'pct_vm_sa'},
        {'region': 'f', 'vm_type': 'sa', 'year': 2015, 'vm_field': 'pct_vm_sa'},
        {'region': 'f', 'vm_type': 'sa', 'year': 2025, 'vm_field': 'pct_vm_sa'},
        {'region': 'ont-', 'vm_type': 'chn', 'year': 2014, 'vm_field': 'pct_vm_chn'},
        {'region': 'ont-', 'vm_type': 'chn', 'year': 2025, 'vm_field': 'pct_vm_chn'},
        {'region': 'f', 'vm_type': 'chn', 'year': 2015, 'vm_field': 'pct_vm_chn'},
        {'region': 'f', 'vm_type': 'chn', 'year': 2025, 'vm_field': 'pct_vm_chn'},
    ];

    let electionsData = $state([]);

    async function loadCSV(info) {
        try {
            const csvPath = `/gta-immigration/data/elections_analysis/vm_cons/${info.region}ed_vm-${info.vm_type}_cons_${info.year}.csv`;
            const response = await fetch(csvPath);
            if (!response.ok) return null;
            const text = await response.text();
            const data = csvParse(text);
            return data.slice(0, NUM_RIDINGS);
        } catch {
            return null;
        }
    }

    onMount(async () => {
        electionsData = await Promise.all(
            electionsInfo.map(async info => ({
                info,
                data: await loadCSV(info)
            }))
        );
    });
</script>

<div class="charts-grid">
    {#if electionsData}
        {#each electionsData as election}
            <CircleBarChart 
                info={election.info}
                data={election.data}
                vmField={election.info.vm_field}
            />
        {/each}
    {/if}
</div>

<style>
    .charts-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
    }

    @media (max-width: 700px) {
        .charts-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
</style>