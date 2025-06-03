<script>
    import Gen2Profile from "./Gen2Profile.svelte";

    const profiles = [
        {
            'votes': ['lib', 'cons1', 'cons1', 'cons1', 'cons1'],
            'header': 'Syed, b. 1990, Don Valley East',
            'description': "Syed's parents, both working-class immigrants, spent decades navigating underemployment and Islamophobic stereotypes—especially after 9/11. Syed completed some university and now works as a personal banker. In his early twenties, he began moving right. By the time of our interview, he was a committed Conservative. When asked why, he said simply: **“I began to think more like a Canadian – and less like a Pakistani.”**",
        },
        {
            'votes': ['NA', 'cons1', 'cons1', 'cons1', 'cons1'],
            'header': 'Jessie, b. 2001, Scarborough Southwest',
            'description': "Jessie was raised by his single mother, a South Asian immigrant from Guyana. During his childhood, Jessie's mother refused social assistance even during their most difficult years. That lesson stuck. For Jessie, voting Conservative was not just about policy – it was a way to distance himself from the racialized stigma around welfare and to honour that ethic of self-reliance and prove that he belongs. **“You've arrived. You're a Canadian. So, start voting like one,”** he told me.",
        },
        {
            'votes': ['NA', 'cons1', 'cons1', 'cons1', 'cons1'],
            'header': 'Naomi, b. 1997, Don Valley North',
            'description': "Naomi's parents arrived from China with master's degrees but spent years in low-wage work, quietly rebuilding their lives in pursuit of middle-class stability. Naomi came of age in a household where success meant being dependable, discreet, and above all, respectable – leading her to avoid activist spaces, lest she be seen as ungrateful or difficult. Aligning with the right offered a kind of protection: a way to distance herself from racial grievance and to quietly belong. **“The Conservatives just seem... reasonable,”** she said. **“They don't make everything about race.”**",
        },
        {
            'votes': ['lib', 'NA', 'lib', 'cons1', 'NA'],
            'header': 'Anika, b. 1993, Markham-Unionville',
            'description': "The daughter of Tamil refugees, Anika grew up believing that the Liberal Party stood for inclusion and opportunity. But after a decade of stagnant wages and skyrocketing housing prices, she began to question whether those promises meant anything. Now in her early thirties, she still rents and sees homeownership slipping further out of reach. She worried that rising immigration levels were putting pressure on housing and public services, and felt that the government had failed to plan adequately. Disillusioned with the parties she had long supported, Anika turned to the Conservatives – not out of deep alignment, but out of a desire for something different.",
        },
        {
            'votes': ['ndp', 'lib', 'lib', 'cons1', 'cons1'],
            'header': 'Kevin, b. 1989, Mississauga East-Cooksville',
            'description': "Kevin, a second-generation Chinese Canadian, used to be a committed progressive. But after struggling with delayed career prospects and watching his parents' retirement savings dwindle, he started to see the Conservatives as the only party speaking to **“people like me who are trying to make it without [asking for] handouts.”**",
        },
    ]
    
    const electionLabels = ["Fed. 2015", "Ont. 2018", "Fed. 2019", "Fed. 2021", "Ont. 2022"];
</script>

<div class="profiles-container">
    <div class="plots-title">
        <h4>Many second-generation Canadians speak about disillusionment driving them right</h4>
        <p>Quotes from interviews with Conservative supporters</p>
    </div>
    <div class="profiles-grid">
        {#each profiles as profile, i}
            <Gen2Profile 
                profile={profile}
                showLabels={i === 0}
                electionLabels={electionLabels}
            />
        {/each}
    </div>
</div>

<style>
    .profiles-container {
        margin-top: -30px;
    }
    .profiles-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin-top: 25px;
    }

    @media (max-width: 650px) {
        .profiles-grid {
            grid-template-columns: 1fr;
        }
    }
</style>