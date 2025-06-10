<script>
    export let footnotes;
</script>

<div class="footnotes">
    <h3>Footnotes</h3>
    {#each footnotes as footnote (footnote.id)}
        <div id={`footnote-${footnote.id}`} class="footnote-item">
            <sup>{footnote.id}</sup>
            <p style="display:inline">{@html footnote.text}</p>

            <a href={`#footnote-ref-${footnote.id}`} class="backlink" on:click|preventDefault={() => {
                const element = document.getElementById(`footnote-ref-${footnote.id}`);
                const yOffset = -100;
                if (element) {
                    const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
                    window.scrollTo({ top: y, behavior: 'auto' });
                }
            }}>
                ↩
            </a>
        </div>
    {/each}
</div>

<style>
    
    .footnote-item {
        margin-bottom: 0.5em;
        line-height: 1.4;
        position: relative;
        padding-left: 1.5em;
    }

    .footnote-item sup {
        position: absolute;
        left: 0;
    }

    .backlink {
        margin-left: 0.5em;
        text-decoration: none;
        color: #007FA3;
    }
</style>