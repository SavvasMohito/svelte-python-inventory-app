<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import type { Item, User } from '$lib/types';
	import Logout from 'lucide-svelte/icons/log-out';
	import Items from './Items.svelte';

	const { user = $bindable(), items = $bindable() }: { user: User; items: Item[] } = $props();
</script>

<svelte:head>
	<title>Dashboard</title>
</svelte:head>

<div class="flex w-full max-w-screen-lg flex-col gap-10">
	<div class="flex items-center justify-between">
		<h2 class="text-4xl font-bold">Welcome back, {user?.username}!</h2>
		<form action="/login?/logout" method="post">
			<Button type="submit" variant="destructive" class="text-lg">
				<Logout class="mr-1 h-5 w-5" />
				Logout
			</Button>
		</form>
	</div>
	<Items {items} />
</div>
