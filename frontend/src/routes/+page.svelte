<script lang="ts">
	const { data } = $props();
	const { message }: { message: string } = data;
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<h2 class="mt-10">Backend message:</h2>
<p>{message}</p>
