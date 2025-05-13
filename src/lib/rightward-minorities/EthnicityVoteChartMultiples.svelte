<script>
    import { onMount } from "svelte";
    import { csvParse } from 'd3-dsv';
    import CircleBarChart from "./CircleBarChart.svelte";

    let {
        ethnicType,
        title,
        subtitle,
    } = $props();

    const NUM_RIDINGS = 5;
    const electionsInfoSA = [
        {'region': 'ont-', 'vm_type': 'sa', 'vm_field': 'pct_vm_sa', 'year': 2014, 'pct_cons_total': 31.2},
        {'region': 'ont-', 'vm_type': 'sa', 'vm_field': 'pct_vm_sa', 'year': 2025, 'pct_cons_total': 43.0},
        {'region': 'f', 'vm_type': 'sa', 'vm_field': 'pct_vm_sa', 'year': 2015, 'pct_cons_total': 31.9},
        {'region': 'f', 'vm_type': 'sa', 'vm_field': 'pct_vm_sa', 'year': 2025, 'pct_cons_total': 41.3},
    ];
    const electionsInfoChn = [
        {'region': 'ont-', 'vm_type': 'chn', 'vm_field': 'pct_vm_chn', 'year': 2014, 'pct_cons_total': 31.2},
        {'region': 'ont-', 'vm_type': 'chn', 'vm_field': 'pct_vm_chn', 'year': 2025, 'pct_cons_total': 43.0},
        {'region': 'f', 'vm_type': 'chn', 'vm_field': 'pct_vm_chn', 'year': 2015, 'pct_cons_total': 31.9},
        {'region': 'f', 'vm_type': 'chn', 'vm_field': 'pct_vm_chn', 'year': 2025, 'pct_cons_total': 41.3},
    ]

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
        let electionsInfo;
        if (ethnicType === 'sa') {
            electionsInfo = electionsInfoSA;
        } else if (ethnicType === 'chn') {
            electionsInfo = electionsInfoChn;
        }

        electionsData = await Promise.all(
            electionsInfo.map(async info => ({
                info,
                data: await loadCSV(info)
            }))
        );
    });
</script>

<div class="plots-title">
    <h4>
        {title}
    </h4>
    <p>
        {subtitle}
    </p>
</div>
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
        margin-top: 20px;
    }

    @media (max-width: 700px) {
        .charts-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
</style>