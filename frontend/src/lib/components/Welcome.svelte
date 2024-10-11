<script lang="ts">
	import { buttonVariants } from '$lib/components/ui/button';
	import * as Card from '$lib/components/ui/card';
	import { ArrowRight } from 'lucide-svelte';

	const features = [
		'Add new items to your inventory',
		'Manage existing items',
		'Update item details',
		'Delete items you no longer need',
		'Track inventory levels',
		'Save items in your account'
	];
</script>

<svelte:head>
	<title>Welcome</title>
</svelte:head>

<Card.Root class="max-w-screen-lg space-y-10">
	<Card.Header class="flex items-center">
		<h2 class="text-4xl font-bold">Welcome to the Inventory Manager</h2>
	</Card.Header>
	<Card.Content class="flex flex-col items-center gap-10">
		<div class="flex flex-wrap justify-center gap-4">
			{#each features as feature}
				<Card.Root class="w-[400px] bg-primary/25">
					<Card.Content class="flex items-center justify-center gap-2">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-8 w-8 text-green-500"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M5 13l4 4L19 7"
							/>
						</svg>
						<span class="text-xl font-semibold">{feature}</span>
					</Card.Content>
				</Card.Root>
			{/each}
		</div>
		<a href="/login" class={buttonVariants({ size: 'lg', className: 'text-lg' })}>
			Get Started <ArrowRight class="ml-2 h-5 w-5" />
		</a>
	</Card.Content>
</Card.Root>
