// import adapter from '@sveltejs/adapter-auto';
import adapter from '@sveltejs/adapter-static';

const dev = "production" === "development";

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
		    pages: "docs",
		    assets: "docs"
		}),
		prerender: {
			entries: ['*'] // prerender everything
		},
		paths: {
		    // change below to your repo name
		    base: dev ? "" : "/gta-immigration",
		}
	}
};

export default config;
