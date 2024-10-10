<script lang="ts">
	import type { User } from '$lib/types.js';

	const { data } = $props();
	const { message, user }: { message: string; user: User } = data;
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<h2 class="mt-10">Backend message:</h2>
<p>{message}</p>

{#if user}
	<h2 class="mt-10">Hello, {user.username}</h2>
	<form action="/login?/logout" method="post">
		<button type="submit">Logout</button>
	</form>
{/if}
