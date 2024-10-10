<script lang="ts">
	import Dashboard from '$lib/components/Dashboard.svelte';
	import Welcome from '$lib/components/Welcome.svelte';
	import type { User } from '$lib/types.js';

	const { data } = $props();
	const { user }: { user: User } = data;
</script>

<div class="flex w-full flex-grow justify-center">
	<div class="hero-content flex w-full flex-col items-center">
		{#if user}
			<Dashboard {user} />
		{:else}
			<Welcome />
		{/if}
	</div>
</div>
