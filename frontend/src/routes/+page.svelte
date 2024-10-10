<script lang="ts">
	import Welcome from '$lib/components/Welcome.svelte';
	import type { User } from '$lib/types.js';

	const { data } = $props();
	const { user }: { user: User } = data;
</script>

<div class="flex w-full flex-grow justify-center">
	<div class="hero-content flex w-full flex-col items-center">
		{#if user}
			<h2 class="mt-10">Hello, {user.username}</h2>
			<form action="/login?/logout" method="post">
				<button type="submit">Logout</button>
			</form>
		{:else}
			<Welcome />
		{/if}
	</div>
</div>
