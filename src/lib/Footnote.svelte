<script>
    export let id;
    let footnoteId = `footnote-${id}`;
    let refId = `footnote-ref-${id}`;
</script>

<a id={refId} href={`#${footnoteId}`} class="footnote-ref" on:click|preventDefault={() => {
    const element = document.getElementById(footnoteId);
    if (element) element.scrollIntoView({ behavior: 'auto', block: 'start' });
}}>
    {id}
</a>

<style>
    .footnote-ref {
        vertical-align: super;
        font-size: 0.8em;
        margin-left: 2px;
        text-decoration: none;
        color: #007FA3;
    }
</style>
