<script lang="ts">
	const { data } = $props();
	const { message, loggedIn }: { message: string; loggedIn: string } = data;
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<h2 class="mt-10">Backend message:</h2>
<p>{message}</p>

<h2 class="mt-10">Protected message:</h2>
<p>{loggedIn}</p>

<form action="/login?/logout" method="post">
	<button type="submit">Logout</button>
</form>
