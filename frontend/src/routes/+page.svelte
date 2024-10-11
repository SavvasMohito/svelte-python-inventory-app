<script lang="ts">
	import Dashboard from '$lib/components/Dashboard.svelte';
	import Welcome from '$lib/components/Welcome.svelte';

	const { data } = $props();
</script>

<div class="flex w-full flex-grow justify-center">
	<div class="hero-content flex w-full flex-col items-center">
		{#if data.user}
			<Dashboard user={data.user} items={data.items} />
		{:else}
			<Welcome />
		{/if}
	</div>
</div>
