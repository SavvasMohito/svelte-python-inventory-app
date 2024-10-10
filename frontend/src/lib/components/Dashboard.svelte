<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import * as Card from '$lib/components/ui/card';
	import type { User } from '$lib/types';

	const { user = $bindable() }: { user: User } = $props();
</script>

<svelte:head>
	<title>Dashboard</title>
</svelte:head>

