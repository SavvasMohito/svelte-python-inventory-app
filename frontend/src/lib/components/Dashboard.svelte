<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import * as Card from '$lib/components/ui/card';
	import type { User } from '$lib/types';

	const { user = $bindable() }: { user: User } = $props();
</script>

<Card.Root class="w-full max-w-screen-lg">
	<Card.Header>
		<div class="flex items-center justify-between">
			<h2 class="text-4xl font-bold">Welcome back, {user?.username}!</h2>
			<form action="/login?/logout" method="post">
				<Button size="lg" type="submit" variant="destructive" class="text-lg">Logout</Button>
			</form>
		</div>
	</Card.Header>
	<Card.Content class="flex flex-col items-center gap-10"></Card.Content>
</Card.Root>
